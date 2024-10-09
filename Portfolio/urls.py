from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView  # Serves React app

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),  # Include API app URLs
    path('users/', include('users_app.urls')),  # Include user app URLs
    path('', TemplateView.as_view(template_name='index.html')),  # Serve React's index.html
    
]
