from django.urls import path

from . import views
from . import api

from .api import create_bookmark

urlpatterns = [
  path('login/', views.login_view, name='login'),
  path('register/', views.register_view, name = 'signup'),
  path('logout/', views.logout_view, name = 'logout'),

]