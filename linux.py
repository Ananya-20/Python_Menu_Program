import os 
def Locally():
    while True:
        os.system("clear")
        os.system("tput setaf 1")
        print("\t\t\t -------------------------")
        print("\t\t\t Welcome To Linux Services")
        print("\t\t\t -------------------------")
        os.system("tput setaf 7")
        os.system("tput setaf 2")
        print("""
            Press 1: To Check IP Address
            Press 2: Date
            Press 3: Calendar
            Press 4: Create a directory
            Press 5: Create a file
            Press 6: Configure Web Server
            Press 7: Exit
            """)
        if ch == 1:
            print("Checking the IP...")
            os.system("ifconfig enp0s3")
        elif ch == 2:
            os.system("date")
        elif ch == 3:
            os.system("cal")
        elif ch == 4:
            Dir_Nm = input("Enter the name of directory")
            os.system("mkdir {}".format(Dir_NM))
            print("Directory Successfully Created...")
        elif ch == 5:
            File_Nm = input("Enter the name of file")
            os.system("touch {}".format(File_Nm))
            print("File Successfully Crested...")
        elif ch == 6:
            os.system("yum install httpd -y")
            os.system("cp index.html /var/www/html/index.html")
            os.system("systemctl start httpd")
            os.system("systemctl status httpd")
        elif ch == 7:
            break
        else:
            print("Enter a valid choice")
            input()


def LinuxMenu():
    print()
    os.system("tput setaf 3")
    login = input("In which way you want to work: locally/remotely")
    print(login)
    print()
    os.system("tput setaf 7")
    if login == "remotely":
        RemoteLogin()
    elif login == "locally":
        Locally()
    else:
        print("Enter a valid choice")
        input()

