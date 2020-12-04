#!/usr/bin/python3

import os
import getpass
import fileinput
import subprocess

os.system("clear")
os.system("tput setaf 14")
print ("\t\t\t Welcome to Menu!!!")
os.system("tput setaf 12")
print("\t\t\t-----------------------")

passwd = getpass.getpass("Enter password")
if passwd != "divya":
	print("password incorrect")
	exit()

dnf sysop1():
  while True:
      os.system("tput setaf 2")
      os.system("\n\t\t\tfiglet -t -k system operations \n\n\n")
      print("""
      \n
      System Operations for local system:
      -----------------------------------
      Press 1: Date
      Press 2: Calender
      Press 3: System configuration settings
      Press 4: View system profile
      Press 5: To install a package
      Press 6: To see a package info 
      Press 7: Check service status
      Press 8: Veiw installed software
      Press 9: Veiw a software info
      Press 10: Add new user
      Press 11: Delete a user
      Press 12: Create directory
      Press 13: To start a service
      Press 14: To stop a service
      Press 15: Back to main menu
      """)
      ch = int(input("Enter your choice:\t"))
      os.system("tput setaf 15")

      if ch == 1:
        os.system("date")
	i = input("do you want to continue on system menu [y/n]:\t")
        if i != 'y':
          break
	
      elif ch == 2:
        os.system("cal")
	i = input("do you want to continue on system menu [y/n]:\t")
        if i != 'y':
          break
	
      elif ch == 3:
        os.system("gnome-control-center")
        i = input("do you want to continue on system menu [y/n]:\t")
        if i != 'y':
          break

      elif ch == 4:
        os.system("lscpu")
	i = input("do you want to continue on system menu [y/n]:\t")
        if i != 'y':
          break

      elif ch == 5:
        name = input("enter package name:")
        os.system("yum install {} -y".format(name))
        i = input("do you want to continue on system menu [y/n]:\t")
        if i != 'y':
          break

      elif ch == 6:
        name = input ("enter package name:")
        os.system("yum info {}".format(name))
	i = input("do you want to continue on system menu [y/n]:\t")
        if i != 'y':
          break
  
      elif ch == 7:
        num = input ("enter the service name:")
        os.system("systemctl status {}".format(num))
	i = input("do you want to continue on system menu [y/n]:\t")
        if i != 'y':
          break
  
      elif ch == 8:
        os.system("rpm -qa")
	i = input("do you want to continue on system menu [y/n]:\t")
        if i != 'y':
          break
  
      elif ch == 9:
        name = input ("enter software name:")
        os.system("yum info {}".format(name))
	i = input("do you want to continue on system menu [y/n]:\t")
        if i != 'y':
          break
  
      elif ch == 10:
        new_uswer = input ("enter name of the new user:")
        os.system("sudo useradd {}".format(new_user))
        os.system("id -u {}".format(new_user))
	i = input("do you want to continue on system menu [y/n]:\t")
        if i != 'y':
          break
  
      elif ch == 11:
        name = input ("name the user:")
        os.system("sudo userdel {}".format(name))
	i = input("do you want to continue on system menu [y/n]:\t")
        if i != 'y':
          break
    
      elif ch == 12:       
        name=input("name your directory :")
        os.system("mkdir /{}".format(name))
	i = input("do you want to continue on system menu [y/n]:\t")
        if i != 'y':
          break
	
      elif ch == 13:       
        name=input("name of the service :")
        os.system("systemctl start {}".format(name))
	i = input("do you want to continue on system menu [y/n]:\t")
        if i != 'y':
          break
	
      elif ch == 14:       
        name=input("name of the service :")
        os.system("systemctl stop {}".format(name))
	i = input("do you want to continue on system menu [y/n]:\t")
        if i != 'y':
          break
      
      elif ch == 15:
        break
	
dnf sysop2():
  while True:
      os.system("tput setaf 2")
      os.system("\n\t\t\tfiglet -t -k system operations \n\n\n")
      print("""
      \n
      System Operations for remote system:
      -----------------------------------
      Press 1: Date
      Press 2: Calender
      Press 3: System configuration settings
      Press 4: View system profile
      Press 5: To install a package
      Press 6: To see a package info 
      Press 7: Check service status
      Press 8: Veiw installed software
      Press 9: Veiw a software info
      Press 10: Add new user
      Press 11: Delete a user
      Press 12: Create directory
      Press 13: To start a service
      Press 14: To stop a service
      Press 15: Back to main menu
      """)
      ch1 = int(input("Enter your choice:\t"))
      os.system("tput setaf 15")

      if ch1 == 1:
        ip = input("Enter the ip of the system:\t")
        os.system("ssh {} date".format(ip))
	i = input("do you want to continue on system menu [y/n]:\t")
        if i != 'y':
          break
	
      elif ch1 == 2:
        ip = input("Enter the ip of the system:\t")
        os.system("ssh {} cal".format(ip))
	i = input("do you want to continue on system menu [y/n]:\t")
        if i != 'y':
          break
	
      elif ch1 == 3:
        ip = input("Enter the ip of the system:\t")
        os.system("ssh {} gnome-control-center".format(ip))
        i = input("do you want to continue on system menu [y/n]:\t")
        if i != 'y':
          break

      elif ch1 == 4:
        ip = input("Enter the ip of the system:\t")
        os.system("ssh {} lscpu".format(ip))
	i = input("do you want to continue on system menu [y/n]:\t")
        if i != 'y':
          break

      elif ch1 == 5:
        ip = input("Enter the ip of the system:\t")
        name = input("enter package name:")
        os.system("ssh {} yum install {} -y".format(ip, name))
        i = input("do you want to continue on system menu [y/n]:\t")
        if i != 'y':
          break

      elif ch1 == 6:
        ip = input("Enter the ip of the system:\t")
        name = input ("enter package name:")
        os.system("ssh {} yum info {}".format(ip, name))
	i = input("do you want to continue on system menu [y/n]:\t")
        if i != 'y':
          break
  
      elif ch1 == 7:
        ip = input("Enter the ip of the system:\t")
        num = input ("enter the service name:")
        os.system("ssh {} systemctl status {}".format(ip, num))
	i = input("do you want to continue on system menu [y/n]:\t")
        if i != 'y':
          break
  
      elif ch1 == 8:
        ip = input("Enter the ip of the system:\t")
        os.system("ssh {} rpm -qa".format(ip))
	i = input("do you want to continue on system menu [y/n]:\t")
        if i != 'y':
          break
  
      elif ch1 == 9:
        ip = input("Enter the ip of the system:\t")
        name = input ("enter software name:")
        os.system("ssh {} yum info {}".format(ip, name))
	i = input("do you want to continue on system menu [y/n]:\t")
        if i != 'y':
          break
  
      elif ch1 == 10:
        ip = input("Enter the ip of the system:\t")
        new_uswer = input ("enter name of the new user:")
        os.system("ssh {} sudo useradd {}".format(ip, new_user))
        os.system("ssh {} id -u {}".format(ip, new_user))
	i = input("do you want to continue on system menu [y/n]:\t")
        if i != 'y':
          break
  
      elif ch1 == 11:
        ip = input("Enter the ip of the system:\t")
        name = input ("name the user:")
        os.system("ssh {} sudo userdel {}".format(ip, name))
	i = input("do you want to continue on system menu [y/n]:\t")
        if i != 'y':
          break
    
      elif ch1 == 12: 
        ip = input("Enter the ip of the system:\t")
        name=input("name your directory :")
        os.system("ssh {} mkdir /{}".format(ip, name))
	i = input("do you want to continue on system menu [y/n]:\t")
        if i != 'y':
          break
	
      elif ch1 == 13:
        ip = input("Enter the ip of the system:\t")
        name=input("name of the service :")
        os.system("ssh {} systemctl start {}".format(ip, name))
	i = input("do you want to continue on system menu [y/n]:\t")
        if i != 'y':
          break
	
      elif ch1 == 14:
        ip = input("Enter the ip of the system:\t")
        name=input("name of the service :")
        os.system("ssh {} systemctl stop {}".format(ip, name))
	i = input("do you want to continue on system menu [y/n]:\t")
        if i != 'y':
          break
      
      elif ch1 == 15:
        break
	
dnf docker1():
  while True:
      os.system("tput setaf 2")
      os.system("\n\t\t\tfiglet -t -k docker menu \n\n\n")
      print("""
      \n
      Docker for local system:
      -------------------------
      Press 1: Install and Configure Docker
      Press 2: List Docker images stored locally
      Press 3: Pull an image from registry
      Press 4: Push an image to registry
      Press 5: Delete an image from local image store
      Press 6: Build an image from dockerfile
      Press 7: Run a container from docker image
      Press 8: List the networks
      Press 9: List the running containers
      Press 10: Delete all containers
      Press 11: Go back to main menu
      """)

      di = int(input("Enter your choice:\t"))
      os.system("tput setaf 15")

      if di == 1:
        with open("/etc/tum.repos.d/baseforyum.repo", "w") as d:
            d.write("[cde1]\nbaseurl = file:///run/media/root/RHEL-8-0-0-BaseOS-x86_64/AppStream\ngpgcheck=0\n\n[cde2]\nbaseurl =file:///run/media/root/RHEL-8-0-0-BaseOS-x86_64/BaseOS\ngpgcheck=0\n")
        os.system("sudo yum -y install https://dl.fedoraproject.org/pub/epel/epel-release-latest-8.noarch.rpm")
        os.system("sudo yum update")
        os.system("yum -y install docker-ce --nobest")
        os.system("systemctl start docker")
        os.system("systemctl enable docker")
        i = input("do you want to continue on docker menu [y/n]:\t")
        if i != 'y':
          break

      elif di == 2:
        os.system("docker image ls")
        i = input("do you want to continue on docker menu [y/n]:\t")
        if i != 'y':
          break
  
      elif di == 3:
        name = input ("enter image name with version:")
        os.system("docker pull {}".format(name))
        i = input("do you want to continue on docker menu [y/n]:\t")
        if i != 'y':
          break

      elif di == 4:
        name = input ("enter image name: ")
        os.system("docker push {}".format(name))
        i = input("do you want to continue on docker menu [y/n]:\t")
        if i != 'y':
          break
	
      elif di == 5:
        name = input ("enter image name:")
        os.system("docker image rm {}".format(name))
        i = input("do you want to continue on docker menu [y/n]:\t")
        if i != 'y':
          break
  
      elif di == 6:
        name = input ("enter image name:")
        os.system("docker build -t {}".format(name))
        i = input("do you want to continue on docker menu [y/n]:\t")
        if i != 'y':
          break
  
      elif di == 7:
        img_name = input ("enter name of the image:")
        port = input ("enter port:")
        con_name = input ("enter container name:")
        os.system("docker container run --name {} -p {} {}".format(con_name, port, img_name))
        i = input("do you want to continue on docker menu [y/n]:\t")
        if i != 'y':
          break
  
      elif di == 8:
        os.system("docker network ls")
        i = input("do you want to continue on docker menu [y/n]:\t")
        if i != 'y':
          break
  
      elif di == 9:
        os.system("docker container ls")
        i = input("do you want to continue on docker menu [y/n]:\t")
        if i != 'y':
          break
  
      elif di == 10:
        os.system("docker container rm -f $(docker ps -aq)")
        i = input("do you want to continue on docker menu [y/n]:\t")
        if i != 'y':
          break
  
      elif di == 11:
         break
	
dnf docker2():
  while True:
      os.system("tput setaf 2")
      os.system("\n\t\t\tfiglet -t -k docker menu \n\n\n")
      print("""
      \n
      Docker for remote system:
      -------------------------
      Press 1: Install and Configure Docker
      Press 2: List Docker images stored locally
      Press 3: Pull an image from registry
      Press 4: Push an image to registry
      Press 5: Delete an image from local image store
      Press 6: Build an image from dockerfile
      Press 7: Run a container from docker image
      Press 8: List the networks
      Press 9: List the running containers
      Press 10: Delete all containers
      Press 11: Go back to main menu
      """)

      di1 = int(input("Enter your choice:\t"))
      os.system("tput setaf 15")

      if di1 == 1:
        ip = input("Enter the ip of the system:\t")
        os.system("ssh {} sudo yum -y install https://dl.fedoraproject.org/pub/epel/epel-release-latest-8.noarch.rpm".format(ip))
        os.system("ssh {} sudo yum update".format(ip))
        os.system("ssh {} yum -y install docker-ce --nobest".format(ip))
        os.system("ssh {} systemctl start docker".format(ip))
        os.system("ssh {} systemctl enable docker".format(ip))
        i = input("do you want to continue on docker menu [y/n]:\t")
        if i != 'y':
          break

      elif di1 == 2:
        ip = input("Enter the ip of the system:\t")
        os.system("ssh {} docker image ls".format(ip))
        i = input("do you want to continue on docker menu [y/n]:\t")
        if i != 'y':
          break
  
      elif di1 == 3:
        ip = input("Enter the ip of the system:\t")
        name = input ("enter image name with version(name:version):")
        os.system("ssh {} docker pull {}".format(ip, name))
        i = input("do you want to continue on docker menu [y/n]:\t")
        if i != 'y':
          break

      elif di1 == 4:
        ip = input("Enter the ip of the system:\t")
        name = input ("enter image name: ")
        os.system("ssh {} docker push {}".format(ip, name))
        i = input("do you want to continue on docker menu [y/n]:\t")
        if i != 'y':
          break
	
      elif di1 == 5:
        ip = input("Enter the ip of the system:\t")
        name = input ("enter image name:")
        os.system("ssh {} docker image rm {}".format(name))
        i = input("do you want to continue on docker menu [y/n]:\t")
        if i != 'y':
          break
  
      elif di1 == 6:
        ip = input("Enter the ip of the system:\t")
        name = input ("enter image name:")
        os.system("ssh {} docker build -t {}".format(name))
        i = input("do you want to continue on docker menu [y/n]:\t")
        if i != 'y':
          break
  
      elif di1 == 7:
        ip = input("Enter the ip of the system:\t")
        img_name = input ("name the image:")
        port = input ("enter port:")
        con_name = input ("enter container name:")
        os.system("ssh {} docker container run --name {} -p {} {}".format(ip, con_name, port, img_name))
        i = input("do you want to continue on docker menu [y/n]:\t")
        if i != 'y':
          break
  
      elif di1 == 8:
        ip = input("Enter the ip of the system:\t")
        os.system("ssh {} docker network ls".format(ip))
        i = input("do you want to continue on docker menu [y/n]:\t")
        if i != 'y':
          break
  
      elif di1 == 9:
        ip = input("Enter the ip of the system:\t")
        os.system("ssh {} docker container ls".format(ip))
        i = input("do you want to continue on docker menu [y/n]:\t")
        if i != 'y':
          break
  
      elif di1 == 10:
        ip = input("Enter the ip of the system:\t")
        os.system("ssh {} docker container rm -f $(docker ps -aq)".format(ip))
        i = input("do you want to continue on docker menu [y/n]:\t")
        if i != 'y':
          break
  
      elif di1 == 11:
         break
	
	
dnf lvm():
  while True:
      os.system("tput setaf 2")
      os.system("\n\t\t\tfiglet -t -k lvm menu \n\n\n")
      print("""
      \n
      Logical Volume Management Operations:
      -------------------------------------
      
      Press 1: To get all partitions information in one disk.
      Press 2: To format the partition.
      Press 3: To mount the partition to the directory.
      Press 4: To unmount the partition.
      Press 5: To get details of size and mount point of the disk.
      Press 6: To create Physical volume
      Press 7: To display PV information
      Press 8: To create Volume Group
      Press 9: To display VG information.
      Press 10: To create logical volume
      Press 11: To display LV information
      Press 12: To extend the size of LV
      Press 13: To reduce the size of LV
      Press 14: Go back to main menu
      """)

      vm = int(input("Enter your choice:\t"))
      os.system("tput setaf 15")

      
      if vm == 1:
        d_name = input("Enter the disk name:")
        os.system("fdisk -l {}".format(d_name))
        i = input("do you want to continue on lvm menu [y/n]:\t")
        if i != 'y':
          break
      
      elif vm ==2:
        part=input("Enter the partition name(e.g. /dev/sdb1): ")
        os.system("mkfs.ext4 {}".format(part))
        i = input("do you want to continue on lvm menu [y/n]:\t")
        if i != 'y':
          break
      
      elif vm == 3:
        folder_name=input("Enter the folder name on which you want to mount the partition. ")
        part_name = input("Enter the formatted partition full name: ")
        os.system("mount {} {}".format(part_name, folder_name))
        i = input("do you want to continue on lvm menu [y/n]:\t")
        if i != 'y':
          break
      
      elif vm == 4:
        folder_name=input("Enter the folder name on which you want to unmount the partition. ")
        part_name = input("Enter the partition full name: ")
        return os.system("umount {} {}".format(part_name, folder_name))
        i = input("do you want to continue on lvm menu [y/n]:\t")
        if i != 'y':
          break
      
      elif vm == 5:
        os.system("df -h")
        i = input("do you want to continue on lvm menu [y/n]:\t")
        if i != 'y':
          break

      elif vm == 6:
        disk_name=input("Enter the disk name :")
        os.system("pvcreate {}".format(disk_name))
        i = input("do you want to continue on lvm menu [y/n]:\t")
        if i != 'y':
          break
    
      elif vm == 7:
        disk_name=input("Enter the disk name :")
        os.system("pvdisplay {}".format(disk_name))
        i = input("do you want to continue on lvm menu [y/n]:\t")
        if i != 'y':
          break
    
      elif vm == 8:
        pv1=input("Enter first PV name:")
        pv2=input("Enter second PV name:")
        vg=input("Enter the name of the VG:")
        os.system("vgcreate {} {} {}".format(pv1, pv2, vg))
        i = input("do you want to continue on lvm menu [y/n]:\t")
        if i != 'y':
          break
    
      elif vm == 9:
        vg=input("Enter the VG name:")
        os.system("vgdisplay {}".format(vg))
        i = input("do you want to continue on lvm menu [y/n]:\t")
        if i != 'y':
          break
    
      elif vm == 10:
        size=input("Enter the size of the Logical volume(e.g. 8G):")
        vg=input("Enter the name of the VG:")
        lv=input("Enter the name of the Logical volume:")
        os.system("lvcreate --size {} --name {} {}".format(size, lv, vg))
        i = input("do you want to continue on lvm menu [y/n]:\t")
        if i != 'y':
          break
    
      elif vm == 11:
        lv=input("Enter the name of the Logical volume:")
        vg=input("Enter the name of the VG:")
        os.system("lvdisplay {}/{}".format(vg, lv))
        i = input("do you want to continue on lvm menu [y/n]:\t")
        if i != 'y':
          break

      elif vm == 12:
        lv=input("Enter the name of the Logical volume:")
        size=input("How much size you want to extend(e.g. 8G):")
        os.system("lvextend --size +{} {}".format(size, lv))
        os.system("resize2fs {}".format(lv))
        i = input("do you want to continue on lvm menu [y/n]:\t")
        if i != 'y':
          break
    
      elif vm == 13:
        lv=input("Enter the name of the Logical volume:")
        size=input("How much size you want to reduce(e.g. 8G):")
        os.system("lvreduce --size -{} {}".format(size, lv))
        os.system("resize2fs {}".format(lv))
        i = input("do you want to continue on lvm menu [y/n]:\t")
        if i != 'y':
          break
    
      elif vm == 14:
        break()
	
dnf aws():
  while True:
      os.system("tput setaf 2")
      os.system("\n\t\t\tfiglet -t -k aws menu \n\n\n")
      print("""
      \n
      AWS Menu:
      ----------
      Press 1: To install aws cli software
      Press 2: Create a key-pair  
      Press 3: Create security-group
      Press 4: Launch EC2 instance
      Press 5: Describe EC2 instances
      Press 6: Create and attach a volume to EC2 instance
      Press 7: Create a S3 bucket
      Press 8: Upload objects in S3 bucket
      Press 9: Lunch a cloudfront
      Press 10: Configure cli for iam user
      Press 11: Back to main menu
      """)
      as = int(input("Enter your choice:\t"))
      os.system("tput setaf 15")

      if as == 1:
        os.system("curl 'https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip' -o 'awscliv2.zip'")
        os.system("unzip awscliv2.zip")
        os.system("sudo ./aws/install")
        os.system("aws --version")
        i = input("do you want to continue on aws menu [y/n]:\t")
        if i != 'y':
          break
 
      elif as == 2:
        name = input ("enter key-pair name:")
        os.system("aws ec2 create-key-pair --key-name {}".format(name))
        i = input("do you want to continue on aws menu [y/n]:\t")
        if i != 'y':
          break
  
      elif as == 3:
        name = input ("enter security groupe name:")
        des=input("Write description:")
        os.system("aws ec2 create-security-group --group-name {} --description {}".format(name,des))
        i = input("do you want to continue on aws menu [y/n]:\t")
        if i != 'y':
          break
  
      elif as == 4:
        name = input ("enter image id:")
        sg=input("Security group id:")
        subnet= input("Subnet id:")
        key= input("key name:")
        os.system("aws ec2 run-instances --image-id {} --instance-type t2.micro --security-group-ids {} --subnet-id {} --key-name {}".format(name,sg,subnet,key))
        i = input("do you want to continue on aws menu [y/n]:\t")
        if i != 'y':
          break
	
      elif aws_input == 5:
        os.system("aws ec2  describe-instances")
        i = input("do you want to continue on aws menu [y/n]:\t")
        if i != 'y':
          break
  
      elif as == 6:
        az = input ("enter availability zone:")
        vtype=input("Volume type:")
        insid=input("enter instance id to which you want to attach")
        vid= input("Enter volume id which is to be attached")	
        os.system("aws ec2 create-volume --availability-zone {} --size 1 --volume-type {}".format(az, vtype))
        os.system("aws ec2 attach-volume --device xvdh --instance-id {} --volume-id {}".format(insid, vid))
        i = input("do you want to continue on aws menu [y/n]:\t")
        if i != 'y':
          break
	
      elif as == 7:
        bucket_name=input("give an identical bucket name:\t")
        os.system("aws s3api create-bucket --bucket {} --region ap-south-1 --acl public-read --create-bucket-configuration LocationConstraint=ap-south-1".format(bucket_name))
        i = input("do you want to continue on aws menu [y/n]:\t")
        if i != 'y':
          break 

      elif as == 8:
        print("Available s3 bucket: " )
        os.system("aws s3 ls")
        bucket_name=input("give bucket name where you want to upload the object:\t")
        object_name=input("give the full path of the file which you want to upload:\t")
        os.system("aws s3 cp {} s3://{}/".format(object_name,bucket_name))
        i = input("do you want to continue on aws menu [y/n]:\t")
        if i != 'y':
          break

      elif as == 9:
        bucket_name=input("buket name for cloudfront:\t")
        os.system("aws cloudfront create-distribution --origin-domain-name {}.s3.amazonaws.com".format(bucket_name))
        i = input("do you want to continue on aws menu [y/n]:\t")
        if i != 'y':
          break
	
      elif as == 10:
        name = input("provide name to the aws user:\t")
        os.system("aws configure --profile  {}".format(name))
        os.system("aws configure list-profiles")
        i = input("do you want to continue on aws menu [y/n]:\t")
        if i != 'y':
          break

      elif as == 11:
        break()
	



dnf webserver():
  while True:
      os.system("tput setaf 2")
      os.system("\n\t\t\tfiglet -t -k webserver menu \n\n\n")
      print("""
      \n
      Webserver Menu:
      ----------------
      Press 1: Configure yum locally
      Press 2: Configure yum remotely
      Press 3: Install webserver in local system
      Press 4: Start webserver services in local sysem
      Press 5: Stop webserver services in local system
      Press 6: Install webserver in remote system
      Press 7: Start webserver services in remote sysem
      Press 8: Stop webserver services in remote system
      Press 9: Back to main menu
      """)
      web = int(input("Enter your choice:\t"))
      os.system("tput setaf 15")
      
      if web == 1:
        with open("/etc/yum.repos.d/base2.repo", "w") as f:
            f.write("[cde1]\nbaseurl = file:///run/media/root/RHEL-8-0-0-BaseOS-x86_64/AppStream\ngpgcheck=0\n\n[cde2]\nbaseurl =file:///run/media/root/RHEL-8-0-0-BaseOS-x86_64/BaseOS\ngpgcheck=0\n")
        i = input("do you want to continue on webserver menu [y/n]:\t")
        if i != 'y':
            break
	
      elif web == 2:
        ip = input("Enter the ip of the system :\t")
        with open("/root/base2.repo", "w") as f:
            f.write("[cde1]\nbaseurl = file:///run/media/root/RHEL-8-0-0-BaseOS-x86_64/AppStream\ngpgcheck=0\n\n[cde2]\nbaseurl =file:///run/media/root/RHEL-8-0-0-BaseOS-x86_64/BaseOS\ngpgcheck=0\n")
        os.system("scp  cp /root/base2.repo  {}:/etc/yum.repos.d/ ".format(ip))
        os.system("rm -f /root/base2.repo")
        i = input("do you want to continue on webserver menu [y/n]:\t")
        if i != 'y':
           break
	
      elif web == 3:
        os.system("yum install httpd -y")
        i = input("do you want to continue on webserver menu [y/n]:\t")
        if i != 'y':
           break
	
      elif web == 4:
        os.system("systemctl start httpd")
        os.system("systemctl enable httpd")
        i = input("do you want to continue on webserver menu [y/n]:\t")
        if i != 'y':
           break
	
      elif web == 5:
        os.system("systemctl stop httpd")
        i = input("do you want to continue on webserver menu [y/n]:\t")
        if i != 'y':
           break

      elif web == 6:
        ip = input("Enter the ip of the system :\t")
        os.system("ssh {} yum install httpd -y".format(ip))
        i = input("do you want to continue on webserver menu [y/n]:\t")
        if i != 'y':
            break

      elif web == 7:
        ip = input("Enter the ip of the system:\t")
        os.system("ssh {}  systemctl start httpd".format(ip))
        os.system("ssh {}  systemctl enable httpd".format(ip))
        i = input("do you want to continue on webserver menu [y/n]:\t")
        if i != 'y':
             break

        elif web == 8:
          ip = input("Enter the ip of the system :\t")
          os.system("systemctl stop httpd".format(ip))
          i = input("do you want to continue on webserver menu [y/N]:\t")
          if i != 'y':
              break
	
def hadoop():
  while True:
    os.system("clear")
    os.system("tput setaf 2")
    os.system("\t\t\tfiglet -t -k Hadoop  cluster")
    print("""
    1. Installing Hadoop.
    2. Creating Master in hadoop cluster.
    3. Creating Datanode in hadoop cluster.
    4. Creating Client in hadoop cluster.
    5. Limit The Data Node Storage.
    6. Upload data into the hadoop cluster.
    7. Read Data from Hadoop Cluster.
    8. List all the files.
    9. Delete Client Data.
    10. Stop Name Node.
    11. Stop Data Node.
    12. Converting the role of local system in the hadoop cluster.
    13. To go back to the main menu""")
    choice_hadoop = int(input("give your choice:\t"))
    os.system("tput setaf 15")
    if choice_hadoop == 1:
          print("""
press 1: For installing hadoop locally
press 2: For installing hadoop remotely 
""")
          insta = int(input("Enter you choice:\t"))
          if  insta == 1:
              os.system("rpm -ivh /root/jdk-8u171-linux-x64.rpm ")
              os.system("rpm -ivh /root/hadoop-1.2.1-1.x86_64.rpm  --force")
              print("\nHadoop Requirements Sucessfully Installed")
          elif insta == 2:
              sip = input("Enter the ip in which you want to install hadoop:\t")
              os.system('scp  /root/jdk-8u171-linux-x64.rpm  {}:/root/'.format(sip))
              os.system('scp  /root/hadoop-1.2.1-1.x86_64.rpm {}:/root/'.format(sip))
              os.system("ssh {} rpm -ivh /root/jdk-8u171-linux-x64.rpm ".format(sip))
              os.system("ssh {} rpm -ivh /root/hadoop-1.2.1-1.x86_64.rpm  --force".format(sip))
              print("\nHadoop Requirements Sucessfully Installed")
          i = input("do you want to continue on Hadoop menu [y/N]:\t")
          if i != 'y' and i!= 'Y':
                    break
		

    elif choice_hadoop == 2:
          print("press 1 : For making the local system Namenode")
          print("press 2 : For making Datanode by ssh")
          datan = int(input("Enter your choice:\t"))
          if datan == 1:
                 add_master()
          elif datan == 2:
           sip = input("Enter Name Node IP : \t")
           sshd = input("Enter your Data Node directory name : \t")
           os.system("ssh {} mkdir {}".format(sip,sshd))
           print("Configuring hdfs-site.xml file ............")
           os.system("echo -e '<?xml version=\"1.0\"?> \n<?xml-stylesheet type=\"text/xsl\" href=\"configuration.xsl\"?>' > /root/hdfs-site.xml")
           os.system("echo -e '\n<!-- Put site-specific property overrides in this file. -->' >> /root/hdfs-site.xml")
           os.system('echo -e "\n<configuration>" >> /root/hdfs-site.xml')
           os.system('echo -e "\n<property>" >> /root/hdfs-site.xml')
           os.system('echo -e "\n<name>dfs.name.dir</name>" >> /root/hdfs-site.xml')
           os.system('echo -e "\n<value>{}</value>" >> /root/hdfs-site.xml'.format(sshd))
           os.system('echo -e "\n</property>" >> /root/hdfs-site.xml')
           os.system('echo -e "\n</configuration>" >> /root/hdfs-site.xml')
           os.system('scp  /root/hdfs-site.xml  {}:/etc/hadoop/'.format(sip))
           os.system('rm -rf /root/hdfs-site.xml')
           print("\nFormatting the Name Node ..............................")
           os.system('ssh {} hadoop namenode -format'.format(sip))
           nip = input("Enter  IP of which you want to start your hadoop master:")
           print("\t\t\t\tConfiguring core-site.xml file ...........")
           os.system("echo -e '<?xml version=\"1.0\"?> \n<?xml-stylesheet type=\"text/xsl\" href=\"configuration.xsl\"?>' > /root/core-site.xml")
           os.system('echo -e "\n<!-- Put site-specific property overrides in this file. -->" >> /root/core-site.xml')
           os.system('echo -e "\n<configuration>" >> /root/core-site.xml')
           os.system('echo -e "\n<property>" >> /root/core-site.xml')
           os.system('echo -e "\n<name>fs.default.name</name>" >> /root/core-site.xml')
           os.system('echo -e "\n<value>hdfs://{}:9001</value>" >> /root/core-site.xml'.format(nip))
           os.system('echo -e "\n</property>" >> /root/core-site.xml')
           os.system('echo -e "\n</configuration>" >> /root/core-site.xml')
           os.system('scp  /root/core-site.xml  {}:/etc/hadoop/'.format(sip))
           os.system('rm -rf /root/core-site.xml')
           os.system("ssh {} hadoop-daemon.sh start namenode".format(sip))
           print("Now the hadoop master servicee start you can check it by jps command")
           print("ssh {} jps".format(sip))
                 
          i = input("do you want to continue on Hadoop menu [y/N]:\t")
          if i != 'y' and i!= 'Y':
                    break

    elif choice_hadoop == 3:
          print("press 1 : For making the local system Datanode")
          print("press 2 : For making Datanode by ssh")
          datan = int(input("Enter your choice:\t"))
          if datan == 1:
                 add_slave()
          elif datan == 2:
           sip = input("Enter Data Node IP : \t")
           sshd = input("Create Data Node directory name remotely : \t")
           os.system("ssh {} mkdir {}".format(sip,sshd))
           print("Configuring hdfs-site.xml file ............")
           os.system("echo -e '<?xml version=\"1.0\"?> \n<?xml-stylesheet type=\"text/xsl\" href=\"configuration.xsl\"?>' > /root/hdfs-site.xml")
           os.system("echo -e '\n<!-- Put site-specific property overrides in this file. -->' >> /root/hdfs-site.xml")
           os.system('echo -e "\n<configuration>" >> /root/hdfs-site.xml')
           os.system('echo -e "\n<property>" >> /root/hdfs-site.xml')
           os.system('echo -e "\n<name>dfs.data.dir</name>" >> /root/hdfs-site.xml')
           os.system('echo -e "\n<value>{}</value>" >> /root/hdfs-site.xml'.format(sshd))
           os.system('echo -e "\n</property>" >> /root/hdfs-site.xml')
           os.system('echo -e "\n</configuration>" >> /root/hdfs-site.xml')
           os.system('scp  /root/hdfs-site.xml  {}:/etc/hadoop/'.format(sip))
           os.system('rm -rf /root/hdfs-site.xml')
           nip = input("Enter Name Node IP :")
           print("\t\t\t\tConfiguring core-site.xml file ...........")
           os.system("echo -e '<?xml version=\"1.0\"?> \n<?xml-stylesheet type=\"text/xsl\" href=\"configuration.xsl\"?>' > /root/core-site.xml")
           os.system('echo -e "\n<!-- Put site-specific property overrides in this file. -->" >> /root/core-site.xml')
           os.system('echo -e "\n<configuration>" >> /root/core-site.xml')
           os.system('echo -e "\n<property>" >> /root/core-site.xml')
           os.system('echo -e "\n<name>fs.default.name</name>" >> /root/core-site.xml')
           os.system('echo -e "\n<value>hdfs://{}:9001</value>" >> /root/core-site.xml'.format(nip))
           os.system('echo -e "\n</property>" >> /root/core-site.xml')
           os.system('echo -e "\n</configuration>" >> /root/core-site.xml')
           os.system('scp  /root/core-site.xml  {}:/etc/hadoop/'.format(sip))
           os.system('rm -rf /root/core-site.xml')
           os.system("ssh {} hadoop-daemon.sh start datanode".format(sip))
           print("Now the hadoop slave services start you can check it by jps command")
           os.system("ssh {} jps".format(sip))
          i = input("do you want to continue on Hadoop menu [y/N]:\t")
          if i != 'y' and i!= 'Y':
                    break

    elif choice_hadoop == 4:
          print("press 1 : For making the local system Client")
          print("press 2 : For making Client by ssh")
          datan = int(input("Enter your choice:\t"))
          if datan == 1:
                 add_client()
          elif datan == 2:
           sip = input("Enter Client IP : \t")
           nip = input("Enter Name Node IP : ")
           print("\tConfiguring core-site.xml file ...........")
           ip = input("\n\tEnter Client IP : ")
           os.system("echo -e '<?xml version=\"1.0\"?> \n<?xml-stylesheet type=\"text/xsl\" href=\"configuration.xsl\"?>' > /root/core-site.xml")
           os.system('echo -e "\n<!-- Put site-specific property overrides in this file. -->" >> /root/core-site.xml')
           os.system('echo -e "\n<configuration>" >> /root/core-site.xml')
           os.system('echo -e "\n<property>" >> /root/core-site.xml')
           os.system('echo -e "\n<name>fs.default.name</name>" >> /root/core-site.xml')
           os.system('echo -e "\n<value>hdfs://{}:9001</value>" >> /root/core-site.xml'.format(nip))
           os.system('echo -e "\n</property>" >> /root/core-site.xml')
           os.system('echo -e "\n</configuration>" >> /root/core-site.xml')
           os.system('scp  /root/core-site.xml  {}:/etc/hadoop'.format(sip))
           print("\tHadoop Client Sucessfully Configured.........")

          i = input("do you want to continue on Hadoop menu [y/N]:\t")
          if i != 'y' and i!= 'Y':
                    break

    elif choice_hadoop == 5:
          print("press 1 : For making the local system Client")
          print("press 2 : For making Client by ssh")
          datan = int(input("Enter your choice:\t"))
          if datan == 1:
           si = input("Do You want to extend/reduce Data Node Storage? : ")
           if si == "extend":
               os.system('df -hT')
               ex = input("How much you want to extend? : ")
               vg = input("Enter Your Volume Group Name : ")
               lv = input("Enter Your Logical Volume Name : ")
               os.system('lvextend --size {} /dev/{}/{}'.format( ex , vg , lv))
               print("\tSucessfully Extended the  Data Node Storage ")
               os.system('resize2fs  /dev/{}/{}'.format( vg ,lv))
               print("--------------------------------------------------")
               os.system('df -hT')
           elif si == "reduce":
               os.system(' df -hT')
               ex = input("How much you want to reduce? : ")
               vg = input("Enter Your Volume Group Name : ")
               lv = input("Enter Your Logical Volume Name : ")
               os.system('lvextend --size {} /dev/{}/{}'.format( ex , vg , lv))
               print("\tSucessfully Reduced Data Node Storage ")
               os.system('resize2fs  /dev/{}/{}'.format( vg ,lv))
               print("--------------------------------------------------")
               os.system('df -hT')
          elif datan == 2:
           ip = input("Enter Data Node IP : \t")
           si = input("\n\tDo You want to extend/reduce Data Node Storage? : \t")
           if si == "extend":
               os.system('ssh {} df -hT'.format(ip))
               ex = input("How much you want to extend? : ")
               vg = input("Enter Your Volume Group Name : ")
               lv = input("Enter Your Logical Volume Name : ")
               os.system('ssh {} lvextend --size {} /dev/{}/{}'.format(ip , ex , vg , lv))
               print("\tSucessfully Extended the  Data Node Storage ")
               os.system('ssh {} resize2fs  /dev/{}/{}'.format(ip , vg ,lv))
               print("--------------------------------------------------")
               os.system('ssh {} df -hT'.format(ip))
           elif si == "reduce":
               os.system('ssh {} df -hT'.format(ip))
               ex = input("How much you want to reduce? : ")
               vg = input("Enter Your Volume Group Name : ")
               lv = input("Enter Your Logical Volume Name : ")
               os.system('ssh {} lvextend --size {} /dev/{}/{}'.format(ip , ex , vg , lv))
               print("\tSucessfully Reduced Data Node Storage ")
               os.system('ssh {} resize2fs  /dev/{}/{}'.format(ip , vg ,lv))
               print("------------------------------------------------------------")
               os.system('ssh {} df -hT'.format(ip))
          i = input("do you want to continue on Hadoop menu [y/N]:\t")
          if i != 'y' and i!= 'Y':
                    break

    elif choice_hadoop == 6:
          print("press 1 : For uploading data to hadoop cluster if the local system is Client ")
          print("press 2 : For uploading data to hadoop cluster if remote system is Client ")
          datan = int(input("Enter your choice:\t"))
          if datan == 1:
                 filez = input("Enter the file name which you want to upload:\t")
                 os.system("hadoop fs -put {} /".format(filez))
          elif datan == 2:
                 sip = input("Enter the ip of the Client:\t")
                 filez = input("Enter the file name which you want to upload:\t")
                 os.system("ssh {} hadoop fs -put {} /".format(sip,filez))
          i = input("do you want to continue on Hadoop menu [y/N]:\t")
          if i != 'y' and i!= 'Y':
                    break

    elif choice_hadoop == 7:
          print("""
                press 1 : For read data to hadoop cluster if local system  is client
                press 2 : For read data to hadoop cluster if remote system is Client """)
          datan = int(input("Enter your choice:\t"))
          if datan == 1:
                 os.system("hadoop fs -ls / ")
                 filez = input("Enter the file name which you want to read:\t")
                 os.system("hadoop fs -cat  /{}".format(filez))
          elif datan == 2:
                 sip = input("Enter the ip of the Client:\t")
                 os.system("ssh {} hadoop fs -ls / ".format(sip))
                 filez = input("Enter the file name which you want to read:\t")
                 os.system("ssh {} hadoop fs -cat /{}".format(sip,filez))
          i = input("do you want to continue on Hadoop menu [y/N]:\t")
          if i != 'y' and i!= 'Y':
                    break

    elif choice_hadoop == 8:
          print("""
                press 1 : For list all data to hadoop cluster in local system 
                press 2 : For list all data to hadoop cluster in remote system  """)
          datan = int(input("Enter your choice:\t"))
          if datan == 1:
                 os.system("hadoop fs -ls / ")

          elif datan == 2:
                 sip = input("Enter the ip of the Client:\t")
                 os.system("ssh {} hadoop fs -ls / ".format(sip))
          i = input("do you want to continue on Hadoop menu [y/N]:\t")
          if i != 'y' and i!= 'Y':
                    break

    elif choice_hadoop == 9:
          print("""
                press 1 : For deleting a file from hadoop cluster in local system 
                press 2 : For deleting a file from hadoop cluster in remote system  """)
          datan = int(input("Enter your choice:\t"))
          if datan == 1:
                 os.system("hadoop fs -ls / ")
                 filez = input("Enter the file which you want to delete:\t")
                 os.system("hadoop fs -rm /{} ".format(filez))

          elif datan == 2:
                 sip = input("Enter the ip of the Client node:\t")
                 os.system("ssh {} hadoop fs -ls / ".format(sip))
                 filez = input("Enter the file which you want to delete:\t")
                 os.system("ssh {} hadoop fs -rm /{} ".format(sip.filez))
          i = input("do you want to continue on Hadoop menu [y/N]:\t")
          if i != 'y' and i!= 'Y':
                    break
    elif choice_hadoop == 10:
          print("""
                press 1 : For stopping Namenode of the hadoop cluster  locally 
                press 2 : For stopping Namenode of the hadoop cluster remotelly  """)
          datan = int(input("Enter your choice:\t"))
          if datan == 1:
                os.system("hadoop-daemon.sh stop namenode")
                os.system("jps")
                print("\t \t Namenode stopped successfully ........")
          elif datan == 2:
                sip = input("Enter the ip of the Namenode:\t")
                os.system("ssh {} hadoop-daemon.sh stop namenode".format(sip))
                os.system("ssh {} jps".format(sip))
                print("\t \t Namenode stopped successfully ........")
          i = input("do you want to continue on Hadoop menu [y/N]:\t")
          if i != 'y' and i!= 'Y':
                    break

    elif choice_hadoop == 11:
          print("""
                press 1 : For stopping Datanode of the hadoop cluster  locally 
                press 2 : For stopping Datanode of the hadoop cluster remotelly  """)
          datan = int(input("Enter your choice:\t"))
          if datan == 1:
                os.system("hadoop-daemon.sh stop datanode")
                os.system("jps")
                print("\t \t Datanode stopped successfully ........")
          elif datan == 2:
                sip = input("Enter the ip of the Datanode:\t")
                os.system("ssh {} hadoop-daemon.sh stop datanode".format(sip))
                os.system("ssh {} jps".format(sip))
                print("\t \t Datanode stopped successfully ........")
          i = input("do you want to continue on Hadoop menu [y/N]:\t")
          if i != 'y' and i!= 'Y':
                    break

    elif choice_hadoop == 12:   
          print("""
    1. Converting local Master node to Datanode
    2. Converting local Master node to client
    3. Converting local Datanode to master
    4. Converting local Datanode to client
    5. Coverting local Client to master node
    6. Converting local Client to datanode""")
          datan = int(input("Enter your choice:\t"))
          if datan == 1:
                add_slave()
                print("\n\t\t Successfully converted master node into Datanode and start the service............")
                i = input("do you want to continue on hadoop menu [y/N]:\t")
                if i != 'y' and i!= 'Y':
                    break

          elif datan == 2:
                add_client()
                print("\n\t\t Successfully converted master node into Client............")
                i = input("do you want to continue on hadoop menu [y/N]:\t")
                if i != 'y' and i!= 'Y':
                    break

          elif datan == 3:
                add_master()
                print("\n\t\t Successfully converted Datanode into Masternode and start the service............")
                i = input("do you want to continue on hadoop menu [y/N]:\t")
                if i != 'y' and i!= 'Y':
                    break
          elif datan == 4:
                add_client()
                print("\n\t\t Successfully converted Datanode into Client............")
                i = input("do you want to continue on hadoop menu [y/N]:\t")
                if i != 'y' and i!= 'Y':
                    break

          elif datan == 5:
                add_master()
                print("\n\t\t Successfully converted Client into Datanode and start the service............")
                i = input("do you want to continue on hadoop menu [y/N]:\t")
                if i != 'y' and i!= 'Y':
                    break
 
          elif datan == 6:
                add_slave()
                print("\n\t\t Successfully converted Client into Datanode and start the service............")
                i = input("do you want to continue on hadoop menu [y/N]:\t")
                if i != 'y' and i!= 'Y':
                    break


    elif choice_hadoop == 13:
          break
          


        
def add_master():
    print("to create a master first you have to make a folder for that")
    fold = input("folder name with directory:\t")
    os.system("mkdir {}".format(fold))
    old = ""
    old1 = ""
    with open("/etc/hadoop/hdfs-site.xml", "r+") as f:
        old = f.read()
        if len(old) < 20:
             print("hadoop is not installed on the system")
             exit()
        jame = old.find("<confi")
        jame1 = old.find("</confi")
        jame2 = old[jame:jame1]
        old = old.replace(jame2, "<configuration>\n <property>\n<name>dfs.name.dir</name>\n<value>{}</value>\n</property>\n".format(fold))
    with open("/etc/hadoop/hdfs-site.xml", "w") as f:
        f.write(old)

    print("You have to set the ip for your master")
    ip = input("provide the ip to the master ;\t")
    with open("/etc/hadoop/core-site.xml", "r+") as f:
        old1  = f.read()
        jam = old1.find("<confi")
        jam1 = old1.find("</confi")
        jam2 = old1[jam:jam1]
        old1 = old1.replace(jam2, "<configuration>\n <property>\n<name>fs.default.name</name>\n <value>hdfs://{}:9001</value>\n</property>\n".format(ip))
    with open("/etc/hadoop/core-site.xml", "w") as f:
        f.write(old1)
    print("Now the hadoop master folder format")
    os.system("hadoop namenode -format")
    os.system("hadoop-daemon.sh start namenode")
    print("Now the hadoop master servicee start you can check it by jps command")
    print("jps")



def add_slave():
    print("to create a slave first you have to make a folder for that")
    fold = input("folder name with directory:\t")
    os.system("mkdir {}".format(fold))
    old = ""
    old1 = ""
    with open("/etc/hadoop/hdfs-site.xml", "r+") as f:
        old = f.read()
        if len(old) < 20 :
             print("hadoop is not installed on the system")
             exit()
        jame = old.find("<confi")
        jame1 = old.find("</confi")
        jame2 = old[jame:jame1]
        old = old.replace(jame2, "<configuration>\n<property>\n<name>dfs.data.dir</name>\n<value>{}</value>\n</property>\n".format(fold))
    with open("/etc/hadoop/hdfs-site.xml", "w") as f:
        f.write(old)

    print("You have to provide hadoop master ip to established connection ")
    ip = input("provide the ip of the master ;\t")
    with open("/etc/hadoop/core-site.xml", "r+") as f:
        old1 = f.read()
        jam = old1.find("<confi")
        jam1 = old1.find("</confi")
        jam2 = old1[jam:jam1]
        old1 = old1.replace(jam2, "<configuration>\n<property>\n<name>fs.default.name</name>\n<value>hdfs://{}:9001</value>\n</property>\n".format(ip))
    with open("/etc/hadoop/core-site.xml", "w") as f:
        f.write(old1)
    os.system("hadoop-daemon.sh start datanode")
    print("Now the hadoop slave services start you can check it by jps command")
    os.system("jps")


def add_client():
    old = ""
    old1 = ""
    with open("/etc/hadoop/hdfs-site.xml", "r+") as f:
        old = f.read()
        if len(old) < 20:
             print("hadoop is not installed on the system")
             exit()
        jame = old.find("<confi")
        jame1 = old.find("</confi")
        jame2 = old[jame:jame1]
        old = old.replace(jame2, "<configuration>\n")
    with open("/etc/hadoop/hdfs-site.xml", "w") as f:
        f.write(old)

    print("You have to provide hadoop master ip to established connection between client and master")
    ip = input("provide the ip of the master ;\t")
    with open("/etc/hadoop/core-site.xml", "r+") as f:
        old1 = f.read()
        jam = old1.find("<confi")
        jam1 = old1.find("</confi")
        jam2 = old1[jam:jam1]
        old1 = old1.replace(jam2, "<configuration>\n<property>\n<name>fs.default.name</name>\n<value>hdfs://{}:9001</value>\n</property>\n".format(ip))
    with open("/etc/hadoop/core-site.xml", "w") as f:
        f.write(old1)
    print("Now the hadoop client services start you can check it by jps command")
    os.system("jps")
	

dnf ans():
  while True:
      os.system("tput setaf 2")
      os.system("\n\t\t\tfiglet -t -k ansible \n\n\n")
      print("""
      \n
      Ansible Menu:
      ----------
      Press 1: To install ansible
      Press 2: Create inventory
      Press 3: Ping all nodes to check connectivity
      Press 4: Install httpd package in target nodes
      Press 5: Back to main menu
      """)
      as = int(input("Enter your choice:\t"))
      os.system("tput setaf 15")

      if as == 1:
        os.system("pip3 install ansible")
        os.system("ansible --version")
        i = input("do you want to continue on ansible menu [y/n]:\t")
        if i != 'y':
           break
	
      elif as == 2:
        file = input("give name to inventory file")
        os.system("touch {}.txt".format(file))
        ip, user, password = input("Enter credentital of target node in the format (ip root password): ").split()
        with open("/root/{}.txt".format(file), "w") as f:
              f.write("("{}  ansible_user={} ansible_ssh_pass={} ansible_connection=ssh".format(ip, user, password))")
        with open("/etc/ansible/ansible.cfg", "w") as f:
              f.write("[defaults]\n inventory = /root/{}.txt\n host_key_checking = false".format(file))
        os.system("ansible all --list-hosts")
        i = input("do you want to continue on ansible menu [y/n]:\t")
        if i != 'y':
           break
	
      elif as == 3:
        os.system("ansible all -m ping")
        i = input("do you want to continue on ansible menu [y/n]:\t")
        if i != 'y':
           break
	
      elif as == 4:
        os.system("ansible all -m package -a "name=httpd state=present"")
        i = input("do you want to continue on ansible menu [y/n]:\t")
        if i != 'y':
           break
	
     elif as == 5:
        break

dnf nfs():
  while True:
      os.system("tput setaf 2")
      os.system("\n\t\t\tfiglet -t -k NFS \n\n\n")
      print("""
      \n
      Network File System:
      --------------------
      Press 1: To install nfs
      Press 2: To configure and share storage  
      Press 3: Create security-group
      Press 4: Launch EC2 instance
      Press 5: Describe EC2 instances
      Press 6: Create and attach a volume to EC2 instance
      Press 7: Create a S3 bucket
      Press 8: Upload objects in S3 bucket
      Press 9: Lunch a cloudfront
      Press 10: Configure cli for iam user
      Press 11: Back to main menu
      """)
      as = int(input("Enter your choice:\t"))
      os.system("tput setaf 15")

      if  == 1:
        os.system("yum install nfs-utils")
        i = input("do you want to continue on nfs menu [y/n]:\t")
        if i != 'y':
           break
      elif  == 2:
        ip = input("Enter ip of the system where storage is to be shared: ")
        folder = input("Enter a name for the folderr: ")
        os.system("mkdir /{}".format(folder))
        with open("/etc/exports", "w") as f:
                f.write("/{} {}".format(folder, ip))
        i = input("do you want to continue on nfs menu [y/n]:\t")
        if i != 'y':
           break
	
      elif  == 3:
        ip = input("Enter ip of the system where storage is to be shared: ")
        folder = input("Enter a name for the folderr: ")
        os.system("mkdir /{}".format(folder))
        with open("/etc/exports", "w") as f:
                f.write("/{} {}".format(folder, ip))
        i = input("do you want to continue on nfs menu [y/n]:\t")
        if i != 'y':
           break
      
