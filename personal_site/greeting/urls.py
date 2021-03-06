from django.urls import path
from django.contrib.sitemaps.views import sitemap

from . import views


app_name = 'greeting'

urlpatterns = [
    path('', views.IndexView, name='index'),
    path('resume/', views.ResumeView, name='resume'),
    path('contact/', views.ContactView, name='contact'),
]

