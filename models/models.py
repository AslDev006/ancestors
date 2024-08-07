import uuid
from cloudinary.models import CloudinaryField
from django.db import models

male = 'Male'
female = 'Female'
parent = 'Parent'
none = 'None'
child = 'Child'
image = 'Image'
video = 'Video'
class Person(models.Model):
    class GENDER(models.TextChoices):
        male = male
        female = female
        none = none
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=255)
    second_name = models.CharField(max_length=255, null=True, blank=True)
    third_name = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    notfound_birth = models.BooleanField(default=False)
    date_of_death = models.DateField(null=True, blank=True)
    notfound_death = models.BooleanField(default=False)
    image = CloudinaryField("person_images", null=True, default=None, blank=True)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    gender = models.CharField(max_length=100, choices=GENDER, default=none)

    def __str__(self):
        return f"{self.first_name}  {self.second_name}   {self.third_name}"

    @property
    def full_name(self):
        return f"{self.first_name} {self.second_name} {self.third_name}"

class Roles(models.Model):
    class ROLES(models.TextChoices):
        parent = parent
        child = child
    role = models.CharField(max_length=100, choices=ROLES)
    person = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='roles')
    family = models.ForeignKey('Family', on_delete=models.CASCADE, related_name='partner')
    def __str__(self):
        return f"{self.person.__str__()} {self.role}"


class Family(models.Model):
    title = models.CharField(max_length=255)
    def __str__(self):
        return self.title


class Family_Media(models.Model):
    class MEDIA_TYPES(models.TextChoices):
        image = image
        video = video
    title = models.CharField(max_length=255)
    description = models.TextField()
    partners = models.ManyToManyField(Person, related_name='family_media')
    media_type = models.CharField(max_length=20, choices=MEDIA_TYPES)
    image = CloudinaryField("family_media/images/", null=True, blank=True)
    video = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.title


class PersonalImages(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='images')
    image = CloudinaryField("pers_image/images/", null=True, blank=True)

    def __str__(self):
        return f"image for {self.person}"