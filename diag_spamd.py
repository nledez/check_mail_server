#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import spamc

import config_user

from common import show_ok, show_ko


def test(server='127.0.0.1'):
    try:
        client = spamc.SpamC(server)
        client.ping()
        show_ok('SpamD')
    except spamc.exceptions.SpamCError, e:
        show_ko('SpamD', 'Try: systemctl restart spamassassin.service', e)


if __name__ == '__main__':
    test()
    print('=' * 80)
    test(config_user.BAD_IP)
