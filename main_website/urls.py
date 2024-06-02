from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name = 'aiche-home'),
    path('about/', views.about, name = 'aiche-about'),
    path('blog/', views.blog, name = 'aiche-blog'),
    path('contact/', views.contact, name = 'aiche-contact'),
    path('team/', views.team, name = 'aiche-team'),
    path('events/', views.events, name = 'aiche-events'),
] 