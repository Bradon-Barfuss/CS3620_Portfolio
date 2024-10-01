from django.urls import path
from . import views #import views from our current folder

app_name = "portfolio_app"
urlpatterns = [
    #Root it: portfolio_app/
    path('', views.home, name="home"),
    path('home/', views.home, name="home"),
    path('hobbies/', views.hobbies, name="hobbies"),
    path('portfolio/', views.portfolio, name="portfolio"),
    path('contact/', views.contact, name="contact"),
    path('portfolio/<int:portfolio_id>/', views.projectShowcase, name="projectShowcase"), 
    path('hobbies/<int:hobby_id>/', views.hobbyShowcase, name="hobbyShowcase"), 

]

