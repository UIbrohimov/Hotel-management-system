from django.urls import path

from .views import user_info_update_view, user_info_view, register, login_view, logout_view


urlpatterns = [
    path('update_profile/<int:pk>/', user_info_update_view, name='update_profile'),
    path('profile/', user_info_view, name='profile'),
    path('register/', register, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
]
