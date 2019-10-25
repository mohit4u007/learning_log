"""Defines URL patterns for users"""
from django.conf.urls import url
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
	# Login page
  url(r'^login/$', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),

	# Logout page
	url(r'^logout/$', views.logout_view, name='logout'),

	# Registration page
	url(r'^register/$', views.register, name='register'),
]