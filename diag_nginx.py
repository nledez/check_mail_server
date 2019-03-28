#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import requests

from common import show_ok, show_ko


def test(server='127.0.0.1', port='80'):
    try:
        r = requests.get('http://{}:{}/'.format(server, port))
        if r.status_code == 200:
            show_ok('Nginx')
        else:
            show_ko('Nginx', 'Try: systemctl restart nginx.service')
    except requests.exceptions.ConnectionError, e:
            show_ko('Nginx', 'Try: systemctl restart nginx.service', e)


if __name__ == '__main__':
    test()
    print('=' * 80)
    test(server='127.0.0.2', port=82)
