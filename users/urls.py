from django.urls import path
from .views import register, profile, updateProfile
from django.contrib.auth import views as auth_views


urlpatterns =[
    path('register/', register, name="register"),
    path('profile/', profile, name="profile"),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html', redirect_authenticated_user=True), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('update/', updateProfile, name="updateProfile"),
] 