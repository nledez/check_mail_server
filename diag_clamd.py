#!/usr/bin/env python
import clamd


def test(socket='/var/run/clamav/clamd.ctl'):
    try:
        client = clamd.ClamdUnixSocket(socket)
        client.ping()
        print('ClamavDeamon \033[32mOK\033[37m')
    except clamd.ConnectionError, e:
        print('ClamavDeamon \033[31mKO\033[37m')
        print(e)
        print('Try: systemctl restart clamav-daemon.socket')


if __name__ == '__main__':
    test()
    print('=' * 80)
    test('/var/run/clamav/clamd.ctl2')
