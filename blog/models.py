from django.utils import timezone
from django.db import models

# Create your models here.

class Blog1(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    body = models.TextField()

    def summary(self):
        return self.body[:100]
    
class Blog2(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    body = models.TextField()

    def summary(self):
        return self.body[:100]

class Blog3(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    body = models.TextField()

    def summary(self):
        return self.body[:100]

class Comment1(models.Model):
    post = models.ForeignKey('blog.Blog1', related_name="comments", on_delete=models.CASCADE)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(default = timezone.now)

    def __str__(self):
        return self.text


class Comment2(models.Model):
    post = models.ForeignKey('blog.Blog2', related_name="comments", on_delete=models.CASCADE)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(default = timezone.now)

    def __str__(self):
        return self.text


class Comment3(models.Model):
    post = models.ForeignKey('blog.Blog3', related_name="comments", on_delete=models.CASCADE)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(default = timezone.now) #현재 생성된 시간으로 자동 저장 (django.utils에서 가져와야합니다!)

    def __str__(self):
        return self.text