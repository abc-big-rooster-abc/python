from rest_framework.response import Response
from utils.ext import return_code
from django.http.response import Http404


class RetrieveModelMixin:
    def retrieve(self, request, *args, **kwargs):
        try:
            instance = self.get_object()  # 抛出异常  models.Compnay.objects.get(id=11111)
            serializer = self.get_serializer(instance)
            return Response({"code": return_code.SUCCESS, 'data': serializer.data})
        except Http404 as e:
            return Response({"code": return_code.NOT_FOUND, 'msg': "对象不存在"})
        except Exception as e:
            print(e)
            return Response({"code": return_code.SUMMARY_ERROR, 'msg': "请求失败"})


class ListRetrieveModelMixin:
    def list(self, request, *args, **kwargs):
        try:
            instance = self.get_object()  # 抛出异常  models.Compnay.objects.get(id=11111)
            serializer = self.get_serializer(instance)
            return Response({"code": return_code.SUCCESS, 'data': serializer.data})
        except Http404 as e:
            return Response({"code": return_code.NOT_FOUND, 'msg': "对象不存在"})
        except Exception as e:
            print(e)
            return Response({"code": return_code.SUMMARY_ERROR, 'msg': "请求失败"})


class UpdateModelMixin:
    def update(self, request, *args, **kwargs):
        try:
            partial = kwargs.pop('partial', False)
            instance = self.get_object()
            serializer = self.get_serializer(instance, data=request.data, partial=partial)
            if not serializer.is_valid():
                return Response({"code": return_code.FIELD_ERROR, 'msg': "error", 'detail': serializer.errors})
            self.perform_update(serializer)
            return Response({
                "code": return_code.SUCCESS,
                'msg': "success",
                'data': serializer.data
            })
        except Exception as e:
            return Response({"code": return_code.SUMMARY_ERROR, 'msg': "请求失败"})

    def perform_update(self, serializer):
        serializer.save()

    def partial_update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)


class CreateUpdateModelMixin:
    def get_instance(self):
        """ 这是一个钩子，返回对象，则表示更新；返回None则表示新建"""
        pass

    def create(self, request, *args, **kwargs):
        # 1.是否认证信息已存在
        instance = self.get_instance()
        if instance:
            serializer = self.get_serializer(instance, data=request.data, partial=True)
            if not serializer.is_valid():
                return Response({"code": return_code.FIELD_ERROR, 'msg': "error", 'detail': serializer.errors})
            self.perform_update(serializer)
            return Response({
                "code": return_code.SUCCESS,
                'msg': "success",
                'data': serializer.data
            })
        else:
            serializer = self.get_serializer(data=request.data)
            if not serializer.is_valid():
                return Response({"code": return_code.FIELD_ERROR, 'msg': "error", 'detail': serializer.errors})
            self.perform_create(serializer)
            return Response({
                "code": return_code.SUCCESS,
                'msg': "success",
                'data': serializer.data
            })

    def perform_create(self, serializer):
        # 新增数据到数据库钩子
        serializer.save()

    def perform_update(self, serializer):
        # 扩展在数据库更新时，可以自定义字段
        serializer.save()
