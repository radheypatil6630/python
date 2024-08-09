#numeric
a=int(input("enter integer : "));
b=float(input("enter float : "));
c=complex(input("enter complex : "));
print (type(a),type(b),type(c));
#text
s=str(input("enter string : "));
print(type(s));
#squence
l=["abc","xhj"]
print(type(l));

t=(12,32);
print(type(t));



#bytearray
by=bytes(122);
ba=bytearray('hello','utf-8');
print (type(by),type(ba));

for i in range (6):
    print(i)
    
