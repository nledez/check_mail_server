#!/usr/bin/env python
import MySQLdb
import sys

import config_user


def test(db_user=config_user.DB_USER, db_pass=config_user.DB_PASS,
         db_name=config_user.DB_NAME, db_query=config_user.DB_QUERY):
    try:
        db = MySQLdb.connect('localhost', db_user, db_pass, db_name)
        cur = db.cursor()
        cur.execute(db_query)
        cur.rowcount
        print('MysqlAliases \033[32mOK\033[37m')
    except:
        e = sys.exc_info()
        print('MysqlAliases \033[31mKO\033[37m')
        print(e)
        print('Try: systemctl restart mysql.service')


if __name__ == '__main__':
    test()
    print('=' * 80)
    test('0', '0', '0', '0')
