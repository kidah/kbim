from django.contrib import admin
from .models import AutodeskAPIs, AutodeskTokens
# Register your models here.

admin.site.register(AutodeskAPIs)
admin.site.register(AutodeskTokens)
