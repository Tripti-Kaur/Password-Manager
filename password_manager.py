from genericpath import getsize
from cryptography.fernet import Fernet
import os

# Fernet is a module that allows you to encrypt texts

'''
def write_key():
    key = Fernet.generate_key()
    with open("key.key","wb") as key_file:
        key_file.write(key)
'''


def load_key():
    file = open("key.key","rb")
    key = file.read()
    file.close()
    return key


def view():
    with open('passwords.txt','a') as f:
        with open('passwords.txt','r') as f:
            if os.path.getsize('passwords.txt')==0:
                print("No password is saved.\n")
                return
            for line in f.readlines():
                user, password = line.rstrip().split("|")
                print("User name:", user, "| Password:", fer.decrypt(password.encode()).decode())


def add():
    name = input("Account Name: ")
    pwd = input("Password: ")

    with open('passwords.txt','a') as f:
        f.write(name + " | " + fer.encrypt(pwd.encode()).decode() + "\n")

    # you can write the below as even file = open('passwords.txt','a') but if we do so we must even close the file manually so we need to add file.close() and if you don't close the file it will still be open and if you try to access it somewhere else then that might cause problems.
    # Hence we use with keyword which helps you by automatically closing the file for you.
    # modes of files..
    # 'w'(write): so basically if the file with the name already exists then it will clear that file and open a new one. So use 'w' mode only if you always want to overwrite the file that already exists
    # 'r' (read): You can't write anything in this file using r mode. It is just used to read the file. It may cause problem if you try to read a file that doesn't exists
    # 'a' (append): Most flexible mode. It allows you to add something to the end of the existing file and create a new file if it doesn't exists. And so we can write the file and also we can even read the entire file.



# Driver Code

# write_key()
key = load_key()
fer = Fernet(key)

while True:
    mode = input("Would you like to add a new password or view existing ones (view, add), press q to quit? ").lower()

    if mode == "view":
        view()
    elif mode == "add":
        add()
    elif mode == "q":
        break
    else:
        print("Invalid mode.")
        continue
