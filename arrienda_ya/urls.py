from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', views.home_view, name='home_url'),
    path('dashboard/', views.dashboard_view, name='dashboard_url'),
    path('login/', LoginView.as_view(next_page='dashboard_url'), name='login_url'),
    path('logout/', LogoutView.as_view(next_page='home_url'), name='logout_url'),
    path('register', views.register_view, name='register_url')
]