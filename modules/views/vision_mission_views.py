from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from ..models.vision_mission_modal import VisionMission


from ..serializers.vision_mission_serializers import VisionMissionSearializers

@api_view(['POST'])
def create_vision_mission(request):
    requestBody=VisionMissionSearializers(data=request.data)
    if(requestBody).is_valid():
        requestBody.save()
        return Response(requestBody.data,status=status.HTTP_201_CREATED)
    return Response(requestBody.errors,status=status.HTTP_400_BAD_REQUEST)



@api_view(['get'])
def get_vision_mission_per_user(request):
    try:
        user_id = request.query_params.get('userId') 
        vision_mission = VisionMission.objects.filter(user=user_id)
        serialized_vision_mission = VisionMissionSearializers(vision_mission, many=True)
        return Response(serialized_vision_mission.data, status=status.HTTP_200_OK)
    except VisionMission.DoesNotExist:
        return Response({"error": "Vision And Mission not found"}, status=status.HTTP_404_NOT_FOUND)



    
@api_view(['get'])
def delete_vision_mission(request):
    try:
        visionId = request.query_params.get('id') 
        vision = VisionMission.objects.get(id=visionId)
        vision.delete()
        return Response({"message": "Vision And Mission deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
    except VisionMission.DoesNotExist:
        return Response({"error": "Vision And Mission not found"}, status=status.HTTP_404_NOT_FOUND)