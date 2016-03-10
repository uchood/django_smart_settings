from __future__ import unicode_literals

from django.apps import AppConfig



class SmartSettingsConfig(AppConfig):
    name = 'smart_settings'
    verbose_name = "Smart options store"

    def ready(self):
        print 'SmartSettingsConfig ready'
        from smart_settings.tools import set_default_options
        set_default_options()
        pass # startup code here


