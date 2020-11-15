import os 

def Config_Docker():
    os.system('yum install docker-ce --nobest -y')
    os.system('systemctl start docker')
    os.system('systemctl status docker')
   
def Config_Web():
    os.system('docker run -dit --name WebOS -p 8080:80 centos')
    os.system('docker exec WebOS yum install httpd -y')
    os.system('docker cp index.html WebOS:/var/www/html/')
    os.system('docker exec WebOS /usr/sbin/httpd')
    
  
def Docker_GUI():
    os.system('docker un -it gui --env="DISPLAY" -net=host firefox:v1')
    input()
 
def DockerMenu():
    while True:
        os.system("clear")
        os.system("tput setaf 1")
        print("\t\t\t -----------------------------")
        print("\t\t\t Welcome To Our Docker Services")
        print("\t\t\t ------------------------------")
        os.system("tput setaf 7")
        os.system("tput setaf 2")
        print("""
            Press 1: To Configure Docker
            Press 2: To Pull Docker Image
            Press 3: To List Containers
            Press 4: To Remove All Containers
            Press 5: To Configure Web Server on Docker
            Press 6: To Launch GUI Program in Docker
            Press 7: To Select Another Technology
            """)
        print("\n")
        os.system('tput setaf 3')
        ch = int(input("Enter your choice:- "))
        if ch == 1:
            Config_Docker()
        elif ch == 2:
            os.system('tput setaf ')
            img = input("Enter the name of image:- ")
            os.system('tput setaf 7')
            os.system('docker pull {0}'.format(img))
        elif ch == 3:
            os.system('docker ps -a')
            input()
        elif ch == 4:
            os.system("docker rm -f $(docker ps -aq)")
        elif ch == 5:
            Config_Web()
        elif ch == 6:
            Docker_GUI()
        elif ch == 7:
            break
        else:
            print('Enter a valid choice')
            input()


