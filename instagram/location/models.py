from django.db import models
from lib.common_models import BaseModel
from django.utils.translation import gettext_lazy as _

class Location(BaseModel):
    title = models.CharField(_('title'), max_length=32, blank=False)
    points = models.JSONField(_('point'), blank=False) # Sample : {'lat': 32.0992193, 'long': 65.3123123231}

    def __str__(self) :
        return self.title
    
    class Meta:
        verbose_name = _("location")
        verbose_name_plural = _("locations")