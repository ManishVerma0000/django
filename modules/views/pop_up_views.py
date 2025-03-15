from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view,parser_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser
from ..models.pop_up_image import PopUPImage

from django.shortcuts import get_object_or_404

from ..serializers.pop_up_image_serializer import PopUpImageSerializer


@api_view(['POST'])
@parser_classes([MultiPartParser, FormParser])  # Required to handle file uploads
def upload_pop_Up_images(request):
    serializer = PopUpImageSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET'])
def get_pop_up_images(request):
    user_id= request.query_params.get('userId') 
    popUpImages = PopUPImage.objects.filter(user_id=user_id)
    serializer = PopUpImageSerializer(popUpImages, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)



@api_view(["POST"])
def upload_popup_images(request):
    if "images" not in request.FILES:
        return Response({"error": "No images uploaded"}, status=status.HTTP_400_BAD_REQUEST)

    images = request.FILES.getlist("images")
    orders = request.POST.getlist("orders")
    user_id = request.POST.get("user") or request.user.id  # Use request.user.id if user is missing

    if not user_id:
        return Response({"error": "User ID is missing"}, status=status.HTTP_400_BAD_REQUEST)

    uploaded_images = []
    for img, order in zip(images, orders):
        data = {"user": user_id, "photo": img, "order": int(order)}  # Ensure user ID is passed
        serializer = PopUpImageSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            uploaded_images.append(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    return Response({"uploaded_images": uploaded_images}, status=status.HTTP_201_CREATED)



@api_view(['get'])
def get_pop_up_image_user(request):
    try:
        user_id= request.query_params.get('userId') 
        testimonials = PopUPImage.objects.filter(user_id=user_id)
        serializer = PopUpImageSerializer(testimonials, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except PopUPImage.DoesNotExist:
        return Response({"error":"Image not found"},status=status.HTTP_404_NOT_FOUND)
    

@api_view(['get'])
def delete_pop_up_image(request):
    try:
        image_id = request.query_params.get('id') 
        image = PopUPImage.objects.get(id=image_id)
        image.delete()
        return Response({"message": "Carousel image deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
    except PopUPImage.DoesNotExist:
        return Response({"error": "Image not found"}, status=status.HTTP_404_NOT_FOUND)