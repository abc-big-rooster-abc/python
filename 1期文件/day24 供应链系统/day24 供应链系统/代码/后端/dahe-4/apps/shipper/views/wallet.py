import requests
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


class WithDrawSerializer(serializers.Serializer):
    amount = serializers.DecimalField(required=True, max_digits=8, decimal_places=2, coerce_to_string=False)
    ali_account = serializers.CharField(required=True)


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

    @action(detail=False, methods=['post'], url_path="withdraw")
    def withdraw(self, request):
        # 执行提现的逻辑
        # 1.获取用户提交的数据，表单的校验
        ser = WithDrawSerializer(data=request.data)
        if not ser.is_valid():
            return Response({"code": return_code.FIELD_ERROR, 'msg': "error", 'detail': ser.errors})

        amount = ser.data['amount']
        ali_account = ser.data['ali_account']

        # 2.可用余额 > 提现
        user_id = request.user['user_id']
        company_object = models.Company.objects.filter(id=user_id).first()

        if company_object.balance < amount:
            return Response({"code": return_code.SUMMARY_ERROR, 'msg': "余额不足"})

        # 3.创建交易记录
        """
        tran_id = gen_random_oid()
        models.TransactionRecord.objects.create(
            company=company_object,
            tran_type=-1,
            amount=amount,
            ali_account=ali_account,
            trans_id=tran_id,
            pay_status=0,
            auditor_status=0
        )

        # 4.减少账户余额
        company_object.balance -= amount
        company_object.freeze_balance += amount
        company_object.save()
        """

        tran_id = gen_random_oid()
        models.TransactionRecord.objects.create(
            company=company_object,
            tran_type=-1,
            amount=amount,
            ali_account=ali_account,
            trans_id=tran_id,
            pay_status=1
        )

        # 4.减少账户余额
        company_object.balance -= amount
        company_object.save()

        # 5.去实现转账（提现）
        ali_pay = AliPay(
            appid=settings.ALI_APPID,  # "2016102400754054"
            app_notify_url=settings.ALI_NOTIFY_URL,  # 通知URL：POST
            return_url=settings.ALI_RETURN_URL,  # 支付完成之后，跳转到这个地址: GET
            app_private_key_path=settings.ALI_APP_PRI_KEY_PATH,
            alipay_public_key_path=settings.ALI_PUB_KEY_PATH
        )
        query_params = ali_pay.transfer(
            out_biz_no=tran_id,  # 订单号
            trans_amount=float(amount),
            identity=ali_account,
            order_title="支付宝提现"
        )
        pay_url = "{}?{}".format(settings.ALI_GATEWAY, query_params)

        res = requests.get(pay_url)
        data_dict = res.json()
        # # {"alipay_fund_trans_uni_transfer_response":{"code":"10000","msg":"Success","order_id":"20221204110070000006260000848244","out_biz_no":"a3d634f4f15f1a289df250f588ccf4a9","pay_fund_order_id":"20221204110070001506260000849678","status":"SUCCESS"},"sign":"nNxCEnShXYwfaW+IIbu2gJhZ0Tfb0DcNaB5XUd1SU0MsDgeaFwQJlq8/0V7rrNi256AFzG/Fc4eTOuXKuByKDI2ozHZFmCfOwf7W/3N/76nW8MbesOlcweProFAZo8O1wchMeuicfs7+8tlPBjWvHkcmCMhPRpobckhWSzyR7GLG84/3zd+n4n1sA+16LwBIuzZYMl9CNrbgIOHWk3rqlGRRGQ+mJSsoWYbwtzMLkfk04QSUFGjwr61PXkr9hAvPZf6jdjglN6RC4n0iZD65qP8YE4RkcC1ecwW3KPTikztXsD0ZC0lIZAJ1e3odSicXj3/T2FcWgaFaZvq7KUESiw=="}
        if data_dict['alipay_fund_trans_uni_transfer_response']['code'] == "10000":
            return Response({'code': return_code.SUCCESS})
        else:
            return Response({'code': return_code.SUMMARY_ERROR, 'msg': "提现失败"})


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
