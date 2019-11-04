# -*- coding: utf-8 -*-
"""Untitled7.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1tOWoQASKJlGCOe528b_NW3RQQ23Xejir
"""

import os

def main():
  directory = input("Enter the directory that you want to save the file in : ")
  filename = input("Enter the filename : ")
  name = input("Enter your name : ")
  address = input("Enter your address : ")
  phone_number = input("Enter your phone number : ")
  #checking if the directory exists
  if os.path.isdir(directory):
    #creating and opening the file to write
    createFile = open(os.path.join(directory,filename),'w')
    #writing the data
    createFile.write(name+','+address+','+phone_number+'\n')
    #closing the file
    createFile.close()
    
    print("File contents:")
    #reading the file for proof of storing
    readFile = open(os.path.join(directory,filename),'r')
    for line in readFile:
      print(line)
    readFile.close()
  else:
    print("Sorry that directory does not exist...")
main()