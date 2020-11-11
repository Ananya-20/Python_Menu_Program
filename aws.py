import os
def AWS_Menu():
    while True:
        os.system("clear")
        os.system("tput setaf 1")
        print("\t\t\t -----------------------")    
        print("\t\t\t Welcome To AWS Services")
        print("\t\t\t -----------------------")
        os.system("tput setaf 7")
        os.system("tput setaf 2")
        print("""
            Press 1: To Configure AWS 
            Press 2: To Create a Key Pair
            Press 3: To Create Security Group 
            Press 4: To Launch Instance
            Press 5: To Describe Instance
            Press 6: To Create an EBS Volume
            Press 7: To Attach EBS to an Instance
            Press 8: Create S3 Object
            Press 9: Upload Object on S3 Bucket
            Press 10: Exit
            """)
        print()
        os.system("tput setaf 3")
        ch = int(input("Enter your choice:- "))
        os.system("tput setaf 7")
        if ch == 1:
            print()
            os.system("aws configure")
            os.system("tput setaf 3")
            input("Press enter to continue")
            os.system("tput setaf 7")
        elif ch == 2:
            os.system("tput setaf 3")
            KeyName = input("Enter key-pait name:- ")
            os.system("tput setaf 7")
            os.system("aws ec2 create-key-pair --keyname {}".format(KeyName))
            os.system("tput setaf 3")
            input("Press enter to continue")
            os.system("tput setaf 7")
        elif ch == 3:
            print()
            os.system("tput setaf 3")
            sg_name = input("Enter Security Group Name:- ")
            sg_desc = input("Enter the description:- ")
            os.system("aws ec2 create-security-group --group-name {0} --description {1} ".format(sg_name,sg_desc))
            print("Add rule to the security group")
            protocol = input("Enter the protocol- ")
            port = input("Enter the port number:- ")
            cidr = input("Enter the CIDR:- ")
            os.system("aws ec2 authorize-security-group-ingress --group-name {0} --protocol {1} --port {2} --cidr {3}".format(sg_name,protocol,port,cidr))
input("Press enter to continue")




