from django.db import models
from .user import PortalUser

class facilities(models.Model):
    user = models.ForeignKey(
        PortalUser,  # Each menu belongs to a user
        on_delete=models.CASCADE,
        related_name='facilities'
    )
    text = models.TextField()
    heading= models.TextField()
    order = models.IntegerField(null=True, db_index=True)
    def __str__(self):
        return f"{self.text} (User: {self.user.username})"
    
    class Meta:
        ordering = ['order']
