#check if enough space

req=$(du -s /var/log| cut -f1)

disp=$(df $(pwd)|tail -1 | awk '{print $2}')

if [ $(($disp - $req)) -gt 0 ]; then

	echo "espace suffisant, copie des logs localement."

	tar cvf /var/log/logs-${HOSTNAME}-$(date +%s).tar   /var/log

else
      echo "espace insuffisant, affichage de la liste des logs"
      find /var/log -print
fi
exit 0



