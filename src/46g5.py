import sys, subprocess, os, platform
version='0.1'

here = ''

def hello():
    print("46g5 version:%s" %version)

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
    print(sys.argv)
    args = sys.argv[1:]
    mods = []
    if args[0] == '-a':
        mods = getallmods()
    else:
        if len(args) == 0:
           mods = ['usage']
        else:
           for a in args:
               if modexist(a,target):
                  mods.append(a)
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
    print('running on %s'% pf)
    return pf

def run46g5():
    target = getcurOS()
    hello()
    mods = parseargs(target)
    for mod in mods:
        runmods(mod,target)

if __name__ == '__main__':
        #here = os.path.dirname(__file__)
        here = os.path.dirname(os.path.abspath(__file__))
        print("here: %s"%here)
        sys.exit(run46g5())
    
