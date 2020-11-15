import os
from linux import *
from docker import *
from hadoop import *
from aws import *
from ansible import *

while True:
    os.system("clear")
    os.system("tput setaf 1")
    print("\t\t\t ----------------------")
    print("\t\t\t Welcome To Our Program")
    print("\t\t\t ----------------------")
    os.system("tput setaf 7")
    os.system("tput setaf 2")
    print("""
            Press 1: For OS (Linux) related services
            Press 2: For Docker related services
            Press 3: For Hadoop related services
            Press 4: For Ansible related services 
            Press 5: For Amazon Web Services (AWS) 
            Press 6: For Exit
            """)
    print("\n")
    os.system('tput setaf 3')
    ch = int(input("Enter your choice:- "))
    os.system('tput setaf 7')
    if ch == 1:
        LinuxMenu()
    elif ch == 2:
        DockerMenu()
    elif ch == 3:
        HadoopMenu()
    elif ch == 4:
        AnsibleMenu()
    elif ch == 5:
        AWS_Menu()
    elif ch == 6:
        os.system('clear')
        print("\n")
        os.system('tput setaf 1")
        print("\t\t\t -------------------")
        print("\t\t\t Thank You !! ")
        print("\t\t\t -------------------")
        os.system('tput setaf 7')
        exit()


