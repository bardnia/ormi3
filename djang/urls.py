from django.contrib import admin
from django.urls import path
from main.views import index, about, contact, login, logout, blog, blog1, blog2, blog3

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('about/about/', about),
    path('contact/contact/', contact),
    path('accounts/login/', login),
    path('accounts/logout/', logout),
    path('blog/base/', blog),
    path('blog/1/', blog1),
    path('blog/2/', blog2),
    path('blog/3/', blog3),
]
