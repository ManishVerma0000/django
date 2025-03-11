from rest_framework import serializers
from ..models.navigation_items import Menu

class NavigationItemSerializer(serializers.ModelSerializer):
    sub_items = serializers.SerializerMethodField()

    class Meta:
        model = Menu
        fields = ['id', 'user', 'text', 'path', 'parent', 'is_active', 'order', 'sub_items']
        extra_kwargs = {'user': {'read_only': True}}  # Prevent user modification

    def get_sub_items(self, obj):
        sub_items = obj.sub_items.all().order_by('order')
        return NavigationItemSerializer(sub_items, many=True).data

    def create(self, validated_data):
        request = self.context.get('request')
        if request and hasattr(request, "user"):
            validated_data["user"] = request.user
        return super().create(validated_data)

    def update(self, instance, validated_data):
        return super().update(instance, validated_data)
