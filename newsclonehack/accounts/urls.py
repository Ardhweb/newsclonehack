from django.urls import path
# from accounts.views import UserRegister

from . import views

from django.contrib.auth import views as auth_views

urlpatterns = [
    path("register/", views.register, name="register"),
    path("login/", views.user_login, name="login"),

    # path('signup', views.UserRegister.as_view(), name='signup'),
    # # path('login', auth_views.LoginView.as_view(), name="login"),
    # # path('logout', auth_views.LogoutView.as_view(), {'next_page': 'login'}, name="logout"),
    
 
    
]

