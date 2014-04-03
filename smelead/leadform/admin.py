from django.contrib import admin
from leadform.models import leadform

class leadformadmin(admin.ModelAdmin):
    list_display = ('name', 'organisation', 'city', 'emailId', 'contactno')

admin.site.register(leadform, leadformadmin)
