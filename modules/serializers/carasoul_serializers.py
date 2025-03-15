from rest_framework import serializers
from ..models.carasoul_model import AddCarasoulImage
# Adjust import as needed

class AddCarasoulImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = AddCarasoulImage
        fields = ['id', 'user', 'photo', 'order', 'created_at', 'updated_at','user_details']
    user_details = serializers.SerializerMethodField()

    def get_user_details(self, obj):
        return {
            "id": obj.user.id,
            "username": obj.user.username,
            "email": obj.user.email,
        }
