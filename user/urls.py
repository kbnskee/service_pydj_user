from django.urls import path
from . import views


urlpatterns = [
    path('', views.getUsers),
    path('id/<int:id>/', views.getUserById),
    path('un/<str:username>/', views.getUserByUsername),
    path('create/', views.createUser),
    path('create-admin/', views.createUserByAdmin),
    path('change_password/<int:id>/', views.changePassword),
]
