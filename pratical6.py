print ("file operation ")
import os


with open('example.txt','r') as file:
    content=file.read()
    print(content)
    
    file.close()

    

with open('example.txt','w') as file1:
    file1.write(" add new data")
    # file1.seek(0)
    
    
with open ('example.txt','a+') as file:
    file.write(" add at end ")
    file.seek(0)
    data=file.read()
    print("data write :- "+data)
    
f=open('example.txt','r+') 
print(f.read())
f.write(" after taking r+ mode")

f=open('example.txt','+at')
f.write(" new data")

f=open('example.txt','wt')
f.write(" new data")


# os.remove('newfile1.txt')#deleted
print("file deleted")

