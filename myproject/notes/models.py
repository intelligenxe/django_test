

from django.db import models

class Note(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    # image = models.ImageField(upload_to='images/', default='images/default.png')  # Image saved to /media/images/
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title

