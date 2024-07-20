from django.urls import path
from . import views

# The urls available for students to navigate with
urlpatterns = [
    path('', views.homePage, name='homePage'),
    path('thankYou', views.thankYou, name='thankYou'),
    
    
]