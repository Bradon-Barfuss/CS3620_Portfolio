# Start of Selection
from rest_framework import serializers  # Import rest_framework
from portfolio_app.models import Contact, Project




class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'  # Include all fields from the Contact model

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'  # Include all fields from the Portfolio model

