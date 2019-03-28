#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import subprocess

from common import show_ok, show_ko


def test(test_mode=False):
    command = 'nslcd --check'
    process_exec = subprocess.Popen(command,
                                    shell=True,
                                    stdout=subprocess.PIPE,
                                    stderr=subprocess.PIPE)
    process_exec.wait()
    if test_mode:
        returncode = 1
    else:
        returncode = process_exec.returncode

    if returncode == 0:
        show_ok('nslcd')
    else:
        show_ko('nslcd', 'Try: systemctl restart nslcd.service')


if __name__ == '__main__':
    test()
    print('=' * 80)
    test(test_mode=True)
