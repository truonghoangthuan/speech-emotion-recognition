from django.db import models


# Create your models here.
class AudioUploadFile(models.Model):
    audioFile = models.FileField(upload_to='audio_files/')
    textOutput = models.CharField(max_length=255, blank=True, null=True)
