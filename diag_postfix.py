#!/usr/bin/env python
import socket
import smtplib

import config_user


def test(username=config_user.USER, password=config_user.PASSWORD):
    try:
        smtp = smtplib.SMTP()
        smtp.connect('localhost', 587)
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()
        smtp.login(username, password)
        print('Postfix \033[32mOK\033[37m')
    except smtplib.SMTPResponseException, e:
        print('Postfix \033[31mKO\033[37m')
        print(e)
        print('Try: systemctl restart postfix.service')
    except smtplib.SMTPAuthenticationError, e:
        print('Postfix \033[31mKO\033[37m')
        print(e)
        print('Try: systemctl restart postfix.service')
    except socket.error, e:
        print('Postfix \033[31mKO\033[37m')
        print(e)
        print('Try: systemctl restart postfix.service')


if __name__ == '__main__':
    test()
    print('=' * 80)
    test(password=config_user.BAD_PASSWORD)
