from django.db import models


class Profile(models.Model):
    face_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    address = models.TextField()
    phone = models.IntegerField(null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    image = models.ImageField(upload_to="images/", null=True, blank=True)

    def __str__(self) -> str:
        return super().name
