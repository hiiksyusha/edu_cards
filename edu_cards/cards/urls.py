from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('cards/', views.card_view, name='card_view'),
    path('cards/table/', views.card_list, name='card_list'),
    path('cards/add/', views.add_card, name='add_card'),
    path('cards/upload/', views.upload_csv, name='upload_csv'),
    path('cards/edit/<int:pk>/', views.edit_card, name='edit_card'),
    path('cards/delete/<int:pk>/', views.delete_card, name='delete_card'),
]
