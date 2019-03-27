#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import os.path

from common import show_ok, show_ko


def test(socket_path='/var/spool/postfix/spamass/spamass.sock'):
    if os.path.exists(socket_path):
        show_ok('Spamassassin-milter')
    else:
        show_ko('Spamassassin-milter',
                'Try: systemctl restart spamass-milter.service')


if __name__ == '__main__':
    test()
    print('=' * 80)
    test('/var/spool/postfix/spamass/spamass.sock.not')
