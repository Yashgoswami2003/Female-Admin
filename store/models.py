from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=200)
    date = models.CharField(max_length=100, default="October 2026")
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title