from django.db import models

class AddTestimonial(models.Model):
    message = models.EmailField()  # Save email as a unique identifier
    photo = models.ImageField(upload_to='photos', null=True, blank=True)  # Save images in media/user_photos/

    def __str__(self):
        return self.message
