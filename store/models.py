from django.db import models

class Vlog(models.Model):
    title = models.CharField(max_length=200)
    video_url = models.URLField(help_text="Paste YouTube or Video Link here")
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title