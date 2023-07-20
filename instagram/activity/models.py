from django.db import models
from lib.common_models import BaseModel
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
from content.models import Post

User = get_user_model()

class Comment(BaseModel): 
    caption = models.TextField(_('caption'), max_length= 256)
    user = models.ForeignKey(User, verbose_name='user', related_name='comments', on_delete=models.CASCADE)
    post = models.ForeignKey(Post, verbose_name='post', related_name='comments', on_delete=models.CASCADE)
    reply_to = models.ForeignKey('self', related_name='replaies', on_delete=models.CASCADE)

    class Meta:
        verbose_name = _("comment")
        verbose_name_plural = _("comments")

    def __str__(self):
        return self.caption
#############################################
class Like(BaseModel):
    user = models.ForeignKey(User, verbose_name='user', related_name='likes', on_delete=models.CASCADE)
    post = models.ForeignKey(Post, verbose_name='post', related_name='likes', on_delete=models.CASCADE)

    class Meta:
        verbose_name = _("like")
        verbose_name_plural = _("likes")

    def __str__(self):
        return "{} >> {}".format(self.user.username, self.post.id)