from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('resetPassword/', views.reset_password, name='resetPassword'),
    path('logout', views.logout, name='logout')
]
