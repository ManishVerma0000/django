from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from ..models.facilities_model import facilities
from ..serializers.facilities_serializers import facilitiesSearializers

@api_view(['POST'])
def create_facilities(request):
    if not isinstance(request.data, list):  # Ensure the request body is a list
        return Response({"error": "Expected an array of facilities"}, status=status.HTTP_400_BAD_REQUEST)

    created_facilities = []
    errors = []

    for facility_data in request.data:
        serializer = facilitiesSearializers(data=facility_data)
        if serializer.is_valid():
            serializer.save()
            created_facilities.append(serializer.data)
        else:
            errors.append(serializer.errors)

    if errors:
        return Response({"error": errors}, status=status.HTTP_400_BAD_REQUEST)
    
    return Response(created_facilities, status=status.HTTP_201_CREATED)

@api_view(['get'])
def get_facilities_per_user(request):
    try:
        user_id = request.query_params.get('userId') 
        vision_mission = facilities.objects.filter(user=user_id).order_by('order')
        serialized_vision_mission = facilitiesSearializers(vision_mission, many=True)
        return Response(serialized_vision_mission.data, status=status.HTTP_200_OK)
    except facilities.DoesNotExist:
        return Response({"error": "Vision And Mission not found"}, status=status.HTTP_404_NOT_FOUND)

@api_view(['get'])
def delete_facilities(request):
    try:
        visionId = request.query_params.get('id') 
        vision = facilities.objects.get(id=visionId)
        vision.delete()
        return Response({"message": "Vision And Mission deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
    except facilities.DoesNotExist:
        return Response({"error": "Vision And Mission not found"}, status=status.HTTP_404_NOT_FOUND)