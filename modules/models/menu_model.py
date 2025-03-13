from django.db import models
from .user import PortalUser

class Menu(models.Model):
    user = models.ForeignKey(
        PortalUser,  # Each menu belongs to a user
        on_delete=models.CASCADE,
        related_name='menus'
    )
    text = models.CharField(max_length=255)
    path = models.CharField(max_length=255, blank=True, null=True)
    content = models.TextField(blank=True, null=True)  # Added for submenus too
    image = models.ImageField(upload_to='menu_images/', blank=True, null=True)  # Added for submenus too
    has_submenu = models.BooleanField(default=False)
    order = models.IntegerField(default=0)
    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.text} (User: {self.user.username})"
