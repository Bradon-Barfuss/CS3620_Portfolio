from django.urls import path
from . import views

urlpatterns = [
    path('contacts/', views.ContactListView.as_view(), name='contact-list'),  # Example contact API
    path('Project/', views.ProjectListView.as_view(), name='project-list'),  # Example project API
]
