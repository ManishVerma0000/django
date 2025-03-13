from rest_framework import serializers
from django.contrib.auth.models import User
from ..models.menu_model import Menu;
from ..models.submenu_model import SubMenu;

class SubMenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubMenu
        fields = ['id', 'menuId', 'text', 'path', 'content', 'image', 'order']

class MenuSerializer(serializers.ModelSerializer):
    submenus = SubMenuSerializer(many=True, required=False)  # Allow nested submenus

    class Meta:
        model = Menu
        fields = ['id', 'user', 'text', 'path', 'content', 'image', 'has_submenu', 'order', 'submenus']

    def create(self, validated_data):
        submenus_data = validated_data.pop('submenus', [])  # Extract submenus if any
        menu = Menu.objects.create(**validated_data)

        # Create submenus linked to the menu
        for submenu_data in submenus_data:
            SubMenu.objects.create(menuId=menu, **submenu_data)

        return menu
