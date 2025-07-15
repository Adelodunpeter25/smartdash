from django.db import models
from django.contrib.auth.models import User

class Quote(models.Model):
    author = models.CharField(max_length=100)
    content = models.TextField()
    category = models.CharField(max_length=50, blank=True, null=True) 
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.content[:50]}... — {self.author}"

class Utility(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    icon = models.CharField(max_length=50, default='⚙️')
    url_name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name
        
class UserPreference(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    utilities = models.ManyToManyField(Utility)
    theme = models.CharField(max_length=20, default='light')
    
    def __str__(self):
        return f"{self.user.username}'s preferences"
