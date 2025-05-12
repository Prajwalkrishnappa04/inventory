from django.contrib import admin
from django.urls import path
from inventoryapp import views  # Import views from the custom app
urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('delete/<int:pk>/', views.delete_purchase_item, name='delete_purchase_item'),]
