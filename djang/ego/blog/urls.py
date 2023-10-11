from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog, name='blog'),
    path('<int:pk>/', views.post, name='post'),
    path('postdel/<int:pk>/', views.postdel, name='postdel'),
]