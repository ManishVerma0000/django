from rest_framework import serializers
from ..models.add_testimonial import AddTestimonial

class UserPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = AddTestimonial
        fields = ['message', 'photo','user','type','created_at','updated_at','id']  # Explicitly define fields

    def validate_photo(self, value):
        if not value:
            raise serializers.ValidationError("Photo is required.")
        return value
