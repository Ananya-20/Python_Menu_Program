import os 

def RemoteLogin():
	pass

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
            Press 7: Launch Firefox
            Press 8: To add a new user
            Press 9: To delete a new user
            Press 10: To ping an IP address
            Press 11: Install a package/software using yum
            Press 12: Uninstall a package/software using yum
            Press 13: Exit
            """)
        ch = int(input("Enter your Choice:"))
        if ch == 1:
            print("Checking the IP...")
            os.system("ifconfig enp0s3")
        elif ch == 2:
            os.system("date")
        elif ch == 3:
            os.system("cal")
        elif ch == 4:
            Dir_Nm = input("Enter the name of directory ")
            os.system("mkdir {}".format(Dir_NM))
            print("Directory Successfully Created...")
        elif ch == 5:
            File_Nm = input("Enter the name of file ")
            os.system("touch {}".format(File_Nm))
            print("File Successfully Created...")
        elif ch == 6:
            os.system("yum install httpd -y")
            os.system("cp index.html /var/www/html/index.html") #here index.html is a pre-created webpage in the same directory where this script is running
            os.system("systemctl start httpd")
            os.system("systemctl status httpd")
        elif ch == 7:
            os.system("firefox")
        elif ch == 8:
            username = input("Enter a new username ")
            os.system(f"useradd {user_name};id {user_name}")
        elif ch == 9:
            user_name=input("Enter the username To Delete : ")
			os.system(f"userdel {user_name}")
        elif ch == 10:
            ip = input("Enter IP or Hostname you want to ping : ")
			os.system("ping {}".format(ip))
        elif ch == 11:
            software = input("Enter package you want to install ")
			os.system(f"yum install {software}")
        elif ch == 12:
            soft = input("\t\tEnter package you want to uninstall ")
			os.system(f"yum remove {soft}")
        elif ch == 13:
            break
        else:
            print("Enter a valid choice")
            print()


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

