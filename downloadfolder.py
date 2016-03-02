"""Download folder manager"""

import os
import glob
import pdb #pdb.set_trace()
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
    c = None
    while(c == None):
        print ("What do you want to do?");
        print ("1.Show files");
        print ("2.Erase dumb files");
        print ("3.Group Anime Files");
        print ("4.Remove Torrent files");
        try:
            c = int(input("Choice> "));
        except (ValueError):
            print ("");
            print ("-- Invalid choice!");
            print ("");
            continue
        if (c < 0) or (c > 10):
            print ("");
            print ("-- Invalid choice!");
            print ("");
            c = None
            continue

        elif (c == 1):
            return 1
        elif (c == 2):
            return 2
        elif (c == 3):
            return 3
        elif (c == 4):
            return 4
        elif (c == 5):
            return 5
    print(c)

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
    

def listFiles():
    """List files"""
    print ("  ---Filelist---");
    li = os.listdir()
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

def main():
    DOWNLOADPATH = loadConfig('config.ini');
    if (DOWNLOADPATH == False):
        print ("--Quitting...")
        sys.exit()
    c = menu();
    #Choices
    if (c == 1):
        listFiles();
    elif (c == 2):
        print ("NOT IMPLEMENTED");
    elif (c == 3):
        print ("NOT IMPLEMENTED");
    elif (c == 4):
        print ("NOT IMPLEMENTED");
    elif (c == 5):
        print ("NOT IMPLEMENTED");

if __name__ == "__main__":
    main()




