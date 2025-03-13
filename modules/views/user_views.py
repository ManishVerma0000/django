from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from ..models.user import PortalUser;
from ..serializers.user_serializers import UserSerializer
from django.contrib.auth.hashers import check_password

@api_view(['POST'])
def create_user(request):
    requestBody=UserSerializer(data=request.data)
    if(requestBody).is_valid():
        requestBody.save()
        return Response(requestBody.data,status=status.HTTP_201_CREATED)
    return Response(requestBody.errors,status=status.HTTP_400_BAD_REQUEST)



@api_view(['POST'])
def login_user(request):
    username=request.data.get("username")
    password = request.data.get("password")
    if not username or not password:
        return Response({"error": "Username and password are required"}, status=status.HTTP_400_BAD_REQUEST)
    if(username):
        user = PortalUser.objects.get(username=username)
        if password==user.password: 
            return Response({"message": "Login successful", "user_id": user.id}, status=status.HTTP_200_OK)
        else:
            print(user.password,'user.password')
            return Response({"message":"Invalid Password"}, status=status.HTTP_401_UNAUTHORIZED)
    return Response(request.data.username,status=status.HTTP_400_BAD_REQUEST)
    
  