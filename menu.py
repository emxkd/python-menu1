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
      os.system("\n\t\t\tfiglet -t -k webserver menu \n\n\n")
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
	i = input("do you want to continue on webserver menu [y/n]:\t")
        if i != 'y':
          break
	
      elif ch == 2:
        os.system("cal")
	i = input("do you want to continue on webserver menu [y/n]:\t")
        if i != 'y':
          break
	
      elif ch == 3:
        os.system("gnome-control-center")
        i = input("do you want to continue on webserver menu [y/n]:\t")
        if i != 'y':
          break

      elif ch == 4:
        os.system("lscpu")
	i = input("do you want to continue on webserver menu [y/n]:\t")
        if i != 'y':
          break

      elif ch == 5:
        name = input("enter package name:")
        os.system("yum install {} -y".format(name))
        i = input("do you want to continue on webserver menu [y/n]:\t")
        if i != 'y':
          break

      elif ch == 6:
        name = input ("enter package name:")
        os.system("yum info {}".format(name))
	i = input("do you want to continue on webserver menu [y/n]:\t")
        if i != 'y':
          break
  
      elif ch == 7:
        num = input ("enter the service name:")
        os.system("systemctl status {}".format(num))
	i = input("do you want to continue on webserver menu [y/n]:\t")
        if i != 'y':
          break
  
      elif ch == 8:
        os.system("rpm -qa")
	i = input("do you want to continue on webserver menu [y/n]:\t")
        if i != 'y':
          break
  
      elif ch == 9:
        name = input ("enter software name:")
        os.system("yum info {}".format(name))
	i = input("do you want to continue on webserver menu [y/n]:\t")
        if i != 'y':
          break
  
      elif ch == 10:
        new_uswer = input ("enter name of the new user:")
        os.system("sudo useradd {}".format(new_user))
        os.system("id -u {}".format(new_user))
	i = input("do you want to continue on webserver menu [y/n]:\t")
        if i != 'y':
          break
  
      elif ch == 11:
        name = input ("name the user:")
        os.system("sudo userdel {}".format(name))
	i = input("do you want to continue on webserver menu [y/n]:\t")
        if i != 'y':
          break
    
      elif ch == 12:       
        name=input("name your directory :")
        os.system("mkdir /{}".format(name))
	i = input("do you want to continue on webserver menu [y/n]:\t")
        if i != 'y':
          break
	
      elif ch == 13:       
        name=input("name of the service :")
        os.system("systemctl start {}".format(name))
	i = input("do you want to continue on webserver menu [y/n]:\t")
        if i != 'y':
          break
	
      elif ch == 14:       
        name=input("name of the service :")
        os.system("systemctl stop {}".format(name))
	i = input("do you want to continue on webserver menu [y/n]:\t")
        if i != 'y':
          break
      
      elif ch == 15:
        break
	
dnf sysop2():
  while True:
      os.system("tput setaf 2")
      os.system("\n\t\t\tfiglet -t -k webserver menu \n\n\n")
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
	i = input("do you want to continue on webserver menu [y/n]:\t")
        if i != 'y':
          break
	
      elif ch1 == 2:
        ip = input("Enter the ip of the system:\t")
        os.system("ssh {} cal".format(ip))
	i = input("do you want to continue on webserver menu [y/n]:\t")
        if i != 'y':
          break
	
      elif ch1 == 3:
        ip = input("Enter the ip of the system:\t")
        os.system("ssh {} gnome-control-center".format(ip))
        i = input("do you want to continue on webserver menu [y/n]:\t")
        if i != 'y':
          break

      elif ch1 == 4:
        ip = input("Enter the ip of the system:\t")
        os.system("ssh {} lscpu".format(ip))
	i = input("do you want to continue on webserver menu [y/n]:\t")
        if i != 'y':
          break

      elif ch1 == 5:
        ip = input("Enter the ip of the system:\t")
        name = input("enter package name:")
        os.system("ssh {} yum install {} -y".format(ip, name))
        i = input("do you want to continue on webserver menu [y/n]:\t")
        if i != 'y':
          break

      elif ch1 == 6:
        ip = input("Enter the ip of the system:\t")
        name = input ("enter package name:")
        os.system("ssh {} yum info {}".format(ip, name))
	i = input("do you want to continue on webserver menu [y/n]:\t")
        if i != 'y':
          break
  
      elif ch1 == 7:
        ip = input("Enter the ip of the system:\t")
        num = input ("enter the service name:")
        os.system("ssh {} systemctl status {}".format(ip, num))
	i = input("do you want to continue on webserver menu [y/n]:\t")
        if i != 'y':
          break
  
      elif ch1 == 8:
        ip = input("Enter the ip of the system:\t")
        os.system("ssh {} rpm -qa".format(ip))
	i = input("do you want to continue on webserver menu [y/n]:\t")
        if i != 'y':
          break
  
      elif ch1 == 9:
        ip = input("Enter the ip of the system:\t")
        name = input ("enter software name:")
        os.system("ssh {} yum info {}".format(ip, name))
	i = input("do you want to continue on webserver menu [y/n]:\t")
        if i != 'y':
          break
  
      elif ch1 == 10:
        ip = input("Enter the ip of the system:\t")
        new_uswer = input ("enter name of the new user:")
        os.system("ssh {} sudo useradd {}".format(ip, new_user))
        os.system("ssh {} id -u {}".format(ip, new_user))
	i = input("do you want to continue on webserver menu [y/n]:\t")
        if i != 'y':
          break
  
      elif ch1 == 11:
        ip = input("Enter the ip of the system:\t")
        name = input ("name the user:")
        os.system("ssh {} sudo userdel {}".format(ip, name))
	i = input("do you want to continue on webserver menu [y/n]:\t")
        if i != 'y':
          break
    
      elif ch1 == 12: 
        ip = input("Enter the ip of the system:\t")
        name=input("name your directory :")
        os.system("ssh {} mkdir /{}".format(ip, name))
	i = input("do you want to continue on webserver menu [y/n]:\t")
        if i != 'y':
          break
	
      elif ch1 == 13:
        ip = input("Enter the ip of the system:\t")
        name=input("name of the service :")
        os.system("ssh {} systemctl start {}".format(ip, name))
	i = input("do you want to continue on webserver menu [y/n]:\t")
        if i != 'y':
          break
	
      elif ch1 == 14:
        ip = input("Enter the ip of the system:\t")
        name=input("name of the service :")
        os.system("ssh {} systemctl stop {}".format(ip, name))
	i = input("do you want to continue on webserver menu [y/n]:\t")
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

      di = int(input("Enter your choice:\t"))
      os.system("tput setaf 15")

      if di == 1:
        ip = input("Enter the ip of the system:\t")
        os.system("ssh {} sudo yum -y install https://dl.fedoraproject.org/pub/epel/epel-release-latest-8.noarch.rpm".format(ip))
        os.system("ssh {} sudo yum update".format(ip))
        os.system("ssh {} yum -y install docker-ce --nobest".format(ip))
        os.system("ssh {} systemctl start docker".format(ip))
        os.system("ssh {} systemctl enable docker".format(ip))
        i = input("do you want to continue on docker menu [y/n]:\t")
        if i != 'y':
          break

      elif di == 2:
        ip = input("Enter the ip of the system:\t")
        os.system("ssh {} docker image ls".format(ip))
        i = input("do you want to continue on docker menu [y/n]:\t")
        if i != 'y':
          break
  
      elif di == 3:
        ip = input("Enter the ip of the system:\t")
        name = input ("enter image name with version(name:version):")
        os.system("ssh {} docker pull {}".format(ip, name))
        i = input("do you want to continue on docker menu [y/n]:\t")
        if i != 'y':
          break

      elif di == 4:
        ip = input("Enter the ip of the system:\t")
        name = input ("enter image name: ")
        os.system("ssh {} docker push {}".format(ip, name))
        i = input("do you want to continue on docker menu [y/n]:\t")
        if i != 'y':
          break
	
      elif di == 5:
        ip = input("Enter the ip of the system:\t")
        name = input ("enter image name:")
        os.system("ssh {} docker image rm {}".format(name))
        i = input("do you want to continue on docker menu [y/n]:\t")
        if i != 'y':
          break
  
      elif di == 6:
        ip = input("Enter the ip of the system:\t")
        name = input ("enter image name:")
        os.system("ssh {} docker build -t {}".format(name))
        i = input("do you want to continue on docker menu [y/n]:\t")
        if i != 'y':
          break
  
      elif di == 7:
        ip = input("Enter the ip of the system:\t")
        img_name = input ("name the image:")
        port = input ("enter port:")
        con_name = input ("enter container name:")
        os.system("ssh {} docker container run --name {} -p {} {}".format(ip, con_name, port, img_name))
        i = input("do you want to continue on docker menu [y/n]:\t")
        if i != 'y':
          break
  
      elif di == 8:
        ip = input("Enter the ip of the system:\t")
        os.system("ssh {} docker network ls".format(ip))
        i = input("do you want to continue on docker menu [y/n]:\t")
        if i != 'y':
          break
  
      elif di == 9:
        ip = input("Enter the ip of the system:\t")
        os.system("ssh {} docker container ls".format(ip))
        i = input("do you want to continue on docker menu [y/n]:\t")
        if i != 'y':
          break
  
      elif di == 10:
        ip = input("Enter the ip of the system:\t")
        os.system("ssh {} docker container rm -f $(docker ps -aq)".format(ip))
        i = input("do you want to continue on docker menu [y/n]:\t")
        if i != 'y':
          break
  
      elif di == 11:
         break
	
	


