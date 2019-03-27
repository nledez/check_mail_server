#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import ntplib
from time import ctime

from common import show_ok, show_ko

DEBUG = False


def test(ntp_server='127.0.0.1'):
    try:
        c = ntplib.NTPClient()
        response = c.request(ntp_server)
        if DEBUG:
            print(ctime(response.tx_time))
        show_ok('Ntpd')
    except ntplib.NTPException, e:
        show_ko('Ntpd', 'Try: systemctl restart ntp.service', e)


if __name__ == '__main__':
    test()
    print('=' * 80)
    test(ntp_server='127.0.0.2')
