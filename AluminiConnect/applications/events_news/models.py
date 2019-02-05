from django.db import models
import datetime, os
from django.utils import timezone
from ckeditor_uploader.fields import RichTextUploadingField


def upload_event_photo(instance, filename):
    name, extension = os.path.splitext(filename)
    return "Events/" + str(instance.title) + extension

class Event(models.Model):
    event_id = models.AutoField(primary_key = True)
    title = models.TextField(max_length=255, null=False)
    start_date = models.DateTimeField(default = datetime.datetime.now() + datetime.timedelta(hours=24))
    end_date = models.DateTimeField(default = datetime.datetime.now() + datetime.timedelta(hours=48))
    by = models.CharField(max_length = 255, null=True)
    picture = models.ImageField(null = True, blank = True, upload_to = upload_event_photo)
    location = models.CharField(max_length = 100, null = True)
    address = RichTextUploadingField()
    description = RichTextUploadingField()

    def __str__(self):
        return self.title

    def is_completed(self):
        return (timezone.now() > self.end_date)