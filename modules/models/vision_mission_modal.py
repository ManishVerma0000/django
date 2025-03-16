from django.db import models
from .user import PortalUser

class VisionMission(models.Model):
    user = models.ForeignKey(
        PortalUser,  # Each menu belongs to a user
        on_delete=models.CASCADE,
        related_name='vision'
    )
    text = models.TextField()
    def __str__(self):
        return f"{self.text} (User: {self.user.username})"
