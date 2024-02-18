#!/usr/bin/env python
# -*- coding:utf-8 -*-
import jwt
import datetime
from jwt import exceptions
from django.conf import settings


def create_token(payload, timeout=20):
    """
    :param payload:  例如：{'user_id':1,'username':'wupeiqi'}用户信息
    :param timeout: token的过期时间，默认20分钟
    :return:
    """
    headers = {
        'typ': 'jwt',
        'alg': 'HS256'
    }
    payload['exp'] = datetime.datetime.utcnow() + datetime.timedelta(hours=timeout)
    result = jwt.encode(payload=payload, key=settings.SECRET_KEY.encode('utf-8'), algorithm="HS256", headers=headers)
    return result


def parse_payload(token):
    """
    对token进行和发行校验并获取payload
    :param token:
    :return:
    """
    try:
        verified_payload = jwt.decode(token, settings.SECRET_KEY.encode('utf-8'), algorithms=["HS256"])
        return True, verified_payload
    except exceptions.ExpiredSignatureError:
        error = 'token已失效'
    except jwt.DecodeError:
        error = 'token认证失败'
    except jwt.InvalidTokenError:
        error = '非法的token'
    return False, error
