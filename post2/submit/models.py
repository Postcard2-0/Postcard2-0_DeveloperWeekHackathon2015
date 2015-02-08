from django.db import models

# Create your models here.
# AEttinger 7.2.15 - I created two classes for the database, one for sender and one for recipient.

# Recipient class:
class recipient(models.Model):
	recipient_name = models.CharField(max_length=200)
	recipient_street_text = models.CharField(max_length=200)
	recipient_street_nr = models.CharField(max_length=50)
	recipient_city_text = models.CharField(max_length=200)
	recipient_city_zip = models.CharField(max_length=50)
	recipient_country_text = models.CharField(max_length=200)

# Sender class:
class sender(models.Model):
	sender_name = models.CharField(max_length=200)
	sender_memo = models.CharField(max_length=500)
	sender_photo = models.ImageField(upload_to='photos')
	sender_movie = models.URLField(max_length=200)

