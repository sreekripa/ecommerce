from django.urls import path
from . import views
app_name='accounts'

urlpatterns = [
    path('accounts/register',views.register,name='register'),
    path('accounts/login', views.login, name='login'),
    path('accounts/logout', views.logout, name='logout'),
]