from django.urls import path
from . import views

urlpatterns = [
    path('', views.news_list, name='news_list'),
    path('article/', views.load_page, name='load'),
    path('create/', views.create, name='create'),
    path('save/',views.add, name='add')
]