from django.urls import path
from amina import views


urlpatterns = [
    path('', views.home, name='home'),
    path('amina/', views.amina, name='amina'),
    path('<int:pk>/', views.bio, name='bio'),
]