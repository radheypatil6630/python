
print("set ")

set1={"radhey","radhey"}# set avoid duplication (doesnt take error but it shows only one value instead of both)
set2=set(("om","harsh","radhey"))
print(set1)


set3=set2.difference(set1)#show differenece between 2  sets
print("difference =",set3)# use near of sets where present

set1.update(set2)
print("after updating =",set1)

set2.remove("om")#if item not present  reaise error
print("after removing one element =",set2)

set2.clear()
print("after clear() =",)

set2.add("harsh")
set2.add("radhey")
set2.add("om")
print("add() = ",set2)

set2.discard("sami") #if item not present not reaise error
print("discard() = ",set2)


print("\n\n ----- String operation -----")

str="hello World"
dyp=" a"

print("upper case ",str.upper())
print("lower case ",str.lower())

print("check upper or not : ",str.isupper())
print("check lower or not : ",str.islower())

print("check decimal status :",str.isdecimal())

print("join operation : ",str.join(dyp))


print("\n\n --- Dictionary operation ---")

d={"a":1,"b":2,"c":3}


a={1:"abc",2:"xyz"}
print(d)

print("praticular item : ",d["a"])

print("length : ",len(d));

d.update(a)
print("after update operation : ",d)

d.popitem()
print("after pop item :",d)



