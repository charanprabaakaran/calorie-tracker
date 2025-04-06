from django.urls import path, include
from . import views  # Import views from the current app
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='index'),  # Home page
    path('register/', views.register, name='register'),  # Register page
    path('accounts/', include('django.contrib.auth.urls')),  # Built-in auth views (login/logout)
]
