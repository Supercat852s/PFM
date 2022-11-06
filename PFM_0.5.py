import os
from cryptography.fernet import Fernet

# Prints the introduction.
print("Welcome to Python File Manager 0.5!!")
print("Type 'help' for help.")
print("Do 'p' for patch notes.")
print("Version splash: Why not encrypt your files?")

# Defines the help command.
def doHelp():
    print("Welcome to help command!")
    print("Available commands:")
    print("[p] List new patch notes.")
    print("[ls] List the c of the current directory.")
    print("[ta] Add text to an existing text file.")
    print("[tw] Overwrite an existing text file.")
    print("[cat] Shows the c of a text file.")
    print("[mk] Create a file.")
    print("[mkdir] Create a directory.")
    print("[rm] Remove a file.")
    print("[rmdire] Remove a empty directory.")
    print("[ec] Encrypt a file of your choice.")
    print("[dc] Decrypt a encrypted file.")
    print("[exit] Exit the program.")
    doStartup()

# Defines the p command.
def doP():
    print("Welcome to PFM patch notes!")
    print("Version: 0.5")
    print("0.5 patch notes:")
    print("-The encrypt command was added.")
    print("-The decrypt command was added.")
    print("-The version splash was added.")

# Defines the ls command.
def doLs1():
    for file in os.listdir():
        if os.path.isfile(os.path.join(file)):
            yield file

# Runs the ls command when called. 
def doLs2():
    print("---------Name---------")
    for file in doLs1():
        print("|--"+file+"--|")
    doStartup()  

# Defines the ta command.
def doTa():
    print("Please select the file to append and use it's path:")
    i = input(">")
    with open(i, "a") as a:
        print("Please write what to append:")
        i = input(">")
        a.write(i)
        print("Operation succesful.")
    doStartup()

# Defnes the tw command.
def doTw():
    print("Please select file and path:")
    i = input(">")
    with open(i, "w") as w:
        print("What do you want to overwrite?")
        i = input(">")
        w.write(i)
        print("Operation succesful.")
        doStartup()

# defines the cat command.
def doCat():
    print("What file do you want to read?(Also write its path!)")
    i = input(">")
    with open(i, "r") as r:
        print("How many characters do you want to read?")
        i = input(">")
        r = r.read(int(i))
        print(r)
        print("Operation succesful.")
        doStartup()

# Defines the mk command.
def doMk():
    print("Please enter the name of the file and its path:")
    i = input(">")
    with open(str(i), "x"):
        print("Operation succesful.")
    doStartup()    

# Defines the mkdir command.
def doMkdir():
    print("Please place a valid directory name:")
    i = input(">")
    print("Please type the parent's folder path:")
    parent_path = input(">")
    mode = 0o666
    path = os.path.join(parent_path, i)
    os.mkdir(i, mode)
    print("Operation succesful.")
    doStartup()

# Defines the rm function.     
def doRm():
    print("What file do you want removed(wiped off the planet)[Also specify the path.]?")
    i = input(">")
    if os.path.exists(i):
        os.remove(i)
        print("File removed.")
    else:
        print("The file does not exist.")
        doRm()
    doStartup()

# Defines the rmdir funcion.
def doRmdire():
    print("What empty directory you want to remove?[Also specify it's path.]")
    i = input(">")
    os.rmdir(i)
    print("Directory removed.")
    doStartup()

# Defines the ec command.
def doEc():
    print("What file do you want encrypted?(Also specify the path.)")
    i = input(">")
    file = i
    with open(file, "rb") as r:
        c = r.read()
    key = Fernet.generate_key()
    print("Please copy this key for later decryption: " + str(key))
    if os.path.exists("thekey.key"):
        os.remove("thekey.key")
    with open("thekey.key", "x") as x:
        with open("thekey.key", "wb") as w:
            w.write(key)
    ce = Fernet(key).encrypt(c)
    with open(file, "wb") as w:
        w.write(ce)
    print("File encrypted succesfully.")
    doStartup()
    
    # c_e = Fernet(password).encrypt(c)
    # with open(file, "wb") as wb:
    #     wb.write(c_e)

# Defines the dc command.
def doDc():
    print("What file do you want decrypted?[Specify the path!]")
    i = input(">")
    file = i
    with open(i, "rb") as rb:
        c = rb.read()
    with open("thekey.key", "rb") as rb:
        key = rb.read()
    print("What's the key?")
    i = input(">")
    if str(i) == str(key):
        with open(file, "w") as wb:
            cd = Fernet(key).decrypt(c)
            wb.write(str(cd))
        print("File decrypted.")
    else:
        print("--WRONG KEY--")
        print("The whole command was rerunned.")
        print("Next time enter the correct key!")
        doDc()
    if os.path.exists("thekey.key"):
        os.remove("thekey.key")
    doStartup()

# Defines the startup funcion.
def doStartup():
    i = input(">")
    if i == "p":
        doP()
    if i == "ls":
        doLs2()
    if i == "ta":
        doTa()
    if i == "tw":
        doTw()
    if i == "cat":
        doCat()
    if i == "mk":
        doMk()
    if i == "mkdir":
        doMkdir()
    if i == "rm":
        doRm()
    if i == "rmdire":
        doRmdire()
    if i == "ec":
        doEc()
    if i == "dc":
        doDc()
    if i == "help":
        doHelp()
    if i == "exit":
        print("Thank you for using PFM!")
        exit()    
    doStartup()

# Starts the program.
doStartup()
