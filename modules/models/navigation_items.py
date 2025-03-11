from django.db import models
from django.contrib.auth.models import User  # Import User model

class Menu(models.Model):
    user = models.ForeignKey(
        User,  # Each menu belongs to a user
        on_delete=models.CASCADE,
        related_name='menus'
    )
    text = models.CharField(max_length=255)
    path = models.CharField(max_length=255, blank=True, null=True)
    content = models.TextField(blank=True, null=True)  # Added for submenus too
    image = models.ImageField(upload_to='menu_images/', blank=True, null=True)  # Added for submenus too
    has_submenu = models.BooleanField(default=False)
    order = models.IntegerField(default=0)
    parent = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,  # `null=True` means top-level menu items will have no parent
        blank=True,
        related_name='submenus'
    )

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.text} (User: {self.user.username})"
