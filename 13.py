#!bin\python
import os,os.path
x=os.getcwd()
y=os.listdir(x)
z=os.path.getsize(x)
for files in y:
     name=os.path.join(files)
     size=os.path.getsize(files)
     print(name,size)

             

