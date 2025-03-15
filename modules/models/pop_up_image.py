from django.db import models
from ..models.user import PortalUser
from django.utils.timezone import now  # Import Django's timezone utility

class  PopUPImage(models.Model):
    id = models.AutoField(primary_key=True)  # Auto-generated unique ID
    user = models.ForeignKey(
        PortalUser, 
        on_delete=models.CASCADE,  
        related_name="popupimage"  
    )
    order=models.IntegerField(blank=True,null=True)
    photo = models.ImageField(upload_to='popupimage', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True) 
    

    def __str__(self):
        return f"Testimonial by {self.user}."
