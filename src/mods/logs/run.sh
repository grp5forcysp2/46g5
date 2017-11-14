#check if enough space

req=$(du -s /var/log| cut -f1)

disp=$(df $(pwd)|tail -1 | awk '{print $2}')

if [ $(($disp - $req)) -gt 0 ]
then
	echo "ok saving log here ..."
else
      echo "ah bah non"
fi
exit 0



