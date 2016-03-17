"""Download folder manager
   By Zenkerdus    
"""

#TODO:
#detect extensions and create folders
#folder moving?
#Function/class for handling exceptions?
#Continue moving other files even if error instead of return?
#Log errors to stderror

#Test:
#If file is PNG instead of png? Unneccessary?

import os
import shutil
import glob
import pdb #pdb.set_trace()
import configparser
import sys
from collections import OrderedDict

EXTENSIONS = ['7z', 'apk', 'bin','docx', 'epub', 'exe', 'gba', 'jar', 'jpg', 'mkv',
              'mp3', 'mp4', 'msi', 'nds', 'odt', 'pdf', 'png', 'rar', 'stl',
              'txt', 'wav', 'zip']

E_REMOVE = ["nsf","sfk","obj","html","properties","php","svg","ini",]

E_IMAGES = ["png", "jpg", "jpeg", "bmp","tif"]
E_DOCS = ["docx", "odt", "pdf", "ods"]
E_AUDIO = ["mp3", "wav"]
E_VIDEOS = ["mp4","flv"]
E_COMPRESSED = ["rar","7z","rar","zip"]
E_SOFTWARE = ["apk","exe","nds","gba","msi"]

PATH = "#sortedDownloads/"

def startMessage():
    print ("----------------------------")
    print ("-  Downloadfolder manager  -")
    print ("----------------------------")
    return

def loadConfig(file):
    """Load config file and change to that directory. Must be done before
    anything else
    """
    config = configparser.ConfigParser();
    config.sections();
    config.read(file);

    try:
        downloadpath = config['common']['DOWNLOADPATH']
    except KeyError as e:
        print ("--Error: Couldn't read path. Corrupt ini file?");
        print ("--E:", e)
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
        print ("4.Remove junk files");
        print ("5.DEBUG-Move files back");
        print ("6.Count filetypes in downloadfolder")
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
        elif (c == 6):
            return 6
        elif (c == 7):
            return 7
        elif (c == 8):
            return 8
        elif (c == 9):
            return 9
        elif (c == 0):
            return 0
    print(c)

def removeJunkFiles():
    """Removes files with extensions from E_REMOVE"""
    li = os.listdir()
    global E_REMOVE
    for e in E_REMOVE:
        for file in li:
            if file.endswith(e):
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
    print ("  --------------");
    li = os.listdir()
    x = "";
    for x in li:
        if os.path.isfile(x) == False:
            print(x, " -- (Folder)")
        else:
            print(x)
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
    """Creates dir 'sortedfolder' and filetype folders from EXTENSIONS"""
    global EXTENSIONS;
    global PATH;
    try:
        os.mkdir(PATH)
    except FileExistsError as err:
        print (PATH + " exists");
    os.chdir(PATH)
    for e in EXTENSIONS:
        try:
            os.mkdir(e);
        except FileExistsError as err:
            print (e + " exists")
        else:
            print (e, " created");
    print ()
    print ("Done")
    
    os.chdir(os.pardir)

def pathFolderExists(mode=None):
    """Check if global PATH folder exists"""
    global PATH
    li = os.listdir()

    if (mode == None):
        try:
            os.listdir(PATH)
        except FileNotFoundError as err:
            print("-- Error: ", PATH , " doesn't exist.")
            print("Restart the program to make one.")
            print("Err: ", err)
            print()
            return False
        return True

    #For first time run at beginning of program"""
    elif (mode == "intro"):
        try:
            os.listdir(PATH)
        except FileNotFoundError as err:
            print("Your downloadfolder doesn't have an ", PATH, " folder yet.")
            print("It is needed to sort folders.")
            print("Do you want me to create it?")
            a = input("(Y/N): ")
            a = a.upper()
            if (a == "Y" or a == "YES"):
                makeDirs()
            else:
                print(PATH, " not created")
                print()
                return False

            return True
        
def moveFiles():
    """Move downloaded files to folders"""
    global EXTENSIONS
    global PATH;

    pathFolderExists();
    li = os.listdir()
    counter = 0;
    for file in li:
        for e in EXTENSIONS:

            #if e == "images"
            #for img in IMAGEFORMATS 

            
            if file.endswith(e):
                f = PATH+e+"/"+file; #TODO
                try:
                    os.rename(file,PATH+e+"/"+file)
                except FileNotFoundError as err:
                    print("--Error: Have you created folders first? Choose 3 in menu");
                    print("--Message: ",err);
                    return 1
                except FileExistsError as err:
                    print("--Error: File already exists!")
                    print("--Message: ",err)
                    c = ""
                    c = input("Remove? (Y/N)")
                    c = c.upper() 
                    if (c == "Y" or c == "YES"):
                        os.remove(file)
                        print("Removed ", file)
                    elif ( c == "N" or c == "NO"):
                        continue
                except PermissionError as e:
                    print("--Error: File is being used!")
                    print("--Message: ",e)
                    return 1
                    
                print("Moved ", end="")
                print(file, end="")
                print(" to ", end="")
                print(file,PATH+e+"/"+file)
                counter=counter+1
    if (counter == 0):
        print ("No valid files to sort");
    else:
        print ()
        print ("Moved ",counter," files")

def moveFilesBack():
    """DEBUGGING - Move files back from folders, moveFiles in reverse"""
    global EXTENSIONS
    global PATH
    pathFolderExists()
    li = os.listdir()
    counter = 0
    for e in EXTENSIONS:
        try:
            li = os.listdir( PATH + "/" + e);
        except FileNotFoundError:
            print("--Error: File/folder doesn't exist. Skipping")
        
        print("moveFilesBack: ",PATH + e) #DEBUG
        for file in li:
            try:
                #move file
                os.rename( PATH + e + "/" + file, file); 
            except FileNotFoundError as e:
                print("--Error:")
                print("--Message: ",e);
                return 1
            except FileExistsError as err:
                print("--Error: File already exists!")
                print("--Message: ",err)
                c = ""
                c = input("Remove from sorted folder? (Y/N)")
                c = c.upper()
                if (c == "Y" or c == "YES"):
                    os.remove( PATH + e + "/" + file)
                    print("Removed ", file)
                elif ( c == "N" or c == "NO"):
                    continue
            except PermissionError as e:
                print("--Error: File is being used!")
                print("--Message: ",e)
                return 1

            print("Moved ", end="")
            print(file, end="")
            print(" to ", end="")
            print(file,PATH+e+"/"+file)
            counter=counter+1
    if (counter == 0):
        print ("No valid files to sort");
    else:
        print ()
        print ("Moved ",counter," files")

def rmListDupes(li):
    """Return list with dupes in list removed"""
    li = list(set(li));
    li.sort()
    return li      
        
def detectExtensions():
    """Return file extensions from downloaded files"""
    global PATH
    li = os.listdir();
    found = []
    
    for file in li:
        i = file.rfind(".")
        l = len(file[i:])
        if (i == -1): #Didn't find extension, skip file
            continue
        elif (l > 5 or l < 3 ): #Extension length limit
            continue
        found.append(file[i:])

    return found

def countFileTypes():
    """Count occurence of filetypes in folder"""
    global PATH
    li = detectExtensions();
    EXT = rmListDupes(li)
    sortedCounter = {}
    counter = 0;
    other = 0;
    
    for e in EXT:
        for file in li:
            if file == e:
                counter = counter + 1;
                #index(e)
                
        sortedCounter[e] = counter
        #print(e, counter)
    
    sortedCounter = OrderedDict(sorted(sortedCounter.items(), key=lambda t: t[1]))
    for filetype in sortedCounter:
        print (filetype,"\t",sortedCounter[filetype])
    print("")

    
def quitting():
    print ("Quitting...")
    sys.exit()

def main():
    startMessage()
    validpath = loadConfig('config.ini');

    pathFolderExists("intro")

    if (validpath == False):
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
        elif (c == 4): #remove junk files
            removeJunkFiles();
        elif (c == 5): #DEBUG - move files back
            moveFilesBack()
        elif (c == 6): #show number of filetypes
            countFileTypes()
            
        elif (c == 0): #quit
            quitting()
        print ("  --------------");

if __name__ == "__main__":
    main()
