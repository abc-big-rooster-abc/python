"""
Django settings for dahe project.

Generated by 'django-admin startproject' using Django 4.1.2.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-&1^mm3p$98f+5ysoocpvr!e!%(e$z^x#(q8h_p^obi#u_owzh$'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    # 'django.contrib.admin',
    # 'django.contrib.auth',
    # 'django.contrib.contenttypes',
    # 'django.contrib.sessions',
    # 'django.contrib.messages',
    'django.contrib.staticfiles',
    'apps.shipper.apps.ShipperConfig',
    'apps.base.apps.BaseConfig',
    'rest_framework'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    # 'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    # 'django.contrib.auth.middleware.AuthenticationMiddleware',
    # 'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'utils.ext.middlewares.auth.AuthMiddleware'
]

ROOT_URLCONF = 'dahe.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                # 'django.contrib.auth.context_processors.auth',
                # 'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'dahe.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

# LANGUAGE_CODE = 'en-us'
LANGUAGE_CODE = 'zh-hans'

# datetime.datetime.now() / datetime.datetime.utcnow() => utc时间
# TIME_ZONE = 'UTC'
# datetime.datetime.now() - 东八区时间 / datetime.datetime.utcnow() => utc时间
TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

# 影响自动生成数据库时间字段；
#       USE_TZ = True，创建UTC时间写入到数据库。
#       USE_TZ = False，根据TIME_ZONE设置的时区进行创建时间并写入数据库
USE_TZ = False

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379",  # 安装redis的主机的 IP 和 端口
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
            "CONNECTION_POOL_KWARGS": {
                "max_connections": 1000,
                "encoding": 'utf-8'
            },
            "PASSWORD": "qwe123"  # redis密码
        }
    }
}

REST_FRAMEWORK = {
    "UNAUTHENTICATED_USER": None,
    "UNAUTHENTICATED_TOKEN": None
}

# 文件目录个
MEDIA_ROOT = os.path.join(BASE_DIR, "media")
UPLOAD_PATH = 'upload/'
# http://127.0.0.1:8000/media/
# http://127.0.0.1:8000/media/1.png
MEDIA_URL = '/media/'


# 支付宝支付相关
ALI_APP_PRI_KEY_PATH = os.path.join(BASE_DIR, 'files', '应用私钥.txt')
ALI_PUB_KEY_PATH = os.path.join(BASE_DIR, 'files', '支付宝公钥.txt')

ALI_APPID = "2016082500309412"
ALI_GATEWAY = "https://openapi.alipaydev.com/gateway.do"

# 应该跳转到哪里？
#    - vue网址 http://localhost:8080/xxx/xxx/xx/
#    - API网址 http://127.0.0.1:8000/api/xxx/charge/../   [选择]

# 跳转+异步通知，是否需要做认证？我们 or  【支付宝认证】

ALI_RETURN_URL = "http://127.0.0.1:8000/api/shipper/wallet/charge/notify/"  # GET, 为什么GET能访问呀？是基于js做的跳转。location.href = 地址
ALI_NOTIFY_URL = "http://127.0.0.1:8000/api/shipper/wallet/charge/notify/"  # POST,不是公网IP所以没看到请求到来。

# ALI_RETURN_URL = ""  # GET,为什么GET能访问呀？是基于js做的跳转。location.href = 地址

