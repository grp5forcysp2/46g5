#!/bin/bash:
echo " python 46g5.py [-a] [mod1]  ... [modn]"
echo "   mod(n) designe un module d'investigation."
echo " Les modules disponibles se trouvent dans le repertoire ./mods/ ."
echo " Ceux sont des repertoires du nom du module, contenant:"
echo "  - un script shell:           run.sh"
echo "  - un script powershell:      run.ps1"
echo "  - un fichier de description: desc.txt"
echo "  Les script run{sh,ps1} effectuent la tache decrite dans le fichier desc.txt "
echo ""
echo "liste des modules:"
here=$1
mods=$(/usr/bin/find $here/mods/ -type d -exec basename {} \; | grep -v mods)
for m in $mods
do
	echo "-- $m:"
	cat $here/mods/$m/desc.txt 2>/dev/null
	echo ""
done
echo " Exemples:"
echo "python 46g5.py -a: affiche tout ce qu'il peut."
echo "python 46g5.py recents: affiche les fichiers recemments utilisés."
echo "python 46g5.py -a > rapport.txt : affiche tout ce qu'il peut et le sauve dans rapport.txt."
exit 0

