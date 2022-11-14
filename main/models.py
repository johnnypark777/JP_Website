from django.db import models
import os

class File(models.Model):
    file = models.FileField(upload_to='files/')
    def __str__(self):
        return os.path.split(self.file.name)[1] 


    def delete(self, *args, **kwargs):
        self.file.delete()
        super().delete(*args, **kwargs)

