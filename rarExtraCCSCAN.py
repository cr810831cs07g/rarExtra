# -*- coding: utf8 -*-
from importlib.metadata import files
import unrar,os, sys, glob
from rarfile import RarFile

pwd1 = 'P@ssw0rd'           # 第一層解壓密碼
pwd2 = '[Corecloud]'        # 第二層解壓密碼
path1 = os.path.dirname(os.path.realpath(__file__))
for i in glob.glob("*.rar"):
    os.chdir(path1)
    with RarFile(i, 'r') as myrar:
        myrar.extract('m.rar.log',path='tmp', pwd=pwd1) 
        myrar.close()

        path2 = './tmp'
        file = 'm.rar.log'
        os.chdir(path2)
        new_file = i[:-4] + '_' + file[:-4]
        print(new_file)
        os.rename(file, new_file)
        
# dangerous
for s in glob.glob("*.rar"):
    with RarFile(s, 'r') as danrar:
        danrar.extractall(path=s[:-4], pwd=pwd2)
        danrar.close()
print('[+] Extract OK !')
