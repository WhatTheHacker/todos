from django.db import models

# Create your models here.
class Task(models.Model):
    task = models.CharField(max_length=255)
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.task
    

class UserProfile(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE, primary_key=True)
    profile_picture = models.ImageField(upload_to='users/profile_pictures', blank=True, null=True)
    cover_photo = models.ImageField()