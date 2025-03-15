from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view,parser_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser
from ..models.add_testimonial import AddTestimonial
from ..serializers.user_photo_serializer import UserPhotoSerializer;
from django.shortcuts import get_object_or_404


from ..serializers.contact_serializers import ContactUsSerializer


def testFunction(request):
    return HttpResponse("this is for the testing")

@api_view(['POST'])
@parser_classes([MultiPartParser, FormParser])  # Required to handle file uploads
def upload_user_photo(request):
    serializer = UserPhotoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET'])
def get_testimonials(request):
    testimonials = AddTestimonial.objects.all()
    serializer = UserPhotoSerializer(testimonials, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)



@api_view(['get'])
def delete_testimonial(request):
    try:
        testimonial_id = request.query_params.get('id') 
        testimonial = AddTestimonial.objects.get(id=testimonial_id)
        testimonial.delete()
        return Response({"message": "Testimonial deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
    except AddTestimonial.DoesNotExist:
        return Response({"error": "Testimonial not found"}, status=status.HTTP_404_NOT_FOUND)



@api_view(['GET'])
def get_testimonials_using_user_id(request):
    try:
        user_id = request.query_params.get('user') 
        if not user_id:
            return Response({"message":"Please enter the userId"})
        else:
            if user_id:
                testimonials = AddTestimonial.objects.filter(user_id=user_id)
                serializer = UserPhotoSerializer(testimonials, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
        
    except AddTestimonial.DoesNotExist:
        return Response({"error": "Testimonial not found"}, status=status.HTTP_404_NOT_FOUND)
