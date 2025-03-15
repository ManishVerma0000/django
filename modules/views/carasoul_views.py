from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from ..models.carasoul_model import AddCarasoulImage;
from ..serializers.carasoul_serializers import AddCarasoulImageSerializer

@api_view(['POST'])
def add_carasoul_image(request):
    serializer = AddCarasoulImageSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "Carousel image added successfully", "data": serializer.data}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['get'])
def delete_carasoul_image(request):
    try:
        image_id = request.query_params.get('id') 
        image = AddCarasoulImage.objects.get(id=image_id)
        image.delete()
        return Response({"message": "Carousel image deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
    except AddCarasoulImage.DoesNotExist:
        return Response({"error": "Image not found"}, status=status.HTTP_404_NOT_FOUND)



@api_view(['get'])
def getCarasoulList(request):
    try:
        testimonials = AddCarasoulImage.objects.all()
        serializer = AddCarasoulImageSerializer(testimonials, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except AddCarasoulImage.DoesNotExist:
        return Response({"error":"Image not found"},status=status.HTTP_404_NOT_FOUND)
    
    
    
@api_view(['get'])
def getCarasoulListPerUser(request):
    try:
        user_id= request.query_params.get('userId') 
        testimonials = AddCarasoulImage.objects.filter(user_id=user_id)
        serializer = AddCarasoulImageSerializer(testimonials, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except AddCarasoulImage.DoesNotExist:
        return Response({"error":"Image not found"},status=status.HTTP_404_NOT_FOUND)

@api_view(["POST"])
def upload_carousel_images(request):
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
        serializer = AddCarasoulImageSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            uploaded_images.append(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    return Response({"uploaded_images": uploaded_images}, status=status.HTTP_201_CREATED)