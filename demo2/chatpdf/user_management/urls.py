from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('approve_lecturer/', views.approve_lecturer, name='approve_lecturer'),
    path('pending_approval/', views.pending_approval, name='pending_approval'),
]
