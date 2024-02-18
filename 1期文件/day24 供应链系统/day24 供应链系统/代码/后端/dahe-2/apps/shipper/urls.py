from django.urls import path

from rest_framework import routers

from .views import account, basic, auth, wallet

router = routers.SimpleRouter()
router.register(r'basic', basic.BasicView)
router.register(r'auth', auth.AuthView)
router.register(r'wallet', wallet.WalletView)

urlpatterns = [
    path('login/', account.LoginView.as_view()),
    path('send/sms/', account.SendSmsView.as_view()),
    path('login/sms/', account.LoginSmsView.as_view()),
    path('register/', account.RegisterSmsView.as_view()),

    # path('upload/', account.RegisterSmsView.as_view()),
]
urlpatterns += router.urls
