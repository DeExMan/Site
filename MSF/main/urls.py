from django.urls import path, reverse_lazy, include
from django.contrib.auth import views
from django.conf.urls import url
from .views import *
from .views import CustomObtainAuthToken
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('tiltyards', TiltyardViewSet, basename='tiltyards')
router.register('users', UserViewSet)
router.register('users/$/', UserViewSet)
router.register('referees', RefereesViewSet)
router.register("freeFighters", FreeFightersViewSet)


app_name = 'main'
urlpatterns = [
    path('', index, name='index'),
    path('clubs/', clubs, name='clubs'),
    path('login/', views.LoginView.as_view(template_name = 'main/login.html'), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('register/', register, name='register'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,32})/$', activate, name='activate'),
    path('profile/', profile, name='profile'),
    path('profile-change/', profile_change, name='profile_change'),
    path('password-change/', views.PasswordChangeView.as_view(template_name = 'main/password_change.html', success_url=reverse_lazy('main:password_change_done')), name='password_change'),
    path('password-change/done/', views.PasswordChangeDoneView.as_view(template_name = 'main/password_change_done.html'), name='password_change_done'),
    path('api/', include(router.urls)),
    url(r'^authenticate/', CustomObtainAuthToken.as_view()),
]
