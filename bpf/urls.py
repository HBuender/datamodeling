from django.urls import include, path

from . import views
from rest_framework import routers

from bpf.views import OrganizationViewSet, EmployeeViewSet


router = routers.DefaultRouter()
router.register(r'organization', OrganizationViewSet)
router.register(r'employee', EmployeeViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

