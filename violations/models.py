from django.db import models
from django.contrib.auth.models import User

class RoadViolation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()
    vehicle_image = models.ImageField(upload_to="violations_images",null=True,blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):

        return self.name


