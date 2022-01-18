# -*- coding: utf8 -*-
import unrar,os, sys


path = "/usr/naco/Desktop/ccscan_rar/"
dirname = os.path.dirname(path)
print(dirname)
def decryptRarZipFile(filename):
    if filename.endswith('.rar'):
      fp = rarfile.RarFile(filename)
    desPath = filename[:-4]
    
    if not os.path.exists(desPath):
        os.mkdir(desPath)
    
    try:
        fp.extractall(desPath)
        fp.close()
        print('no pwd')
        return
    except:
        try:
            fpPwd = ('P@ssw0rd')
            print('222')
        except:
            print('no dict file pwd in current')
        return
        fp.extractall(path=desPath, pwd=fpPwd)
        print('111')

if __name__ == '__main__':
    filename = sys.argv[1]

    if os.path.isfile(filename) and filename.endswith('.rar'):
        decryptRarZipFile(filename)
