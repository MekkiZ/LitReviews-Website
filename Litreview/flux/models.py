from django.core.validators import MinValueValidator, MaxValueValidator
from django.conf import settings
from django.db import models
from PIL import Image


class Ticket(models.Model):
    """
    A ticket for a user.
    """
    title = models.CharField(max_length=128)
    description = models.TextField(blank=True)
    time_created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null= True, blank=True )
    image = models.ImageField(null=True, blank=True, upload_to='images/', verbose_name='image')

    IMAGE_MAX_SIZE = (800, 800)

    def __str__(self):
        return self.title

    def resize_image(self):
        image = Image.open(self.image)
        image.thumbnail(self.IMAGE_MAX_SIZE)
        image.save(self.image.path)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.resize_image()


class Review(models.Model):
    ticket = models.ForeignKey(to=Ticket, on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField(
        # validates that rating must be between 0 and 5
        validators=[MinValueValidator(0), MaxValueValidator(5)])
    headline = models.CharField(max_length=128)
    body = models.CharField(max_length=8192, blank=True)
    user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    time_created = models.DateTimeField(auto_now_add=True)


class UserFollows(models.Model):
    # Your UserFollows model definition goes here
    user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='following')
    followed_user = models.ForeignKey(to=settings.AUTH_USER_MODEL,
                                      on_delete=models.CASCADE,
                                      related_name='followers_by')
    class Meta:
        # ensures we don't get multiple UserFollows instances
        # for unique user-user_followed pairs
        unique_together = ('user', 'followed_user', )

