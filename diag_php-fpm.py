#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import subprocess

from common import show_ok, show_ko

DEBUG = False


def test(base='/var/www/www', script='/ping.php', server='127.0.0.1:9000'):
    command = 'SCRIPT_NAME={script} SCRIPT_FILENAME={base}{script} REQUEST_METHOD=GET cgi-fcgi -bind -connect {server}'.format(base=base, script=script, server=server)
    if DEBUG:
        print(command)
    process_exec = subprocess.Popen(command,
                                    shell=True,
                                    stdout=subprocess.PIPE,
                                    stderr=subprocess.PIPE)
    process_exec.wait()
    returncode = process_exec.returncode
    if DEBUG:
        print(returncode)

    if returncode == 0:
        show_ok('php5-fpm')
    else:
        error = '\n'.join(process_exec.stderr.readlines())
        show_ko('php5-fpm', 'Try: systemctl restart php5-fpm.service', error)


if __name__ == '__main__':
    test()
    print('=' * 80)
    test(server='127.0.0.1:9001')
