from django.urls import path
from django.conf.urls import include
from api import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('profile', views.ProfileView, basename='profile')

urlpatterns = [
    path('', include(router.urls)),
    path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    path('signup/', views.SignupView.as_view()),
    path('order/<int:profile_id>/', views.OrderView.as_view()),
]