from rest_framework.views import APIView
from rest_framework.response import Response
from utils.ext import return_code
from apps.base import models
from utils.jwt_auth import create_token
from apps.shipper.serializers.account import LoginSerializer, LoginSmsSerializer, RegisterSerializer, SendSmsSerializer


class LoginView(APIView):
    """ 用户登录 """

    def post(self, request):
        # 1.数据格式校验（不为空）
        # print(request.data)
        ser = LoginSerializer(data=request.data)
        # ser.is_valid(raise_exception=True)
        if not ser.is_valid():
            # print(ser.errors)
            return Response({"code": return_code.FIELD_ERROR, 'msg': "error", 'detail': ser.errors})

        # 2.数据库合法性校验 print(ser.data) # {user,pwd,}  mobile  password
        # 18630087660  root123
        # print(ser.data)
        instance = models.Company.objects.filter(**ser.data).first()
        if instance.auth_type == 1:
            auth_id = 0
        else:
            auth_id = instance.companyauth.id  # 对象  空

        # 2.1 登录失败
        if not instance:
            return Response({"code": return_code.SUMMARY_ERROR, 'msg': "用户名或密码错误"})

        # 2.2 登录成功，返回用户信息
        token = create_token({'user_id': instance.id, 'name': instance.name})
        return Response({
            "code": return_code.SUCCESS,
            'msg': "success",
            'data': {"token": token, 'name': instance.name, 'id': instance.id, 'auth_id': auth_id}
        })


class SendSmsView(APIView):

    def post(self, request):
        try:
            # 1.接收请求数据
            print(request.data)
            # 2.校验（手机格式 + 手机号必须存在）
            ser = SendSmsSerializer(data=request.data)
            if not ser.is_valid():
                return Response({"code": return_code.FIELD_ERROR, 'msg': "error", 'detail': ser.errors})
            import random
            random_code = random.randint(1000, 9999)
            print(random_code)
            # 3.短信接口-发短信（设置）

            # 4.保存到redis（启动redis服务、配置redis链接、请求保存）
            from django_redis import get_redis_connection
            conn = get_redis_connection("default")
            conn.set(ser.validated_data['mobile'], random_code, ex=60)

            # 5.返回
            return Response({"code": return_code.SUCCESS})

        except Exception as e:
            print(e)
            return Response({"code": return_code.SUMMARY_ERROR, 'msg': "发送失败"})


class LoginSmsView(APIView):
    def post(self, request):
        try:
            # 1.获取数据
            # print("短信登录", request.data)
            # 2.格式校验（手机格式、手机号存在、短信-去redis中获取+提交=比较）
            ser = LoginSmsSerializer(data=request.data)
            if not ser.is_valid():
                return Response({"code": return_code.FIELD_ERROR, 'msg': "error", 'detail': ser.errors})
            # 3.成功/失败
            instance = models.Company.objects.filter(mobile=ser.validated_data['mobile']).first()
            if instance.auth_type == 1:
                auth_id = 0
            else:
                auth_id = instance.companyauth.id  # 对象  空


            # 4.生成jwt token返回 + 跳转
            token = create_token({'user_id': instance.id, 'name': instance.name})
            return Response({
                "code": return_code.SUCCESS,
                'msg': "success",
                'data': {"token": token, 'name': instance.name, 'id': instance.id,'auth_id': auth_id}
            })
        except Exception as e:
            return Response({"code": return_code.SUMMARY_ERROR, 'msg': "发送失败"})


class RegisterSmsView(APIView):
    def post(self, request):
        try:
            # 1.获取数据
            # print(request.data)
            # 2.校验
            ser = RegisterSerializer(data=request.data)
            if not ser.is_valid():
                return Response({"code": return_code.FIELD_ERROR, 'msg': "error", 'detail': ser.errors})

            ser.validated_data.pop("code")
            ser.validated_data.pop("confirm_password")
            # 3.保存到数据库
            # ser.save(auth_type=2)
            ser.save()
            return Response({"code": return_code.SUCCESS})
        except Exception as e:
            return Response({"code": return_code.SUMMARY_ERROR, 'msg': "注册失败"})
