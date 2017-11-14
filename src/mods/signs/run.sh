find /var/tmp /tmp/ -type f -print -exec md5sum {} \;  2>/dev/null
exit 0
