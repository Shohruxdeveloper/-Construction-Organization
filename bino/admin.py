from django.contrib import admin

from .models import Territory, Organization, Building


admin.site.register(Territory)
admin.site.register(Organization)
admin.site.register(Building)
