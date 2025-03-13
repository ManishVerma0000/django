from django.db import models
from .menu_model import Menu

class SubMenu(models.Model):
    menuId = models.ForeignKey(
        Menu,  # Each menu belongs to a user
        on_delete=models.CASCADE,
        related_name='submenus'
    )
    
    text = models.CharField(max_length=255)
    path = models.CharField(max_length=255, blank=True, null=True)
    content = models.TextField(blank=True, null=True)  # Added for submenus too
    image = models.ImageField(upload_to='submenuImage/', blank=True, null=True)  # Added for submenus too
    order = models.IntegerField(default=0)
    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.text} (Menu: {self.menuId.text})"
