from rest_framework import serializers
from ..models.vision_mission_modal import VisionMission

class VisionMissionSearializers(serializers.ModelSerializer):
    class Meta:
        model = VisionMission
        fields = '__all__' 
