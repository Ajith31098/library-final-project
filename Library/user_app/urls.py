from rest_framework.authtoken.views import obtain_auth_token
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from user_app import views

router = DefaultRouter()
router.register('useraproval', views.Aproval_view, basename='useraproval')


urlpatterns = [
    path('login/', obtain_auth_token, name='login'),
    path('register/', views.Registration_view.as_view(), name='register'),
    path('', include(router.urls)),
    path('logout/', views.Logout_view.as_view(), name='logout'),
]
