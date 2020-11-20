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
      os.system("\n\t\t\tfiglet -t -k webserver menu for local system\n\n\n")
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
	
      elif ch == 2:
        os.system("cal")
	
      elif ch == 3:
        os.system("gnome-control-center")
  
      elif ch == 4:
        os.system("lscpu")

      elif int(ch) == 5:
        name = input("enter package name:")
        os.system("yum install {} -y".format(name))
  
      elif int(ch) == 6:
        name = input ("enter package name:")
        os.system("yum info {}".format(name))
  
      elif int(ch) == 7:
        num = input ("enter the service name:")
        os.system("systemctl status {}".format(num))
  
      elif int(ch) == 8:
        os.system("rpm -qa")
  
      elif int(ch) == 9:
        name = input ("enter software name:")
        os.system("yum info {}".format(name))
  
      elif int(ch) == 10:
        new_uswer = input ("enter name of the new user:")
        os.system("sudo useradd {}".format(new_user))
        os.system("id -u {}".format(new_user))
  
      elif int(ch) == 11:
        name = input ("name the user:")
        os.system("sudo userdel {}".format(name))
    
      elif ch == 12:       
        name=input("name your directory :")
        os.system("mkdir /{}".format(name))
	
      elif ch == 13:       
        name=input("name of the service :")
        os.system("systemctl start {}".format(name))
	
      elif ch == 14:       
        name=input("name of the service :")
        os.system("systemctl stop {}".format(name))
