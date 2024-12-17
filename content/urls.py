from django.urls import path
from .views import content_api, device_status

urlpatterns = [
    path('content/<str:device_id>/', content_api, name='content_api'),
    path('status/', device_status, name='device_status'),
]
