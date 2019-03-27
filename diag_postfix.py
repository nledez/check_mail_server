#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import socket
import smtplib

import config_user

from common import show_ok, show_ko


def test(username=config_user.USER,
         password=config_user.PASSWORD,
         server='localhost',
         port=587):
    try:
        smtp = smtplib.SMTP()
        smtp.connect(server, port)
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()
        smtp.login(username, password)
        show_ok('Postfix')
    except smtplib.SMTPResponseException, e:
        show_ko('Postfix', 'Try: systemctl restart postfix.service', e)
    except smtplib.SMTPAuthenticationError, e:
        show_ko('Postfix', 'Try: systemctl restart postfix.service', e)
    except socket.error, e:
        show_ko('Postfix', 'Try: systemctl restart postfix.service', e)


if __name__ == '__main__':
    test()
    print('=' * 80)
    test(password=config_user.BAD_PASSWORD)
    print('=' * 80)
    test(port=588)
