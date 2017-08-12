# Why this

I have my own mail server. I configure many things to avoid, spam, blacklisting and other stuff.

But sometimes a component stop to work normally. And it's always when I have no time to do fix this.

And my server is used for many sites for auth, monitoring, etc. It's also used by my family.

So, I need a way to found witch part need to be fixed. It's why you have this :)

# Install

After `git clone`, you can do this:

```
apt-get install -y libldap2-dev libsasl2-dev libmysqlclient-dev
virtualenv venv
./venv/bin/pip install -r requirements.txt
cp config_user.py-sample config_user.py
vi config_user.py  # Update with your informations
```

# Use it

Main script launch each diag to show you a summary.

```
# ./venv/bin/python main.py
LDAP OK
SASL OK
SASL OK
Cyrus OK
Postfix OK
SpamD OK
OpenDKIM OK
OpenDMARC OK
ClamavDeamon OK
Spamassassin-milter OK
Clamav-milter OK
MysqlAliases OK
```

# Check if it works

You can check if each diag is working.

```
# ./venv/bin/python diag_clamd.py
# ./venv/bin/python diag_cyrus.py
# ./venv/bin/python diag_ldap.py
# ./venv/bin/python diag_milterclam_clamav.py
# ./venv/bin/python diag_milterclam_spamass.py
# ./venv/bin/python diag_mysql_aliases.py
# ./venv/bin/python diag_opendkim.py
# ./venv/bin/python diag_opendmarc.py
# ./venv/bin/python diag_postfix.py
# ./venv/bin/python diag_sasl.py
# ./venv/bin/python diag_spamd.py
```

Each diag script return things look like this:

```
ClamavDeamon OK
================================================================================
ClamavDeamon KO
Error 2 connecting /var/run/clamav/clamd.ctl2. No such file or directory.
Try: systemctl restart clamav-daemon.socket
```

The first part is the real test. The second part use fake information to force a failure.
