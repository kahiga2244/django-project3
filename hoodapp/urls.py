from . import views
from django.urls import path, include
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('',views.index,name = 'index'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path("logout/", LogoutView.as_view(), name="logout"),
    path('profile/<username>/', views.profile, name='profile'),
    path('profile/<username>/edit', views.edit_profile, name='edit'),
    path('create-hoodz/', views.create_hoodz, name='create_hoodz'),
    path('mahoodz/', views.mitaa, name='mahoodz'),
    path('hoodz/<hoodz_id>', views.hoodz, name='hoodz'),
    path('join-hoodz/<id>', views.join_hoodz, name='join_hoodz'),
    path('leave-hoodz/<id>', views.leave_hoodz, name='leave_hoodz'),
    path('occupants/<hoodz_id>', views.hoodz_occupants, name='occupants'),
    path('business/<hoodz_id>', views.business, name='business'),
    path('post/<hoodz_id>', views.post, name='post'),
    path('search/', views.search, name='search'),

]