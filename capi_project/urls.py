from django.contrib import admin
from django.conf.urls import url, include
from django.views.generic import TemplateView
from rest_framework import routers
from capi_project import views

router = routers.DefaultRouter()
router.register(r'cases', views.CaseViewSet)
router.register(r'jurisdictions', views.JurisdictionViewSet)
router.register(r'courts', views.CourtViewSet)
router.register(r'volumes', views.VolumeViewSet)
router.register(r'reporters', views.ReporterViewSet)

user_router = routers.DefaultRouter()
user_router.register(r'accounts', views.UserViewSet)

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='docs.html'), name='docs'),
    url(r'^', include(user_router.urls)),
    url(r'^api/v1/', include(router.urls)),
    url(r'^admin', include(admin.site.urls)),
    url(r'^accounts/verify-user/(?P<user_id>[\d+]+)/(?P<activation_nonce>[0-9a-z]+)/?$', views.verify_user),
]
