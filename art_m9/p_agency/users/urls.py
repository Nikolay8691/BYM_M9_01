from django.urls import path
from . import views

app_name = 'users'
urlpatterns = [
    path('', views.index2, name = 'index2'),
    path('<int:user2_id>', views.user2, name = 'user2'),
    path('login', views.login_view, name = 'login'),
    path('logout', views.logout_view, name = 'logout'),

] 