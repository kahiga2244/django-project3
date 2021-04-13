from . import views
from django.urls import path, include
from django.contrib.auth.views import LogoutView

urlpatterns = [
    # path('',views.index,name = 'index'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),

]