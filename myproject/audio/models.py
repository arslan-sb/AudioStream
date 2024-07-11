from django.db import models


class AudioFile(models.Model):
    title = models.CharField(max_length=200)
    file = models.FileField(upload_to='audio/')

    def __str__(self):
        return self.title
