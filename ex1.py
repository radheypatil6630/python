#1.write a program that reads a value of n  and check the number is 0 or non zero value
"""
n=int ( input("enter number :"));

if(n==0):
    print( "number is zero");
else:
    print( "number is non zero");
"""

#2. write a program read number the number is positive or negative
"""
n=int(input("enter number :"));
if(n>=0):
    print("number is positive ");
else:
    print("number is negative ");
"""
#3.write a program to check enter charactered is vowel or consulent.
"""
s=str(input("enter charater"));
if(s=='a' or s=='e' or s=='i' or s=='o' or s=='u'):
    print("character is vowel ");
else:
    print("character is cosulent");
"""

#4.even odd

"""
n1=int(input("enter number:"));
if(n1%2==0):
    print("number is even");
else:
    print("number is odd");
"""
#5.leap year or not


year=int(input("enter year :"));
if(year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("year is leap year");
else:
    print("year is not leap year");

#6.smallest number among three

n2=int(input("enter number :"));
n3=int(input("enter number :"));
n4=int(input("enter number :"));


if(n2<n3 and n2<n4):
    print(n2," is smallest no");
elif(n3<n2 and n3<n4):
    print(n3," is smallest no");
else:
    print(n4," is smallest no");

#7.evalute student performance
marks=int(input("enter marks of student"));

if(marks >=80 and marks <=100):
    print("marks is very good ");
elif(marks >=60 and marks <=80):
    print("marks is distinct");
else:
    print("marks is good");
