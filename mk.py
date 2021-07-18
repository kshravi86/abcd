import os
dell=open("del.txt","rt")
f=dell.readlines()
for i in f:


  os.system("rm -rf "+i)