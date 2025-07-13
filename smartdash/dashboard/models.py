from django.db import models

class Quote(models.Model):
    author = models.CharField(max_length=100)
    content = models.TextField()
    category = models.CharField(max_length=50, blank=True, null=True) 
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.content[:50]}... — {self.author}"
