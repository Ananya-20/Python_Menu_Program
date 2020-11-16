import os

def HadoopMenu():
    os.system("clear")
    os.system("tput setaf 1")
    print("Welcome To Hadoop...")
    os.system("tput setaf 2")
    print("""
      Press 1: For Configuring Name(Master) Node
      Press 2: For Configuring Data Node
      Press 3: To go back to the main menu
      """)
    os.system("tput setaf 3")
    ch = int(input('Enter your choice'))
    os.system("tput setaf 7")
    if ch == 1:
        print("\nconfiguring Master Node\n")	       
        ing=input("Enter Machine IP")
        os.system("scp jdk-8u171-linux-x64.rpm {}:/".format(ing))	    
        os.system("ssh {} rpm -i /jdk-8u171-linux-x64.rpm".format(ing))
        os.system("scp hadoop-1.2.1-1.x86_64.rpm {}:/".format(ing))
        os.system("ssh {} rpm -i /hadoop-1.2.1-1.x86_64.rpm --force".format(ing))
        os.system("ssh {} jps".format(ing))
        os.system("mkdir {} /nam".format(ing))
        os.system("scp hdfs-site.xml {}:/etc/hadoop/hdfs-site.xml".format(ing))
       	os.system("scp core-site.xml {}:/etc/hadoop/core-site.xml".format(ing))
        os.system("ssh {} hadoop namenode -format".format(ing))
        os.system("ssh {} hadoop-daemon.sh start namenode".format(ing))
        os.system("ssh {} jps".format(ing))
		
    elif ch == 2:
        print("\nConfiguring Slave Node\n")
       	ing=input("Enter Machine IP")
       	os.system("scp jdk-8u171-linux-x64.rpm {}:/".format(ing))
       	os.system("ssh {} rpm -i /jdk-8u171-linux-x64.rpm".format(ing))
       	os.system("scp hadoop-1.2.1-1.x86_64.rpm {}:/".format(ing))
       	os.system("ssh {} rpm -i /hadoop-1.2.1-1.x86_64.rpm --force".format(ing))
       	os.system("ssh {} jps".format(ing))
       	os.system("mkdir {} /data".format(ing))
       	os.system("scp /home/Ganesh/hdfs-site.xml {}:/etc/hadoop/hdfs-site.xml".format(ing))
       	os.system("scp /home/Ganesh/core-site.xml {}:/etc/hadoop/core-site.xml".format(ing))
        os.system("ssh {} hadoop-daemon.sh start datanode".format(ing))        	
        os.system("ssh {} jps".format(ing))
     
    elif ch == 3:
        pass          
    else:
        print("Enter valid choice")
