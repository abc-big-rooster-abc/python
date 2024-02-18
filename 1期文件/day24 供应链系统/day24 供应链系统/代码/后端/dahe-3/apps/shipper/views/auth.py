from rest_framework.viewsets import ModelViewSet
from rest_framework import serializers
from rest_framework.decorators import action
from rest_framework.response import Response
from apps.base import models
from utils.ext import return_code
from datetime import datetime
import os
from django.conf import settings
from django.core.files.storage import default_storage
import base64


def get_upload_filename(file_name):
    date_path = datetime.now().strftime('%Y/%m/%d')
    upload_path = os.path.join(settings.UPLOAD_PATH, date_path)
    file_path = os.path.join(upload_path, file_name)
    return default_storage.get_available_name(file_path)


def baidu_ai(bytes_body):
    import base64
    import requests

    # client_id 为官网获取的AK， client_secret 为官网获取的SK
    response = requests.get(
        url="https://aip.baidubce.com/oauth/2.0/token",
        params={
            "grant_type": "client_credentials",
            "client_id": "PhGc5UK5e5UOkSqpNakZLpxL",
            "client_secret": "cS1OaU3GngGDdsZj2Fo7scd4j7S3M3Gw",
        }
    )
    data_dict = response.json()
    access_token = data_dict['access_token']
    # print(access_token)

    request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/idcard"
    # 二进制方式打开图片文件
    img = base64.b64encode(bytes_body)

    params = {"id_card_side": "front", "image": img}  # front/back
    request_url = request_url + "?access_token=" + access_token
    headers = {'content-type': 'application/x-www-form-urlencoded'}
    res = requests.post(request_url, data=params, headers=headers)
    res_dict = res.json()
    for k, v in res_dict['words_result'].items():
        print(k, v)


class AuthModelSerializers(serializers.ModelSerializer):
    auth_type_text = serializers.CharField(source="company.get_auth_type_display", read_only=True)
    auth_type_class = serializers.SerializerMethodField(read_only=True)

    licence_path_url = serializers.SerializerMethodField()
    leader_identity_front_url = serializers.SerializerMethodField()
    leader_identity_back_url = serializers.SerializerMethodField()

    class Meta:
        model = models.CompanyAuth
        # fields = "__all__"
        exclude = ["company"]
        extra_kwargs = {
            'remark': {"read_only": True},
        }

    def get_auth_type_class(self, obj):
        return models.Company.auth_type_class_map[obj.company.auth_type]

    def get_licence_path_url(self, obj):
        # request.
        # abs_url = request.build_absolute_uri(local_url)
        return self.context['request'].build_absolute_uri(obj.licence_path)

    def get_leader_identity_front_url(self, obj):
        return self.context['request'].build_absolute_uri(obj.leader_identity_front)

    def get_leader_identity_back_url(self, obj):
        return self.context['request'].build_absolute_uri(obj.leader_identity_back)


from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import CreateModelMixin, UpdateModelMixin, ListModelMixin
from utils.ext.mixins import RetrieveModelMixin
from utils.ext.mixins import CreateUpdateModelMixin
from utils.ext.auth import JwtAuthentication, JwtParamAuthentication, DenyAuthentication


class AuthView(RetrieveModelMixin, CreateUpdateModelMixin, GenericViewSet):
    authentication_classes = [JwtAuthentication, JwtParamAuthentication, DenyAuthentication]
    queryset = models.CompanyAuth.objects.all()
    serializer_class = AuthModelSerializers

    @action(detail=False, methods=['post'], url_path="upload")
    def upload(self, request):
        upload_object = request.FILES.get("file")
        # print(upload_object.name, upload_object.size)
        if upload_object.size > 10 * 1024 * 1024:
            return Response({
                "code": return_code.ERROR,
                "msg": "文件太大"
            })

        upload_url = get_upload_filename(upload_object.name)
        save_path = default_storage.save(upload_url, upload_object)
        local_url = default_storage.url(save_path)
        abs_url = request.build_absolute_uri(local_url)

        img_type = request.data.get("type")
        if img_type == "front":
            upload_object.seek(0)
            baidu_ai(upload_object.read())

        context = {
            "code": return_code.SUCCESS,
            'data': {
                'url': local_url,
                'abs_url': abs_url
            }
        }
        # 2.路径返回（第三方组件） {status:1}  {status:0 }
        return Response(context)

    def get_instance(self):
        # 已登录的用户信息  request.user = {'user_id': instance.id, 'name': instance.name}
        user_id = self.request.user['user_id']
        return models.CompanyAuth.objects.filter(company_id=user_id).first()

    def perform_create(self, serializer):
        user_id = self.request.user['user_id']
        instance = serializer.save(company_id=user_id, remark="")
        instance.company.auth_type = 2
        instance.company.save()
        
    def perform_update(self, serializer):
        instance = serializer.save(remark="")
        instance.company.auth_type = 2
        instance.company.save()
