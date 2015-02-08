from django.contrib import admin
from submit.models import recipient,sender

# Register your models here.

# AEttinger 7.2.15 - added these classes to be able to edit fields via admin web tool
class recipientAdmin(admin.ModelAdmin):
	fields = ['recipient_name','recipient_street_text','recipient_street_nr','recipient_city_text','recipient_city_zip','recipient_country_text' ]

class senderAdmin(admin.ModelAdmin):
	fields = ['sender_name','sender_memo','sender_photo','sender_movie']




# AEttinger 7.2.15 - Add registration for admin account. Register both recipient and sender tables.
admin.site.register(recipient, recipientAdmin)
admin.site.register(sender, senderAdmin)
