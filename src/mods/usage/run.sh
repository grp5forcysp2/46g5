#!/bin/bash:
echo " ./46g5 mod1 mod2 ..."
echo " mod degine un module d'investigation."
echo " les modules disponibles se trouvnt dans le repertoire mods."
echo " ils sont conituté d'un repertoire du nom du module contenant:"
echo " un script shell"
echo " un script powershell"
echo " chaque script effectue la tache demandée sur l'os cible"
echo ""
echo "liste des modules:"
here=$1
mods=$(/usr/bin/find $here/mods/ -type d -exec basename {} \; | grep -v mods)
for m in $mods
do
	echo "$m:"
	cat $here/mods/$m/help 2>/dev/null
done
exit 0

