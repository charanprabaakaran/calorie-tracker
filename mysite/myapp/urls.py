from django.urls import path, include
from . import views  # Import views from the current app
from myapp import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.index, name='index'),  # Home page
    path('register/', views.register, name='register'),  # Register page
    path('accounts/', include('django.contrib.auth.urls')),  # Built-in auth views (login/logout)
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
