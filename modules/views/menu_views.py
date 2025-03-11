from rest_framework import generics, permissions
from ..models.menu import Menu
from ..serializers.menu_serializers import NavigationItemSerializer

class CreateNavigationItemView(generics.CreateAPIView):
    """API to create a new navigation item (menu or submenu)."""
    queryset = Menu.objects.all()
    serializer_class = NavigationItemSerializer
    permission_classes = [permissions.IsAuthenticated]  # Only authenticated users

    def perform_create(self, serializer):
        """Ensure that the user adding the navigation item is set automatically."""
        serializer.save(user=self.request.user)
