#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import socket

import config_user

from common import show_ok, show_ko


def test(server='127.0.0.1', port=12301):
    try:
        s = socket.socket()
        s.connect((server, port))
        show_ok('OpenDKIM')
    except socket.error, e:
        show_ko('OpenDKIM', 'Try: systemctl restart opendkim.service', e)


if __name__ == '__main__':
    test()
    print('=' * 80)
    test(config_user.BAD_IP)
