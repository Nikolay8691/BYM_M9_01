from django.urls import path
from . import views
# from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth import views as auth_views

app_name = 'users'

urlpatterns = [
    path('', views.index2, name = 'index2'),
    path('user/<int:user2_id>', views.user2, name = 'user2'),
    path('<int:user20_id>', views.user20, name = 'user20'),
    path('login', views.login_view, name = 'login'),
    path('logout', views.logout_view, name = 'logout'),
    path('c_delete/<int:campaign_id>', views.c_delete, name = 'c_delete'),
    path('logoutplus', views.logout_plus, name = 'logoutplus'),
    path('<int:user20_id>/create_profile2', views.create_profile2, name = 'create_profile2'),
    path('registerplus2', views.registerplus2, name = 'registerplus2'),
    path('<int:user2_id>/c_profile2', views.c_profile2, name = 'c_profile2'),
    path('c_password', views.c_password, name = 'c_password'),
    # path('<int:user2_id>/c_password', views.c_password, name = 'c_password'),
    # path('c_password', auth_views.PasswordChangeView.as_view(template_name = 'users/c_password.html'), name = 'c_password'),
] 