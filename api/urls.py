from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register('tasks', TaskViewSet)
router.register('users', UserRegistrationViewSet)



urlpatterns = [
    path('', include(router.urls)),
    
    
]
