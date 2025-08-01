# The os module in Python is a built-in standard library module 
# that allows your Python programs to interact with the operating system.
# It provides tools to work with:
import os
# Files and directories
 
print(os.getcwd()) # get current working directory
os.chdir('C:') # change current working directory
print(os.getcwd())

os.chdir('D:/Data Science/python/python')
print(os.getcwd()) # change to original

## list files and directories in a directory

print(os.listdir(".")) # currrent working directory
print(os.listdir(path='D:/Data Science'))

## create directories

pt = 'D:/Data SCience/python/python/one/two/three'
if not os.path.exists(pt):
    os.makedirs('one/two/three') # create nested directories

import time
time.sleep(5)

os.rmdir('one/two/three') #removes empty directory
os.rmdir('one/two')
os.rmdir('one')


## delete file

f = open('E:/aatest.txt','w')

time.sleep(3)
# os.remove('E:/aatest.txt')


# Environment variables
# Paths
# Process management

