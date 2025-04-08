from django.urls import path
from django.contrib.auth import views as auth_views
from .views import (
    HomeView, UserProfileListView, UserProfileDetailView, 
    UserProfileCreateView, UserProfileUpdateView, UserProfileDeleteView, register
)

urlpatterns = [

    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
    path('', HomeView.as_view(), name='home'),
    path('register/', register, name='register'),
    path('userprofiles/', UserProfileListView.as_view(), name='profile_list'),
    path('userprofiles/<int:pk>/', UserProfileDetailView.as_view(), name='profile_detail'),
    path('userprofiles/create/', UserProfileCreateView.as_view(), name='profile_create'),
    path('userprofiles/<int:pk>/update/', UserProfileUpdateView.as_view(), name='profile_update'),
    path('userprofiles/<int:pk>/delete/', UserProfileDeleteView.as_view(), name='profile_delete'),
]


