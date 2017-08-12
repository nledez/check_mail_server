#!/usr/bin/env python
import imaplib
import socket

import config_user


def test(username=config_user.USER, password=config_user.PASSWORD):
    try:
        imap = imaplib.IMAP4('localhost', 143)
        imap.login(username, password)
        print('Cyrus \033[32mOK\033[37m')
    except socket.error, e:
        print('Cyrus \033[31mKO\033[37m')
        print(e)
        print('Try: systemctl restart cyrus-imapd.service')
    except imaplib.IMAP4.error, e:
        print('Cyrus \033[31mKO\033[37m')
        print(e)
        print('Try: systemctl restart cyrus-imapd.service')


if __name__ == '__main__':
    test()
    print('=' * 80)
    test(password=config_user.BAD_PASSWORD)
