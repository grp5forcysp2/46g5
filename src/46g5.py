import sys, subprocess, os, platform, ctypes
version='0.1'

here = ''

def hello():
    hello = '''
==========================================================================
=========                46g5v:%s           =============================
==========================================================================
    ''' % version
    print(hello)

def usage():
    print(Usage)

def modexist(m,target):
    lok = os.path.exists("%s/mods/%s/run.sh" % (here,m))
    wok = os.path.exists("%s/mods/%s/run.ps1" % (here,m))
    if (target == 'Linux' and lok):
        return True
    if (target == 'Windows' and wok):
        return True
    print("module %s indisponible pour l'os: %s" % (m,target))
    return False

def getallmods():
    mods = []
    for d in os.listdir(here+'/mods'):
        print(d)
        if os.path.isdir(here+'/mods/'+d) and d != 'usage':
            print(d)
            mods.append(d)
    print(mods)
    return mods
    
def parseargs(target):

    args = sys.argv[1:]
    mods = []
    
    if len(args) == 0:
         mods = ['usage']
    else:
        if args[0] == '-a':
            mods = getallmods()
        else:
           for a in args:
               if modexist(a,target):
                  mods.append(a)
               #
            #
        #
    #
    return mods

def runmods(mod,target):
    print('%s:'%mod)
    out = '' 
    if target == 'Linux':
       modexe =  '%s/mods/%s/run.sh' % (here,mod)
       out += subprocess.check_output(["/bin/sh", modexe, here])
    else:
       modexe =  '%s/mods/%s/run.ps1' % (here,mod)
       out += subprocess.check_output(["powershell.exe", '-executionpolicy','unrestricted',modexe, here])
       
    print(out)

def getcurOS():
    pf = platform.system()
    print('OS: %s'% pf)
    return pf


def is_user_admin():
    try:
       return os.getuid() == 0
    except AttributeError:
        pass
    try:
       return ctypes.windll.shell32.IsUserAnAdmin() == 1
    except AttributeError:
       return False 


def run46g5():
    hello()
    if not is_user_admin():
        print("Veuillez utiliser un compte administrateur.")
        return

    target = getcurOS()
    mods = parseargs(target)
    for mod in mods:
        runmods(mod,target)

if __name__ == '__main__':
        here = os.path.dirname(os.path.abspath(__file__))
        sys.exit(run46g5())
    
