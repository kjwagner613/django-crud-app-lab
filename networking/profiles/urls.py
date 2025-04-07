from django.urls import path
from . import views
from .views import UserProfileCreateView  # Ensure this import is correct

urlpatterns = [
    path('create/', UserProfileCreateView.as_view(), name='create_profile'),
    path('', views.Home.as_view(), name='home'),
    path('about/', views.about, name='about'),
    path('UserProfiles/', views.UserProfile_index, name='UserProfile-index'),
    path('UserProfiles/<int:UserProfile_id>/', views.UserProfile_detail, name='UserProfile-detail'),
    path('UserProfiles/create/', views.UserProfileCreate.as_view(), name='UserProfile-create'),
    path('UserProfiles/<int:pk>/update/', views.UserProfileUpdate.as_view(), name='UserProfile-update'),
    path('UserProfiles/<int:pk>/delete/', views.UserProfileDelete.as_view(), name='UserProfile-delete'),
    path('UserProfiles/<int:profile_id>/add-FieldOfWork/', views.FieldOfWork, name='add-FieldOfWork'),
    path('accounts/signup/', views.signup, name='signup'),
]
