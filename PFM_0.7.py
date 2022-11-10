import os
import shutil
from cryptography.fernet import Fernet

# Prints the introduction.
print("Welcome to Python File Manager 0.7!!")
print("See https://github.com/Supercat852s/PFM/tree/main for seeing the code.")
print("Type 'help' for help.")
print("Do 'p' for patch notes.")
print("Version splash: Echo command saves the environment!")


# Defines the help command.
def do__h_e_l_p__command():
    print("Welcome to help command!")
    print("Available commands:")
    print("[p] List new patch notes.")
    print("[echo] Print on the screen something of your choice.")
    print("[ls] List the c of the current directory.")
    print("[ta] Add text to an existing text file.")
    print("[tw] Overwrite an existing text file.")
    print("[cat] Shows the c of a text file.")
    print("[mk] Create a file.")
    print("[mkdir] Create a directory.")
    print("[rn] Rename a file.")
    print("[mv] Move a file from one place to another.")
    print("[cp] Copy a file.")
    print("[rm] Remove a file.")
    print("[rmdir] Remove a empty directory.")
    print("[ec] Encrypt a file of your choice.")
    print("[dc] Decrypt a encrypted file.")
    print("[exit] Exit the program.")
    start()


# Defines the p command.
def do_patch_notes():
    print("Welcome to PFM patch notes!")
    print("Version: 0.7")
    print("0.7 patch notes:")
    print("-'rn' command added!")


# Defines the echo command.
def do_echo():
    print("What do you want to print on the screen?")
    i = input(">")
    print(i)


# Defines the ls command.
def do_list_1():
    for file in os.listdir():
        if os.path.isfile(os.path.join(file)):
            yield file


# Runs the ls command when called. 
def do_list_2():
    print("---------Name---------")
    for file in do_list_1():
        print("|--"+file+"--|")
    start()


# Defines the ta command.
def do_text_append():
    print("Please select the file to append and use it's path:")
    i = input(">")
    with open(i, "a") as a:
        print("Please write what to append:")
        i = input(">")
        a.write(i)
        print("Operation successful.")
    start()


# Defines the tw command.
def do_text_write():
    print("Please select file and path:")
    i = input(">")
    with open(i, "w") as w:
        print("What do you want to overwrite?")
        i = input(">")
        w.write(i)
        print("Operation successful.")
        start()


# defines the cat command.
def do_cat():
    print("What file do you want to read?(Also write its path!)")
    i = input(">")
    with open(i, "r") as r:
        print("How many characters do you want to read?")
        i = input(">")
        r = r.read(int(i))
        print(r)
        print("Operation successful.")
        start()


# Defines the mk command.
def do_mk():
    print("Please enter the name of the file and its path:")
    i = input(">")
    with open(str(i), "x"):
        print("Operation successful.")
    start()


# Defines the mkdir command.
def do_mkdir():
    print("Please place a valid directory name:")
    i = input(">")
    print("Please type the parent's folder path:")
    parent_path = input(">")
    mode = 0o666
    path = os.path.join(parent_path, i)
    os.mkdir(i, mode)
    print("Operation successful.")
    start()


# Defines the rn command
def rename():
    print("Please write what file to rename [and it's path!].")
    on = input(">")
    print("What is the new name for the file?")
    nn = input(">")
    os.rename(on, nn)


# Defines the mv command.
def move():
    print("What is the file that you want to move( + path )?")
    ol = input(">")
    print("What is the new path( + new_name ) of the new file?")
    nl = input(">")
    shutil.copy(ol, nl)
    os.remove(ol)
    print("File removed.")
    start()


# Defines the cp command.
def copy():
    print("What is the file that you want to move( + path )?")
    ol = input(">")
    print("What is the new path( + new_name ) of the new file?")
    nl = input(">")
    shutil.copy(ol, nl)
    print("File copied.")
    start()


# Defines the rm function.     
def do_rm():
    print("What file do you want removed(wiped off the planet)[Also specify the path.]?")
    i = input(">")
    if os.path.exists(i):
        os.remove(i)
        print("File removed.")
    else:
        print("The file does not exist.")
        do_rm()
    start()


# Defines the rmdir function.
def do_rmdir():
    print("What empty directory you want to remove?[Also specify it's path.]")
    i = input(">")
    os.rmdir(i)
    print("Directory removed.")
    start()


# Defines the ec command.
def encrypt():
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
    print("File encrypted successfully.")
    start()
    
    # c_e = Fernet(password).encrypt(c)
    # with open(file, "wb") as wb:
    #     wb.write(c_e)


# Defines the dc command.
def decrypt():
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
        print("The whole command was ran again.")
        print("Next time enter the correct key!")
        decrypt()
    if os.path.exists("thekey.key"):
        os.remove("thekey.key")
    start()


# Defines the startup function.
def start():
    i = input(">")
    if i == "p":
        do_patch_notes()
    if i == "echo":
        do_echo()
    if i == "ls":
        do_list_2()
    if i == "ta":
        do_text_append()
    if i == "tw":
        do_text_write()
    if i == "cat":
        do_cat()
    if i == "mk":
        do_mk()
    if i == "mkdir":
        do_mkdir()
    if i == "mv":
        move()
    if i == "cp":
        copy()
    if i == "rm":
        do_rm()
    if i == "rmdir":
        do_rmdir()
    if i == "ec":
        encrypt()
    if i == "dc":
        decrypt()
    if i == "help":
        do__h_e_l_p__command()
    if i == "exit":
        print("Thank you for using PFM!")
        exit()    
    start()


# Starts the program.
start()
