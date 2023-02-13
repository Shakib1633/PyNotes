# To make the notes app modifiable in the admin,
# we need to tell the admin that Notes objects have an admin interface. To do this, open the admin.py file, and edit it to look like this:

from django.contrib import admin
from .models import Notes

# Register your models here.
admin.site.register(Notes)