# -*- coding: utf-8 -*-
__author__ = 'uchood'

import logging

logger = logging.getLogger(__name__)

from django.conf import settings

from smart_settings.models import ConfigOfServer



def check_exist_key_in_options(key):
    result = False
    try:
        query = ConfigOfServer.objects.all().filter(key=key)
        count = query.count()
        if count > 0:
            result = True
    except ConfigOfServer.DoesNotExist as e:
        pass
    return result


def add_key_to_options(**kwargs):
    result = False
    query = {
        'group': '',
        'key': '',
        'value': '',
        'type_of_value': ConfigOfServer.TYPE_OPTIONS[u'STRING'],
        'description': ''
    }
    if 'group' in kwargs:
        query['group'] = kwargs['group'].strip()
    if 'key' in kwargs:
        query['key'] = kwargs['key'].strip()
    if 'value' in kwargs:
        query['value'] = '{}'.format(kwargs['value'])
    if 'type_of_value' in kwargs:
        query['type_of_value'] = ConfigOfServer.TYPE_OPTIONS[kwargs['type_of_value']]
    if 'description' in kwargs:
        query['description'] = kwargs['description']
    try:
        exist_already = check_exist_key_in_options(key=query['key'])
        if not exist_already:
            new_option, created = ConfigOfServer.objects.get_or_create(**query)
            new_option.save()
            result = new_option.id
    except Exception as e:
        print e
        logger.exception(u"add_key_to_options {}".format(e))
    return result


def check_and_add_keys_to_options(options):
    example_options = {
        'time_limits_on_off': [
            {
                'key': 'auto_off_interval_in_min',
                'type_of_value': u'INT',
                'value': 0,
                'description': u'Время в минутах, через которое автоматически будет отдана команда на выключение.'
                               u' Если 0 - автоматическое отключения не производится.',
            },
            {
                'key': 'interval_blocking_in_off_state_in_min',
                'type_of_value': u'INT',
                'value': 0,
                'description': u'Время в минутах после отключения, в течении которого игнорируются команды '
                               u'на включение. Если 0 - нет блокировок.',
            },
        ]
    }
    for group_name, group_value in options.iteritems():
        for x in group_value:
            kwarg = x
            kwarg['group'] = group_name
            res = add_key_to_options(**kwarg)
    return


def set_default_options():
    if hasattr(settings, 'DEFAULT_SMART_OPTIONS'):
        check_and_add_keys_to_options(settings.DEFAULT_SMART_OPTIONS)



def prepare_option_to_dict(option):
    group = option.group
    if len(group) == 0:
        group = 'default'
    string_value = option.value
    type_value = option.type_of_value
    value = None
    if type_value == ConfigOfServer.TYPE_OPTIONS[u'STRING']:
        value = string_value
    elif type_value == ConfigOfServer.TYPE_OPTIONS[u'FLOAT']:
        try:
            value = float(string_value)
        except ValueError:
            value = 0.0
    elif type_value == ConfigOfServer.TYPE_OPTIONS[u'INT']:
        try:
            value = int(string_value)
        except ValueError:
            value = 0
    else:
        logger.error("error read_options_from_db_by_group")
        print "ERROR"

    dic_line = {
        'group': group,
        'key': option.key,
        'value': value,
        'changed_on': option.changed_on
        }
    return dic_line


def read_options_from_db_by_group(time=None):
    result_dict = {}
    if time:
        selected_options = ConfigOfServer.objects.all().filter(changed_on_gt=time)
    else:
        selected_options = ConfigOfServer.objects.all()
    for option in selected_options:
        dic_line = prepare_option_to_dict(option)
        group = option.group
        if len(group) == 0:
            group = 'default'
        result_dict[group].append(dic_line)

    return result_dict
