#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import MySQLdb
import sys

import config_user
from common import show_ok, show_ko


def test(db_user=config_user.DB_USER, db_pass=config_user.DB_PASS,
         db_name=config_user.DB_NAME, db_query=config_user.DB_QUERY):
    try:
        db = MySQLdb.connect('localhost', db_user, db_pass, db_name)
        cur = db.cursor()
        cur.execute(db_query)
        cur.rowcount
        show_ok('MysqlAliases')
    except:
        e = sys.exc_info()
        show_ko('MysqlAliases', 'Try: systemctl restart mysql.service', e)


if __name__ == '__main__':
    test()
    print('=' * 80)
    test('0', '0', '0', '0')
