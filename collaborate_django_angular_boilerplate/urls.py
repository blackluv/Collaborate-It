from django.conf.urls import patterns, url
from authentication.views import LogoutView

from collaborate_django_angular_boilerplate.views import IndexView
from rest_framework_nested import routers
from django.conf.urls import include
from authentication import views
from . import views as view

from authentication.views import LoginView
from authentication.views import AccountViewSet

router = routers.SimpleRouter()
router.register(r'accounts', AccountViewSet)

urlpatterns = patterns(
    '',
    url(r'^api/v1/', include(router.urls)),
    url(r'^api/v1/auth/login/$', LoginView.as_view(), name='login'),
    url(r'^api/v1/auth/logout/$', LogoutView.as_view(), name='logout'),
    url(r'^api/v1/auth/code/$', views.save_code, name='save_code'),
)