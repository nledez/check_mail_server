#!/usr/bin/env python
import ldap

import config_user

SERVER = 'ldap://localhost'
LDAP = ldap.initialize(SERVER)
UID = config_user.LDAP_SEARCH.format(config_user.USER)
PASSWORD = config_user.PASSWORD


def test(uid=UID, password=PASSWORD):
    try:
        LDAP.bind_s(uid, password)
        print('LDAP \033[32mOK\033[37m')
    except ldap.INVALID_CREDENTIALS:
        print('LDAP \033[31mKO\033[37m')
        print('Your username or password is incorrect.')
    except ldap.LDAPError, e:
        print('LDAP \033[31mKO\033[37m')
        if type(e.message) == dict and 'desc' in e.message:
            print(e.message['desc'])
        else:
            print(e)
        print('Try: systemctl restart slapd.service')


if __name__ == '__main__':
    test()
    print('=' * 80)
    test(password=config_user.BAD_PASSWORD)
