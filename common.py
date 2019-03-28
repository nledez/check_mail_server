#!/usr/bin/env python
# -*- encoding: utf-8 -*-


def show_ok(service):
    # print('{} \033[32mOK\033[37m'.format(service))
    print('✅ {}'.format(service))


def show_ko(service, hint, error=None):
    # print('{} \033[31mKO\033[37m'.format(service))
    print('🚨 {}'.format(service))
    if error:
        print(error)
    print(hint)
