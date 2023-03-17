from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('details/<int:id>', views.details_page),
    path('addpage/', views.add_page),
    path('delpage/', views.delete_page)
]
