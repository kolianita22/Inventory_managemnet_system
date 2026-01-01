
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views




urlpatterns = [
    path('', views.Index, name='index'),
    path('dashboard/', views.Dashboard.as_view(), name='dashboard'), 
    path('signup/', views.SignUpView.as_view(), name='signup'),

    path('login/', auth_views.LoginView.as_view(template_name='inventory/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='inventory/logout.html'), name='logout')

]