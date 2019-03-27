#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import clamd

from common import show_ok, show_ko


def test(socket='/var/run/clamav/clamd.ctl'):
    try:
        client = clamd.ClamdUnixSocket(socket)
        client.ping()
        show_ok('ClamavDeamon')
    except clamd.ConnectionError, e:
        show_ko('ClamavDeamon',
                'Try: systemctl restart clamav-daemon.socket',
                e)


if __name__ == '__main__':
    test()
    print('=' * 80)
    test('/var/run/clamav/clamd.ctl2')
