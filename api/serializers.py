# portfolio_app/serializers.py

from rest_framework import serializers
from .models import Portfolio, Hobbies, Contact

class PortfolioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Portfolio
        fields = '__all__'

class HobbiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hobbies
        fields = '__all__'

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'
