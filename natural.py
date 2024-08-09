
#natural no
n1=int(input("enter number :"));
for i in range (1,n1+1):
    print(i);


#even number
print("\n\n Even number");
n2=int(input("enter number for print even upto thi number :"));
for i in range (1,n2+1):
    if(i % 2 == 0):
        print(i);

#odd number
print("\n\n odd number");
n3=int(input("enter number for print odd upto thi number :"));
for i in range (1,n3+1):
    if(i % 2 != 0):
        print(i);

#sum of num
print("\n\n Sum of even numbers :");
sum=0;
r=int(input("enter range number :"));
for i in range(1,r+1):
    sum+=i;
print(sum);


#reverse no
print("\n\n reverse no ");

rev=int(input("enter range :"));
for i in range (rev,0,-1):
    print(i);


#fibonacci series

print("\n\n fibonacci series");
a=0;
b=1;
c=0;
n5=int(input("enter range :"));


temp=a;


for i in range(2,n5+2):
    print(a,end=" ");
    c=a+b;#0+1   0 1 1 2 3 5
    a=b;
    b=c;
print()



#factorial num
print("\n\n factorial")
fact=1;
n6=int(input("enter number :"));
for i in range (1,n6+1):
    fact*=i
print("factorial is :",fact)




#prime
print("\n\n prime number ")
n7=int(input("enter number :"))

isprime=False

for i in range(2,n7//2):
    if(n%i==0):
        isprime=True
        break
    

if(isprime==True):
    print("not prime")
else:
    print("prime")



#sum of digit
print("sum of digit ");
digit=int(input("enter number :"))
sum=0
rem=0
while (digit>0):
    rem=digit%10
    sum+=rem;
    digit=digit//10
print(sum)


#palindrome
print("Palindrome number ");
digit=int(input("enter number :"))
sum=0
rem=0
while (digit>0):
    rem=digit%10
    sum=sum*10+rem;
    digit=digit//10
print(sum)







    






    
