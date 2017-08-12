#!/usr/bin/env python
import os.path


def test(socket_path='/var/spool/postfix/clamav/clamav-milter.ctl'):
    if os.path.exists(socket_path):
        print('Clamav-milter \033[32mOK\033[37m')
    else:
        print('Clamav-milter \033[31mKO\033[37m')
        print('Try: systemctl restart clamav-milter.service')


if __name__ == '__main__':
    test()
    print('=' * 80)
    test('/var/spool/postfix/clamav/clamav-milter.ctl.not')
