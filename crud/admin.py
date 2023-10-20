from django.contrib import admin
from .models import ClientInfo

# Register your models here.
admin.site.register(ClientInfo)

admin.site.site_header = 'digi brains academy '
admin.site.index_title = 'Nag'
