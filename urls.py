from django.urls import path
from . import views

urlpatterns = [
    path('', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
     path('logout/', views.logout_view, name='logout'),
     path('add/', views.add_medicine, name='add_medicine'),
    path('medicion/', views.medicine_list, name='medicine_list'),
     path('edit/<int:pk>/', views.edit_medicine, name='edit_medicine'),
     path('delete/<int:pk>/', views.delete_medicine, name='delete_medicine'),
]