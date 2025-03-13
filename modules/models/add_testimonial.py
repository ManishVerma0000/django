from django.db import models
from ..models.user import PortalUser
from django.utils.timezone import now  # Import Django's timezone utility

class AddTestimonial(models.Model):
    id = models.AutoField(primary_key=True)  # Auto-generated unique ID
    user = models.ForeignKey(
        PortalUser, 
        on_delete=models.CASCADE,  
        related_name="testimonials"  
    )
    message = models.TextField()
    photo = models.ImageField(upload_to='photos', null=True, blank=True)
    type = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)  # Set default on creation
    updated_at = models.DateTimeField(auto_now=True)  # Auto-update on modification

    def __str__(self):
        return f"Testimonial by {self.user} - {self.message[:20]}..."
