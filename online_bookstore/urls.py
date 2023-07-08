
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('bookstore.urls')),
    path('index/', views.index, name='index')
]
