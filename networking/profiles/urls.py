from django.urls import path
from django.contrib.auth import views as auth_views
from .views import (
    HomeView, UserProfileListView, UserProfileDetailView, 
    UserProfileCreateView, UserProfileUpdateView, UserProfileDeleteView, register, FieldOfWorkListView, FieldOfWorkCreateView,
    FieldOfWorkUpdateView, FieldOfWorkDeleteView
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
    path('fields/', FieldOfWorkListView.as_view(), name='field_list'),
    path('fields/create/', FieldOfWorkCreateView.as_view(), name='field_create'),
    path('fields/<int:pk>/update/', FieldOfWorkUpdateView.as_view(), name='field_update'),
    path('fields/<int:pk>/delete/', FieldOfWorkDeleteView.as_view(), name='field_delete'),
]


