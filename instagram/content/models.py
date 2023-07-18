from django.db import models
from lib.common_models import BaseModel
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
from location.models import  Location

User = get_user_model()

class Post(BaseModel):
    caption = models.TextField(_('caption'), blank= True)
    user = models.ForeignKey(User, verbose_name='user', related_name='posts', on_delete=models.CASCADE)
    location = models.ForeignKey(Location, verbose_name='location', related_name='posts', on_delete=models.CASCADE)
    
    def __str__(self):
        return "{} ({})".format(self.user.username, self.id)
    
    class Meta:
        verbose_name = _("post")
        verbose_name_plural = _("posts")
#############################################
class PostMedia(BaseModel):
    IMAGE = 1
    VIDEO = 2

    TYPE_CHIOSES = (
        (IMAGE, _('Image')),
        (VIDEO, _('Video')),
    )
    media_type = models.PositiveSmallIntegerField(_('media type'), choices=TYPE_CHIOSES, default=IMAGE)
    post = models.ForeignKey(Post, verbose_name='post', related_name='media', on_delete=models.CASCADE)
    media_file = models.FileField(_('media file'), upload_to='content/media/')

    def __str__(self):
        return "{} {}".format(str(self.post), self.get_media_type_display()) #show the translation of media_type

    class Meta:
        verbose_name = _("media")
        verbose_name_plural = _("medias")
#############################################
class Tag (BaseModel):
    title = models.TextField(_('title'), max_length=32)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = _("tag")
        verbose_name_plural = _("tags")
#############################################
class PostTag(BaseModel):
    post = models.ForeignKey(Post, verbose_name='post', related_name='hashtag', on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, verbose_name='tag', related_name='posts', on_delete=models.CASCADE)

    def __str__(self):
        return "{} {}".format(str(self.post), str(self.tag)) #show the translation of media_type
    
    class Meta:
        verbose_name = _("post tagged")
        verbose_name_plural = _("posts tagged")
#############################################
class TaggedUser(BaseModel):
    user = models.ForeignKey(User, verbose_name='user', related_name='tagged_posts', on_delete=models.CASCADE)
    post = models.ForeignKey(Post, verbose_name='post', related_name='tagged_users', on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name = _("tagged user")
        verbose_name_plural = _("tagged users")