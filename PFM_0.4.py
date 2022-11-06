import os

# Prints the introduction.
print("Welcome to Python File Manager 0.4!!")
print("Type 'help' for help.")
print("Do 'p' for patch notes.")

# Defines the help command.
def doHelp():
    print("Welcome to help command!")
    print("Available commands:")
    print("[p] List new patch notes.")
    print("[ls] List the contents of the current directory.")
    print("[ta] Add text to an existing text file.")
    print("[tw] Overwrite an existing text file.")
    print("[cat] Shows the contents of a text file.")
    print("[mk] Create a file.")
    print("[mkdir] Create a directory.")
    print("[rm] Remove a file.")
    print("[rmdire] Remove a empty directory.")
    print("[exit] Exit the program.")
    doStartup()

# Defines the p command.
def doP():
    print("Welcome to PFM patch notes!")
    print("Version: 0.4")
    print("0.4 patch notes:")
    print("-Added full compatability with files out of external folders.")
    print("-A function in the code was relocated.")
    print("-Most commands got new phrases!")

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
    print("What file do you want to read?(Also write it's path!)")
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
    print("Please enter the name of the file and it's path:")
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

# Defines the startup funcion.
def doStartup():
    i = input(">")

    match i:
        case "p":
            doP()
        case "ls":
            doLs2()
        case "ta":
            doTa()
        case "tw":
            doTw()
        case "cat":
            doCat()
        case "mk":
            doMk()
        case "mkdir":
            doMkdir()
        case "rm":
            doRm()
        case "rmdire":
            doRmdire()
        case "help":
            doHelp()
        case "exit":
            print("Thank you for using PFM!")
            exit()
    doStartup()

# Starts the program.
doStartup()
