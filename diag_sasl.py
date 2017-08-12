#!/usr/bin/env python
import subprocess

import config_user


def test(username=config_user.USER, password=config_user.PASSWORD,
         mux='/var/run/saslauthd/mux'):
    cmd = '/usr/sbin/testsaslauthd -u {} -p {} -f {}'.format(username,
                                                             password,
                                                             mux)
    p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE,
                         close_fds=True)
    p.wait()
    if p.returncode == 0:
        print('SASL \033[32mOK\033[37m')
    else:
        print('SASL \033[31mKO\033[37m')
        print('Failed with mux: {}'.format(mux))
        print('\n'.join(p.stdout.readlines()))
        if mux == '/var/run/saslauthd/mux':
            print('Try: ln -s /var/spool/postfix/var/run/saslauthd \
                /var/run/saslauthd')
        print('Try: systemctl restart saslauthd.service')


if __name__ == '__main__':
    test()
    print('=' * 80)
    test(password=config_user.BAD_PASSWORD, mux='/var/run/saslauthd/mux')
