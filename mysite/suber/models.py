from django.db import models

# Create your models here.
# Recipient class:
class Suber(models.Model):
        name = models.CharField(max_length=200)
        street_text = models.CharField(max_length=200)
        street_nr = models.CharField(max_length=50)
        city_text = models.CharField(max_length=200)
        city_zip = models.CharField(max_length=50)
        country_text = models.CharField(max_length=200)
        def __str__(self):
            return self.name

# Sender class:
# class Sender(models.Model):
        # sender_name = models.CharField(max_length=200)
        # sender_memo = models.CharField(max_length=500)
        # sender_photo = models.ImageField(upload_to='photos')
        # sender_movie = models.FileField(upload_to='movies') # AEttinger 7.2.15 5:30 pm - changed from URL to file field
