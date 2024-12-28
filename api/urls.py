from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register('task', TaskViewSet)
router.register('user', UserRegistrationViewSet)



urlpatterns = [
    path('', include(router.urls)),
    
    
]
