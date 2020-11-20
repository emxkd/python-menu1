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
