#!/usr/bin/python3

import os
import subprocess as sp

dnf lvm():
  while True:
      os.system("tput setaf 2")
      os.system("\n\t\t\tfiglet -t -k lvm menu \n\n\n")
      print("""
      \n
      Logical Volume Management Operations:
      -------------------------------------
      Press 1: To create partition.
      Press 2: To get all partitions information in one disk.
      Press 3: To format the partition.
      Press 4: To mount the partition to the directory.
      Press 5: To unmount the partition.
      Press 6: To get details of size and mount point of the disk.
      Press 7: To create Physical volume
      Press 8: To display PV information
      Press 9: To create Volume Group
      Press 10: To display VG information.
      Press 11: To create logical volume
      Press 12: To display LV information
      Press 13: To extend the size of LV
      Press 14: To reduce the size of LV
      Press 15: Go back to main menu
      """)

      vm = int(input("Enter your choice:\t"))
      os.system("tput setaf 15")

      if vm == 1:
        disk_name = input("Enter the complete disk name for e.g. /dev/sdb: ")
        os.system("fdisk {} ".format(disk_name))
      
      elif vm == 2:
         d_name = input("Enter the disk name:")
         os.system("fdisk -l {}".format(d_name))
      
      elif vm == 3:
        part=input("Enter the partition name(e.g. /dev/sdb1): ")
        os.system("mkfs.ext4 {}".format(part))
      
      elif vm == 4:
        folder_name=input("Enter the folder name on which you want to mount the partition. ")
        part_name = input("Enter the formatted partition full name: ")
        os.system("mount {} {}".format(part_name, folder_name))
      
      elif vm == 5:
        folder_name=input("Enter the folder name on which you want to unmount the partition. ")
        part_name = input("Enter the partition full name: ")
        return os.system("umount {} {}".format(part_name, folder_name))
      
      elif vm == 6:
        os.system("df -h")

      elif vm == 7:
        disk_name=input("Enter the disk name :")
        os.system("pvcreate {}".format(disk_name))
    
      elif vm == 8:
        disk_name=input("Enter the disk name :")
        os.system("pvdisplay {}".format(disk_name))
    
      elif vm == 9:
        pv1=input("Enter first PV name:")
        pv2=input("Enter second PV name:")
        vg=input("Enter the name of the VG:")
        os.system("vgcreate {} {} {}".format(pv1, pv2, vg))
    
      elif vm == 10:
        vg=input("Enter the VG name:")
        os.system("vgdisplay {}".format(vg))
    
      elif vm == 11:
        size=input("Enter the size of the Logical volume(e.g. 8G):")
        vg=input("Enter the name of the VG:")
        lv=input("Enter the name of the Logical volume:")
        os.system("lvcreate --size {} --name {} {}".format(size, lv, vg))
    
      elif vm == 12:
        lv=input("Enter the name of the Logical volume:")
        vg=input("Enter the name of the VG:")
        os.system("lvdisplay {}/{}".format(vg, lv))

      elif vm == 13:
        lv=input("Enter the name of the Logical volume:")
        size=input("How much size you want to extend(e.g. 8G):")
        os.system("lvextend --size +{} {}".format(size, lv))
        os.system("resize2fs {}".format(lv))
    
      elif vm == 14:
        lv=input("Enter the name of the Logical volume:")
        size=input("How much size you want to reduce(e.g. 8G):")
        os.system("lvreduce --size -{} {}".format(size, lv))
        os.system("resize2fs {}".format(lv))
    
      elif vm == 15:
        break()
       
while True:
      os.system("clear")
      lvm()
      input("press enter for continue:")
    os.system("tput setaf 7")
