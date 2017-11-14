for u in $(getent passwd | cut -d":" -f1); do echo "$u crontab:"; crontab -u $u -l; done
exit 0
