from django.db import models
from django.utils.translation import gettext_lazy as _

class BaseModel (models.Model):
    created_time = models.DateTimeField(_('created time'), auto_now_add=True)
    modified_time = models.DateTimeField(_('modified time'), auto_now= True)

    class Meta:
        abstract = True # DON'T CREATE ANY TABLE NAMED BASEMODEL