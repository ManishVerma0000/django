from django.db import models
from ..models.user import PortalUser
from django.utils.timezone import now  # Import Django's timezone utility

class  AddCarasoulImage(models.Model):
    id = models.AutoField(primary_key=True)  # Auto-generated unique ID
    user = models.ForeignKey(
        PortalUser, 
        on_delete=models.CASCADE,  
        related_name="carasoul"  
    )
    photo = models.ImageField(upload_to='carasoul', null=True, blank=True)
    order=models.IntegerField(blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)  # Set default on creation
    updated_at = models.DateTimeField(auto_now=True)  # Auto-update on modification

    def __str__(self):
        return f"Testimonial by {self.user} - {self.message[:20]}..."
