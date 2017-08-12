#!/usr/bin/env python
import socket

import config_user


def test(server='127.0.0.1', port=12301):
    try:
        s = socket.socket()
        s.connect((server, port))
        print('OpenDKIM \033[32mOK\033[37m')
    except socket.error, e:
        print('OpenDKIM \033[31mKO\033[37m')
        print(e)
        print('Try: systemctl restart opendkim.service')


if __name__ == '__main__':
    test()
    print('=' * 80)
    test(config_user.BAD_IP)
