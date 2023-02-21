import os
from django.core.exceptions import ValidationError
from django.db import models
from multiselectfield import MultiSelectField
from applications.alumniprofile.models import Profile


# Create your models here.
class Constants:
    TYPE = (
        ('S', 'Self'),
        ('C', 'Campaign')
    )

def upload_photo(instance, filename):
    name, extension = os.path.splitext(filename)
    return 'Profile_Pictures/' + str(instance.blog_id) + ".jpg"

class Campaign(models.Model):
    campaign_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=250)
    date_started = models.DateTimeField(auto_now=True)
    date_ended = models.DateTimeField(blank=True)
    thumbnail = models.ImageField(null=True, upload_to=upload_photo)
    description = models.TextField(blank=False, max_length=2000)
    author = models.CharField(max_length=250)

    def __str__(self):
        return self.name

class Blog(models.Model):
    blog_id = models.AutoField(primary_key=True)
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    title = models.CharField(max_length=250, blank=False)

    thumbnail = models.ImageField(null=True, upload_to=upload_photo)
    # TODO: Apply a limit of 5 on the number of tags
    tags = models.ManyToManyField('Tags')
    content = models.TextField(max_length=5000, blank=False)
    date_added = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    upvotes = models.IntegerField(default=0)
    
    blog_type = models.CharField(choices=Constants.TYPE, max_length=15,default='S')
    campaign_id = models.ForeignKey(Campaign, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title

class Replies(models.Model):
    blog_id = models.ForeignKey(Blog, on_delete=models.CASCADE)
    reply_id = models.AutoField(primary_key=True)
    content = models.CharField(blank=False, max_length=500)

    time_stamp = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    parent_reply_id = models.ForeignKey("self", on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name_plural = "Replies"

class Tags(models.Model):
    tag_id = models.AutoField(primary_key=True)
    tag_name = models.CharField(max_length=50, null=False, blank=False)
    on_home_page = models.BooleanField(default=False)
    date_added = models.DateTimeField(auto_now=True)
    last_modified = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Tags"

    def __str__(self):
        return self.tag_name