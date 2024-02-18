from django.conf import settings
from urllib.parse import parse_qs
from django.shortcuts import HttpResponse, redirect
from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework.decorators import action
from rest_framework.views import APIView

from apps.base import models
from utils.ext.auth import JwtAuthentication, JwtParamAuthentication, DenyAuthentication
from utils.ext.mixins import ListRetrieveModelMixin
from utils.ext import return_code
from utils.alipay import AliPay
from utils.encrypt import gen_random_oid


class WalletModelSerializers(serializers.ModelSerializer):
    total = serializers.SerializerMethodField()

    # balance = serializers.DecimalField(coerce_to_string=False, max_digits=10, decimal_places=2)

    class Meta:
        model = models.Company
        fields = ["total", "balance", "freeze_balance"]
        extra_kwargs = {
            "balance": {"coerce_to_string": False},
            "freeze_balance": {"coerce_to_string": False},
        }

    def get_total(self, obj):
        return obj.balance + obj.freeze_balance


class WalletView(ListRetrieveModelMixin, GenericViewSet):
    authentication_classes = [JwtAuthentication, JwtParamAuthentication, DenyAuthentication]
    queryset = models.Company.objects.all()
    serializer_class = WalletModelSerializers

    def get_object(self):
        queryset = self.filter_queryset(self.get_queryset())
        # 获取当前登录用户信息 request.user  request.auth
        # {'user_id': instance.id, 'name': instance.name}
        user_id = self.request.user['user_id']
        return queryset.filter(id=user_id).first()

    @action(detail=False, methods=['post'], url_path="charge")
    def charge(self, request):
        # 序列化进行校验
        user_id = request.user['user_id']

        out_trade_no = gen_random_oid()

        # 生成交易记录（待支付）
        models.TransactionRecord.objects.create(
            company_id=user_id,
            tran_type=1,
            amount=request.data['amount'],
            trans_id=out_trade_no,
            pay_status=0
        )

        ali_pay = AliPay(
            appid=settings.ALI_APPID,  # "2016102400754054"
            app_notify_url=settings.ALI_NOTIFY_URL,  # 通知URL：POST
            return_url=settings.ALI_RETURN_URL,  # 支付完成之后，跳转到这个地址: GET
            app_private_key_path=settings.ALI_APP_PRI_KEY_PATH,
            alipay_public_key_path=settings.ALI_PUB_KEY_PATH
        )
        query_params = ali_pay.direct_pay(
            subject="平台充值",  # 商品简单描述
            out_trade_no=out_trade_no,  # 商户订单号
            total_amount=request.data['amount']
        )

        pay_url = "{}?{}".format(settings.ALI_GATEWAY, query_params)
        return Response({"code": return_code.SUCCESS, 'data': pay_url})


class ChargeNotifyView(APIView):
    authentication_classes = []

    def get(self, request):
        # 支付成功后，页面会跳转到这里
        ali_pay = AliPay(
            appid=settings.ALI_APPID,  # "2016102400754054"
            app_notify_url=settings.ALI_NOTIFY_URL,  # 通知URL：POST
            return_url=settings.ALI_RETURN_URL,  # 支付完成之后，跳转到这个地址: GET
            app_private_key_path=settings.ALI_APP_PRI_KEY_PATH,
            alipay_public_key_path=settings.ALI_PUB_KEY_PATH
        )
        # 1.获取支付宝携带的参数
        params = request.GET.dict()
        sign = params.pop('sign', None)

        # 2.签名校验
        status = ali_pay.verify(params, sign)
        if status:
            # 状态=待支付 => 已支付（临时） out_trade_no
            out_trade_no = params['out_trade_no']

            # 订单状态修改
            tran_object = models.TransactionRecord.objects.filter(trans_id=out_trade_no, pay_status=0).first()

            # 订单状态更新
            tran_object.pay_status = 1
            tran_object.save()

            # 账户更新余额
            tran_object.company.balance += tran_object.amount
            tran_object.company.save()

            return redirect("http://localhost:8080/front/wallet?pay=success")
        return redirect("http://localhost:8080/front/wallet?pay=error")

    def post(self, request):
        # 异步通知，没接收到时，他重复通知
        ali_pay = AliPay(
            appid=settings.ALI_APPID,  # "2016102400754054"
            app_notify_url=settings.ALI_NOTIFY_URL,  # 通知URL：POST
            return_url=settings.ALI_RETURN_URL,  # 支付完成之后，跳转到这个地址: GET
            app_private_key_path=settings.ALI_APP_PRI_KEY_PATH,
            alipay_public_key_path=settings.ALI_PUB_KEY_PATH
        )
        # 1.获取支付宝携带的参数
        body_str = request.body.decode('utf-8')
        post_data = parse_qs(body_str)
        post_dict = {}
        for k, v in post_data.items():
            post_dict[k] = v[0]

        sign = post_dict.pop('sign', None)
        status = ali_pay.verify(post_dict, sign)
        if status:
            out_trade_no = post_dict['out_trade_no']
            # 3.状态=待支付 => 已支付（临时） out_trade_no
            # print("支付成功", out_trade_no)
            return HttpResponse('success')

        return HttpResponse('error')
