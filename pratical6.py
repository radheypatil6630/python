print ("file operation ")
import os

with open('example.txt','r') as file:
    content=file.read()
print(content)

with open('example.txt','w') as file:  #previous data are replaced by new data
    print(file.write("how are you "))


f = open("example.txt", "a")
f.write("Now the file has more content!")
f.close()


f = open("newfile.txt", "x")#create a new file



os.remove("newfile.txt")#delete file
