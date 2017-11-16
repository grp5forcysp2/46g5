
write-host  " python 46g5.py [-a] [mod1]  ... [modn]"
write-host  "   mod(n) designe un module d'investigation."
write-host  " Les modules disponibles se trouvent dans le repertoire ./mods/ ."
write-host  " Ce sont des repertoires du nom du module, contenant:"
write-host  "  - un script shell:           run.sh"
write-host  "  - un script powershell:      run.ps1"
write-host  "  - un fichier de description: desc.txt"
write-host  "  Les script run{sh,ps1} effectuent la tache decrite dans le fichier desc.txt "
write-host  ""
write-host  "liste des modules:"
$mods= get-childitem mods/ 

foreach($m in $mods){
	#write-host  "-- ${m}:"
	write-host  "-- $m --"
	get-Content mods\$m\desc.txt 
	write-host  ""
}


write-host  " Exemples:"
write-host  "python 46g5.py -a: affiche tout ce qu'il peut."
write-host  "python 46g5.py recents: affiche les fichiers recemments utilisés."
write-host  "python 46g5.py -a > rapport.txt : affiche tout ce qu'il peut et le sauve dans rapport.txt."
exit 0


exit 0
