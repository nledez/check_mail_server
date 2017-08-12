#!/usr/bin/env python
import spamc

import config_user


def test(server='127.0.0.1'):
    try:
        client = spamc.SpamC(server)
        client.ping()
        print('SpamD \033[32mOK\033[37m')
    except spamc.exceptions.SpamCError, e:
        print('SpamD \033[31mKO\033[37m')
        print(e)
        print('Try: systemctl restart spamassassin.service')


if __name__ == '__main__':
    test()
    print('=' * 80)
    test(config_user.BAD_IP)
