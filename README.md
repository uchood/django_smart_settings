# django_smart_settings
store and initialize from settings.py smart settings with ghrouping, types and descriptions
django >=1.7

# settings.py 

```
INSTALLED_APPS = (
    ..,
    'smart_settings',
    ...
)
```
Setting from DEFAULT_SMART_OPTIONS  will be copied to database  at start server. If they already exist will nothing to do.
```
DEFAULT_SMART_OPTIONS = {
    'global': [
            {
                'key': 'int_1',
                'type_of_value': u'INT',
                'value': 0,
                'description': u'Description string int 1',
            },
            {
                'key': 'string_1',
                'type_of_value': u'STRING',
                'value': u'string one',
                'description': u'Description string 1',
            },
            {
                'key': 'float_1',
                'type_of_value': u'FLOAT',
                'value': 0.0,
                'description': u'Description float 1',
            },
        ]
    }
```
