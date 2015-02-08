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
	def __str__(self):
		return self.recipient_name

# Sender class:
class sender(models.Model):
	sender_name = models.CharField(max_length=200)
	sender_memo = models.CharField(max_length=500)
	sender_photo = models.ImageField(upload_to='photos')
	sender_movie = models.FileField(upload_to='movies') 

# AEttinger 7.2.15 5:30 pm - changed from URL to file field

