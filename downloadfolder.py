"""Download folder manager"""

import os
import glob
import pdb
import configparser
import sys

def loadConfig(file):
    """Load config file with path"""
    config = configparser.ConfigParser();
    config.sections();
    config.read(file);

    try:
        downloadpath = config['common']['DOWNLOADPATH']
    except (KeyError):
        print ("--Error: Couldn't read path. Corrupt ini file?");
        return False

    try:
        os.chdir(downloadpath)
    except (FileNotFoundError):
        print("--Error: Path not found! Did you type it correctly in the config file?")
        return False;
    return True;
        
def toptensize():
    """Show a list of top ten biggest files"""
    pass;

def numOfFiles():
    """Returns number of files"""
    return len(li);

def menu():
    print ("What do you want to do?");
    print ("1.Erase dumb files");
    print ("2.Group Anime Files");
    print ("3.Remove Torrent files");
    return;



def removeTorrentFiles():
    for file in li:
        if file.endswith(".torrent"):
            os.remove(file);
            print(file);
    return

def listFileSizes():
    """Displays sizes of files"""

    x = 0;
    size = [];
    while x < len(li):
        #print(x.st_size);
        f = DOWNLOADPATH+li[x];
        
        try:
            size.append(os.stat(f).st_size);
            break
        except WindowsError:
            print ("ERROR!");
        
        x = x + 1;

    size.sort();
    x = 0;
    for x in size:
        print (bConv(x));
    return
    

def listFiles(li):
    """List files"""
    print ("  ---Filelist---");
    
    x = "";
    for x in li:
        print(x);
    print ("  --------------");
    return

def bConv(byte,mode=None):
    """Converts bytevalues to other things"""
    KB = 1000;
    MB = 10000;

    if (mode==None) or (mode=="kb"):
        #print(byte/KB,end="");
        #print(" KB");
        return byte/KB;
    elif (mode=="mb"):
        return byte/MB;
    else:
        print("Error");
    return



DOWNLOADPATH = loadConfig('config.ini');
if (DOWNLOADPATH == False):
    print ("--Quitting...")
    sys.exit()

menu();

