import os

while(True):
    ch=input("enter choice :")
    print("Directory operations :\n 1.create \n 2.remove \n 3.modify ")
    
    if ch==1:
        
        try:
            os.mkdir("mypackage ")
            print("directory created using mkdir ")
        except:
            print("file already exists")

    

    # os.rmdir("D:\programming\python\mypackage")
    # print("directory deleted ")

