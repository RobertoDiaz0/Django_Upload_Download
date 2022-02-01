from django.db import models

# Create your models here.
class UploadModel(models.Model):
 
    title = models.CharField(max_length = 80)
    xls = models.FileField
 
    class Meta:
        ordering = ['title']
     
    def __str__(self):
        return f"{self.title}"