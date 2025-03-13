from django.db import models
from django.utils.translation import gettext_lazy as _

class PortalUser(models.Model):
    username = models.CharField(_("Name"), max_length=100)
    email = models.EmailField(_("Email"))
    password=models.CharField(_("Password"), max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.username} - {self.email}"
