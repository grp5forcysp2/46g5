
==========================================================================
=========                46g5v:0.1           =============================
==========================================================================
    
OS: Linux
usage:
 python 46g5.py [-a] [mod1]  ... [modn]
   mod(n) designe un module d'investigation.
 Les modules disponibles se trouvent dans le repertoire ./mods/ .
 Ceux sont des repertoires du nom du module, contenant:
  - un script shell:           run.sh
  - un script powershell:      run.ps1
  - un fichier de description: desc.txt
  Les script run{sh,ps1} effectuent la tache decrite dans le fichier desc.txt 

liste des modules:
-- pstree:
Affichage de l'arborescence des processus.
Linux: ps -aef f
Windows: TODO

-- signs:
Linux: md5sum des fichiers presents dans /tmp /var/tmp
Windows: md5sum des fichiers dans %temp%

-- navhist:
Windows: TODO
Linux: TODO

-- recents:
Linux: recherche les fichiers lus depuis 24h
Windows: Liste les documents recents

-- srvlst:
Liste des services.

-- usage:
Affiche l'usage

-- autoruns:
Windows: liste les programmes persistants avec autorunsc.
Linux: TODO

-- planlst:
Windows: liste les taches planifiées.
Linux: liste les crontab

-- ps:
Liste des processus

-- logs:
Windows: affiche les logs avec psloglist
Linux: TODO (copie ou affiche ?)

-- network:
Affiche les connections reseau en cours.

 Exemples:
python 46g5.py -a: affiche tout ce qu'il peut.
python 46g5.py recents: affiche les fichiers recemments utilisés.
python 46g5.py -a > rapport.txt : affiche tout ce qu'il peut et le sauve dans rapport.txt.

