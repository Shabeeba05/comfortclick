from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import register, login_view, home  

urlpatterns = [
    path('', home, name='home'),
    path('register/', register, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
]
