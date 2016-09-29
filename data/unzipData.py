from zipfile import ZipFile
import glob as gb
import os

os.chdir (os.path.dirname(os.path.realpath(__file__)))

zfiles = gb.glob('*.zip')
for f in zfiles:
    print ("Unzipping: %s" % f)
    ZipFile(f).extractall()
    
print ("Done")
    
