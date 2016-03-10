"""Download folder manager
   By Zenkerdus    
"""

#TODO:
#Correct backslashes on paths!

import os
import glob
import pdb #pdb.set_trace()
import configparser
import sys

EXTENSIONS = ["rar","zip","mkv","mp3", "7z", "jpg", "png", "odt", "exe", "pdf", "nds", "msi"];
PATH = "sortedDownloads/"



def startMessage():
    print ("----------------------------")
    print ("-  Downloadfolder manager  -")
    print ("----------------------------")
    return


def loadConfig(file):
    """Load config file with path"""
    config = configparser.ConfigParser();
    config.sections();
    config.read(file);

    try:
        downloadpath = config['common']['DOWNLOADPATH']
    except KeyError as e:
        print ("--Error: Couldn't read path. Corrupt ini file?");
        print ("--E:",end="")
        print (e);
        return False

    try:
        os.chdir(downloadpath)
        print ("Downloadfolder: ", downloadpath, end="\n\n")
    except (FileNotFoundError):
        print("--Error: Path not found! Did you type it correctly in the config file?")
        return False;
    return True;
        
def toptensize():
    """Show a list of top ten biggest files"""
    pass;

def numOfFiles():
    """Returns number of files"""
    pass
    #return len(li);

def menu():
    c = None
    while(c == None):
        print ("What do you want to do?");
        print ("1.Show files");
        print ("2.Move files");
        print ("3.Create folders");
        print ("4.Remove .torrent files");
        print ("5.DEBUG-Move files back");
        print ("Q/0 - Quit");
        print ("")
        c = input("Choice> ");

        #Quit if Q
        c = c.upper()
        if (c == "Q" or c == "QUIT" or c == "EXIT"):
            return 0
        try:
            c = int(c);
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
        elif (c == 0):
            return 0
    print(c)

def removeTorrentFiles():
    li = os.listdir()
    for file in li:
        if file.endswith(".torrent"):
            os.remove(file);
            print(file);
    print("Done")
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
    print ("  --------------");
    li = os.listdir()
    x = "";
    for x in li:
        print(x);
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

def makeDirs():
    """Creates dir 'sortedfolder' and filetype folders"""
    global EXTENSIONS;
    global PATH;
    try:
        os.mkdir(PATH)
    except FileExistsError as err:
        print ("Skipping folder ", end="");
        print (PATH)
    os.chdir(PATH)
    for e in EXTENSIONS:
        try:
            os.mkdir(e);
        except FileExistsError as err:
            print ("Skipping folder ", end="")
            print (e)
        else:
            print (e, " created");
    os.chdir(os.pardir)

        


def detectFileTypes():
    """Return how many known filetypes in folder in list"""
    """extensions = ["rar","zip","mkv","mp3", "7z", "jpg", "png", "odt", "exe", "pdf"]
    li = os.listdir();
    found=[];
    for file in li:
        for t in extensions:
            if file.endswith("."+t):
                found.append(t);
                li.pop(li.index(file));
    print (found);
    print (extensions)
    print (li);"""
    pass

def moveFiles():
    """Move downloaded files to folders"""
    global EXTENSIONS
    global PATH;
    li = os.listdir()
    counter = 0;
    for file in li:
        for e in EXTENSIONS:
            if file.endswith(e):
                try:
                    os.rename(file,PATH+e+"\\"+file)
                except FileNotFoundError as e:
                    print("--Error: Have you created folders first? Choose 3 in menu");
                    print("--Message: ",e);
                    return 1
                    
                print("Moved ", end="")
                print(file, end="")
                print(" to ", end="")
                print(file,PATH+e+"\\"+file)
                counter=counter+1
    if (counter == 0):
        print ("No valid files to sort");
    else:
        print ("Moved ",counter," files")

def moveFilesBack():
    """Move files back from folders, moveFiles in reverse"""
    global EXTENSIONS
    global PATH
    li = os.listdir()
    counter = 0
    for e in EXTENSIONS:
        li = os.listdir(PATH+"\\"+e);
        print(li) #DEBUG
        for file in li:
            try:
                os.rename(PATH+file,file);
            except FileNotFoundError as e:
                print("--Error:")
                print("--Message: ",e);
                return 1

            print("Moved ", end="")
            print(file, end="")
            print(" to ", end="")
            print(file,PATH+e+"\\"+file)
            counter=counter+1
        

def quitting():
    print ("Quitting...")
    sys.exit()

def main():
    startMessage()
    DOWNLOADPATH = loadConfig('config.ini');

    if (DOWNLOADPATH == False):
        quitting();

    while (True):
        c = menu();
        #Choices
        print ("  --------------");
        if (c == 1): #show
            listFiles();
        elif (c == 2): #move
            moveFiles();
        elif (c == 3): #create folders
            makeDirs();
        elif (c == 4): #remove torrent files
            removeTorrentFiles();
        elif (c == 5): #DEBUG - move files back
            moveFilesBack()
        elif (c == 0): #quit
            quitting()
        print ("  --------------");

if __name__ == "__main__":
    main()
    #DEBUG
    #DOWNLOADPATH = loadConfig('config.ini');
    #makeDirs();
    #moveFiles()




