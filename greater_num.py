a=int(input("enter 1 number : "));
b=int(input("enter 2 number : "));
c=int(input("enter 3 number : "));

if a>b and a>c :
    print('{} is greater'.format(a));
elif b>c and b>a :
    print('{} is greater'.format(b));
else :
    print('{} is greater'.format(c));
