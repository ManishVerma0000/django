from rest_framework import serializers
from ..models.user import PortalUser

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = PortalUser
        fields = '__all__'  # Include all fields, or specify like ('name', 'created_at')
