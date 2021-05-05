from django.contrib.auth.models import User
from django.db import models
import os
from PIL import Image
from .validators import validate_image_file_extension
from .storage import OverwriteFile


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_private = models.BooleanField(default=0)
    is_online = models.BooleanField(default=0)
    image = models.ImageField(default='profile_pics/default.jpg', upload_to='profile_pics', blank=True, storage=OverwriteFile(), validators=[validate_image_file_extension])

    def __str__(self):
        return f'{self.user.username}'

    def save(self, *args, **kwargs):
        super().save()
        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
        img = img.convert('RGB')
        if 'default.jpg' not in self.image.name:
            os.remove(self.image.path)
            self.image.name = 'profile_pics/' + str(self.user_id) + "." + self.image.name.split(".", 2)[1]
        img.save(self.image.path, "JPEG")