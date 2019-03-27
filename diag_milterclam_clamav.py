#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import os.path

from common import show_ok, show_ko


def test(socket_path='/var/spool/postfix/clamav/clamav-milter.ctl'):
    if os.path.exists(socket_path):
        show_ok('Clamav-milter')
    else:
        show_ko('Clamav-milter',
                'Try: systemctl restart clamav-milter.service')


if __name__ == '__main__':
    test()
    print('=' * 80)
    test('/var/spool/postfix/clamav/clamav-milter.ctl.not')
