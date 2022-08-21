from django.urls import path
from . import views

app_name = 'campaigns'
urlpatterns = [
    path('', views.index, name = 'index'),
    path('<int:campaign_id>', views.campaign, name = 'campaign'),

] 