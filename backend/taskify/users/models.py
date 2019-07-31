from django.db import models
from django.contrib.auth.models import User

def upload_image(instance, filename):
    return f"{instance.user.username}/{filename}"

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    fullname = models.CharField(max_length=40, blank=False, null=False)
    image = models.ImageField(default='default.jpg', upload_to=upload_image)

    def __str__(self):
        return f"{self.user.username}'s Profile"