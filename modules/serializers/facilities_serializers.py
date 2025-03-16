from rest_framework import serializers
from ..models.facilities_model import facilities

class facilitiesSearializers(serializers.ModelSerializer):
    class Meta:
        model = facilities
        fields = '__all__' 
