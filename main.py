#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import diag_ldap
import diag_sasl
import diag_cyrus
import diag_postfix
import diag_spamd
import diag_opendkim
import diag_opendmarc
import diag_clamd
import diag_milterclam_spamass
import diag_milterclam_clamav
import diag_mysql_aliases

if __name__ == '__main__':
    diag_ldap.test()
    diag_sasl.test(mux='/var/spool/postfix/var/run/saslauthd/mux')
    diag_sasl.test()
    diag_cyrus.test()
    diag_postfix.test()
    diag_spamd.test()
    diag_opendkim.test()
    diag_opendmarc.test()
    diag_clamd.test()
    diag_milterclam_spamass.test()
    diag_milterclam_clamav.test()
    diag_mysql_aliases.test()
