from django.urls import path
from . import views

app_name = 'campaigns'
urlpatterns = [
    path('', views.index, name = 'index'),
    path('users/<int:user2_id>', views.indexplususer2, name = 'indexplususer2'),
    path('users/<int:user2_id>/add', views.add, name = 'add'),
    path('index2', views.index2, name = 'index2'),
    path('cu_index', views.cu_index, name = 'cu_index'),
    path('cu_index/<int:checkup_id>', views.checkup, name = 'checkup'),
    path('<int:campaign_id>', views.campaign, name = 'campaign'),
    path('<int:campaign_id>/book', views.book, name = 'book'),
    path('houses', views.h_index, name = 'h_index'),
    path('houses/<int:house_id>', views.house, name = 'house'),
    path('houses2/<int:user2_id>', views.h2_index, name = 'h2_index'),        
] 