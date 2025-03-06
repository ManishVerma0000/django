from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from ..models.contact import ContactUs
from django.shortcuts import get_object_or_404

from ..serializers.contact_serializers import ContactUsSerializer


def testFunction(request):
    return HttpResponse("this is for the testing")

@api_view(['POST'])
def create_contactUs(request):
    requestBody=ContactUsSerializer(data=request.data)
    if requestBody.is_valid():
        requestBody.save()
        return Response(requestBody.data, status=status.HTTP_201_CREATED)
    return Response(requestBody.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_all_contacts(request):
    contacts = ContactUs.objects.all()
    serializer = ContactUsSerializer(contacts, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)



@api_view(['GET'])
def get_contact_by_id(request, id):
    contact = get_object_or_404(ContactUs, id=id)
    serializer = ContactUsSerializer(contact)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['PUT'])
def update_contact_details_using_id(request, id):
    contact = get_object_or_404(ContactUs, id=id)
    serializer = ContactUsSerializer(contact, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()  # Save updated data
        return Response({"message": "Contact updated successfully", "data": serializer.data}, status=status.HTTP_200_OK)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)