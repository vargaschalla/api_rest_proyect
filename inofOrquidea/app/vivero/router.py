from rest_framework.routers import DefaultRouter
# 
from . import viewsets
# code
from django.urls import path, include
from . import viewsets
from rest_framework import routers

router = routers.DefaultRouter(trailing_slash=False)
router.register('viveros', viewsets.ViveroViewSet)

urlpatterns = router.get_urls()