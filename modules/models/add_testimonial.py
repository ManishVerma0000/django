from django.db import models
from ..models.user import User

class AddTestimonial(models.Model):
    user = models.ForeignKey(
        User, 
        on_delete=models.CASCADE,  
        related_name="testimonials"  
    )
    message = models.TextField()  # Change from EmailField to TextField
    photo = models.ImageField(upload_to='photos', null=True, blank=True)  

    def __str__(self):
        return self.message
