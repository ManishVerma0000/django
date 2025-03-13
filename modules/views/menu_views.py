from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from ..models.menu_model import Menu
from ..models.user import PortalUser

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from ..models.user import PortalUser
from ..serializers.menu_serializers import SubMenuSerializer,MenuSerializer

@api_view(['POST'])
def create_menu(request):
    try:
        user_id = int(request.data.get("user"))
    except (TypeError, ValueError):
        return Response({"error": "Invalid User ID"}, status=status.HTTP_400_BAD_REQUEST)

    user = get_object_or_404(PortalUser, pk=user_id)  # Ensure user exists

    menus_to_create = []
    submenus_to_create = []

    text_list = request.data.getlist("text")
    path_list = request.data.getlist("path")
    content_list = request.data.getlist("content")
    has_submenu_list = request.data.getlist("has_submenu")
    order_list = request.data.getlist("order")
    image_list = request.FILES.getlist("image") if "image" in request.FILES else [None] * len(text_list)

    for i in range(len(text_list)):
        text = text_list[i]
        path = path_list[i]
        content = content_list[i]
        has_submenu = has_submenu_list[i].lower() == "true"
        order = int(order_list[i])
        image = image_list[i] if i < len(image_list) else None

        if has_submenu:  
            # Create a menu without storing content/images (submenus will handle that)
            menu = Menu(
                user=user,
                text=text,
                path=path,  
                content=content,  
                has_submenu=True,
                order=order,
                image=image
            )
            menus_to_create.append(menu)
        else:
            # If no submenu, store the content and image inside the submenu instead
            submenus_to_create.append({
                "text": text,
                "path": path,
                "content": content,
                "order": order,
                "image": image
            })

    # Bulk create menus
    created_menus = Menu.objects.bulk_create(menus_to_create)

    # Create submenus
    for submenu_data in submenus_to_create:
        submenu_serializer = SubMenuSerializer(data=submenu_data)
        if submenu_serializer.is_valid():
            submenu_serializer.save()
        else:
            return Response(submenu_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    return Response({"message": "Menus and submenus created successfully"}, status=status.HTTP_201_CREATED)
