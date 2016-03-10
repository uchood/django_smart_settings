from django.contrib import admin

# Register your models here.
from smart_settings.models import ConfigOfServer


class ConfigOfServerAdmin(admin.ModelAdmin):
    list_display = ('group', 'key', 'value', 'type_of_value', 'description', 'changed_on')
    list_editable = ['value']
    list_filter = ['group']
    list_per_page = 1000
    list_max_show_all = 50000

admin.site.register(ConfigOfServer, ConfigOfServerAdmin)