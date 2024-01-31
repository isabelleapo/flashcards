from django.db import models

# Create your models here.
class FlashCard(models.Model):
    side_a = models.TextField()
    side_b = models.TextField()