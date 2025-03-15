from rest_framework import serializers
from ..models.pop_up_image import PopUPImage
# Adjust import as needed

class PopUpImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PopUPImage
        fields = ['id', 'user', 'photo', 'order', 'created_at', 'updated_at','user_details']
    user_details = serializers.SerializerMethodField()

    def get_user_details(self, obj):
        return {
            "id": obj.user.id,
            "username": obj.user.username,
            "email": obj.user.email,
        }
