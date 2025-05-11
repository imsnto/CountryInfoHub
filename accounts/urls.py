from django.urls import path, include

from django.contrib.auth.views import LoginView, LogoutView
from rest_framework.authtoken.views import obtain_auth_token


from .views import ProfileView
from .forms import LoginForm
urlpatterns = [
    path('login/', LoginView.as_view(
        template_name="accounts/login.html",
        form_class=LoginForm
    ), name='login'),
    path('logout/', LogoutView.as_view(
        template_name="accounts/logout.html"
    ), name='logout'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
]