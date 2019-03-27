#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import socket

import config_user

from common import show_ok, show_ko


def test(server='127.0.0.1', port=12345):
    try:
        s = socket.socket()
        s.connect((server, port))
        show_ok('OpenDMARC')
    except socket.error, e:
        show_ko('OpenDMARC', 'Try: systemctl restart opendmarc.service', e)


if __name__ == '__main__':
    test()
    print('=' * 80)
    test(config_user.BAD_IP)
