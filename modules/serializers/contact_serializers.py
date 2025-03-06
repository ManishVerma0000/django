from rest_framework import serializers
from ..models.contact import ContactUs



class ContactUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactUs
        fields = '__all__'  # OR list specific fields: ['name', 'email', 'message', 'created_at']
