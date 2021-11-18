from django.urls import path
from . import views


urlpatterns = [
    path('get/', views.get_user),
    path('create/', views.create_user),
    path('admin-create/', views.admin_create_user),
]
