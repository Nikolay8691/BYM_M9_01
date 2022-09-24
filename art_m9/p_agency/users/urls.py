from django.urls import path
from . import views

app_name = 'users'
urlpatterns = [
    path('', views.index2, name = 'index2'),
    path('user/<int:user2_id>', views.user2, name = 'user2'),
    path('<int:user20_id>', views.user20, name = 'user20'),
    path('login', views.login_view, name = 'login'),
    path('logout', views.logout_view, name = 'logout'),
    path('logoutplus', views.logout_plus, name = 'logoutplus'),
    path('<int:user20_id>/create_profile2', views.create_profile2, name = 'create_profile2'),
    path('registerplus2', views.registerplus2, name = 'registerplus2'),
    path('<int:user2_id>/c_profile2', views.c_profile2, name = 'c_profile2'),
] 