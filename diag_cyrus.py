#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import imaplib
import socket

import config_user

from common import show_ok, show_ko


def test(username=config_user.USER, password=config_user.PASSWORD):
    try:
        imap = imaplib.IMAP4('localhost', 143)
        imap.login(username, password)
        show_ok('Cyrus')
    except socket.error, e:
        show_ko('Cyrus', 'Try: systemctl restart cyrus-imapd.service', e)
    except imaplib.IMAP4.error, e:
        show_ko('Cyrus', 'Try: systemctl restart cyrus-imapd.service', e)


if __name__ == '__main__':
    test()
    print('=' * 80)
    test(password=config_user.BAD_PASSWORD)
