from django.db import models
from django.utils.timezone import now
from django.urls import reverse
from datetime import datetime
from taggit.managers import TaggableManager

# Create your models here.

class ArticlePost(models.Model):
    author = models.ForeignKey('auth.User',on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    create_date = models.DateTimeField(default=now)
    publish_date = models.DateField(blank=True,null=True)
    featured_image = models.ImageField(upload_to='featured_images/%Y/%m/',blank=True)
    tags = TaggableManager()

    def publish(self):
        rn = now()
        self.publish_date = rn
        self.save()

    def approve_comments(self):
        return self.comments.filter(approved_comment=True)

    def get_absolute_url(self):
        return reverse("articles:post_detail",kwargs={'pk':self.pk})

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey('articles.ArticlePost',related_name='comments',on_delete=models.CASCADE)
    author = models.CharField(max_length=36)
    text = models.TextField()
    create_date = models.DateTimeField(default=now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()
    
    def get_absolute_url(self):
        return reverse("articles:post_detail",kwargs={'pk':self.pk})

    def __str__(self):
        return self.text