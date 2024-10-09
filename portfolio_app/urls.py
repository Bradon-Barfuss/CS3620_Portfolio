from django.urls import path
from . import views #import views from our current folder
from django.contrib.auth.views import LogoutView

app_name = "portfolio_app"
urlpatterns = [
    #Root it: portfolio_app/
    path('', views.home),
    path('home/', views.home, name="home"),
    path('Project/', views.Project, name="Project"),
    path('contact/', views.contact, name="contact"),
    path('Project/<int:portfolio_id>/', views.projectShowcase, name="projectShowcase"), 

    path('add/', views.create_contact, name="create_contact"),
    path('update/<int:contact_id>', views.update_contact, name="update_contact"),
    path('delete/<int:contact_id>', views.delete_contact, name="delete_contact"),

]

