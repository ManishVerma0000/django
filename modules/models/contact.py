from django.db import models
from django.utils.translation import gettext_lazy as _
from ..models.user import User

class ContactUs(models.Model):
    user = models.ForeignKey(
        User, 
        on_delete=models.CASCADE,  # If user is deleted, delete all related contacts
        related_name="contacts"  # Allows reverse querying (user.contacts.all())
    )
    name = models.CharField(_("Name"), max_length=100)
    email = models.EmailField(_("Email"))
    phone= models.IntegerField(_("Phone"))
    address = models.TextField(_("Address"))
    landMark = models.TextField(_("LandMark"))
    state=models.TextField(_('State'))
    
    
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.email}"
