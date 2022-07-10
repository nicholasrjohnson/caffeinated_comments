import uuid
from django.db import models
from django.conf import settings
from django.utils import timezone

class Author(models.Model):
    uuid = models.UUIDField(unique=True, editable=False, default=uuid.uuid4)
    name = models.CharField(max_length=200)
    email = models.EmailField(null=True)

class Comment(models.Model):
    body = models.CharField(max_length=500)
    pub_date = models.DateTimeField('Comment Date', default=timezone.now)
    edited_date = models.DateTimeField('Edited Date', default=timezone.now)
    up_vote = models.IntegerField(default=0)
    down_vote = models.IntegerField(default=0)
    post_slug = models.SlugField()
    replied_to = models.ForeignKey('self', on_delete=models.CASCADE, null=True)
    postid = models.IntegerField(default=0)
    
    created_by = models.ForeignKey(
        Author,
        on_delete=models.PROTECT,
        related_name='comments'
    )