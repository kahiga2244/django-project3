from . import views
from django.urls import path, include
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('',views.index,name = 'index'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    # path('login/', auth_views.login, {'template_name': 'login.html'}, name='login'),
    path("logout/", LogoutView.as_view(), name="logout"),
    path('profile/<username>/', views.profile, name='profile'),
    path('profile/<username>/edit', views.edit_profile, name='edit'),
    path('create-hood/', views.create_hood, name='create_hood'),
    path('mahoodz/', views.mahoodz, name='mahoodz'),
    path('hood/<hood_id>', views.hood, name='hood'),
    path('join-hood/<id>', views.join_hood, name='join_hood'),
    path('leave-hood/<id>', views.leave_hood, name='leave_hood'),
    path('occupants/<hood_id>', views.hood_occupants, name='occupants'),
    path('business/<hood_id>', views.business, name='business'),
    path('post/<hood_id>', views.post, name='post'),
    path('search/', views.search, name='search'),

]