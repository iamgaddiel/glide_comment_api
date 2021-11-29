from django.db import models
from django.utils.timezone import now
from uuid import uuid4


class Comment(models.Model):
    id = models.UUIDField(unique=True, editable=False, default=uuid4, primary_key=True)
    blog = models.CharField(max_length=300, default="")
    name = models.CharField(max_length=30)
    comment = models.TextField()
    likes = models.IntegerField(default=0)
    timestamp = models.DateTimeField(auto_now_add=now)
    
    def __str__(self) -> str:
        return "{0} | {1} | {2}".format(self.blog, self.name, self.timestamp)
    
    class Meta:
        ordering = ['-timestamp']

class Like(models.Model):
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    liker = models.CharField(max_length=32)

    def __str__(self) -> str:
        return "{0} | {1} | {2}".format(
            self.comment.name,
            self.comment.blog,
            self.comment.id
        )
