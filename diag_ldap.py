#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import ldap

import config_user

from common import show_ok, show_ko


UID = config_user.LDAP_SEARCH.format(config_user.USER)
PASSWORD = config_user.PASSWORD


def test(uid=UID, password=PASSWORD, server='ldap://localhost'):
    try:
        LDAP = ldap.initialize(server)
        LDAP.bind_s(uid, password)
        show_ok('LDAP')
    except ldap.INVALID_CREDENTIALS:
        show_ko('LDAP', 'Your username or password is incorrect.')
    except ldap.LDAPError, e:
        if type(e.message) == dict and 'desc' in e.message:
            error = e.message['desc']
        else:
            error = e
        show_ko('LDAP', 'Try: systemctl restart slapd.service', error)


if __name__ == '__main__':
    test()
    print('=' * 80)
    test(password=config_user.BAD_PASSWORD)
    print('=' * 80)
    test(password=config_user.BAD_PASSWORD, server='127.0.0.2')
