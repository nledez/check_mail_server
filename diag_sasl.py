#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import subprocess

import config_user

from common import show_ok, show_ko


def test(username=config_user.USER, password=config_user.PASSWORD,
         mux='/var/run/saslauthd/mux'):
    cmd = '/usr/sbin/testsaslauthd -u {} -p {} -f {}'.format(username,
                                                             password,
                                                             mux)
    p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE,
                         close_fds=True)
    p.wait()
    if p.returncode == 0:
        show_ok('SASL')
    else:
        hint = []
        error = []
        error.append('Failed with mux: {}'.format(mux))
        for line in p.stdout.readlines():
            error.append(line)
        if mux == '/var/run/saslauthd/mux':
            hint.append('Try: ln -s /var/spool/postfix/var/run/saslauthd /var/run/saslauthd')
        hint.append('Try: systemctl restart saslauthd.service')
        show_ko('SASL',
                '\n'.join(hint),
                '\n'.join(error))


if __name__ == '__main__':
    test()
    print('=' * 80)
    test(password=config_user.BAD_PASSWORD, mux='/var/run/saslauthd/mux')
