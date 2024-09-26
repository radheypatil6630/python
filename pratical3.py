l1=["hello","world","dyp"]

l2=[1,2,3,4]

print(l1)

print(len(l1))#length
print(type(l1))

print("index of ",l1[1],"is =",l1.index("world"))#index of element

l1.insert(1,"om")# it take different datatypes also 
print("insert data at ",l1)#inserting data

l1.sort()
print("sort data =",l1)#sort data


l1.extend(l2)
print("after extending ",l1)

l1.append("samii")
print("append() = ",l1)

l1.remove("world")
print("remove() = ",l1)

l1.reverse()
print("reverse() = ",l1)

print("copy() = ",l1.copy())

print("count() = ",l1.count("hello"))

l1.pop()
print("pop() - ",l1)



print("tuple operation ")
tuple1=(1,2,3,4,5)#immutable

print(tuple1)

print("length of tuple =",len(tuple1))# length of tuple

print("type of tuple =",type(tuple1))#type of tuple



print("array operation :")
a=[1,3,4,5]

print (a)

a.append(10)
print("after append :",a)

a.insert(2,12)
print("after insert :",a)

a.remove(3)
print("after remove :",a)

a.sort()
print("after sort :",a)

a.pop()
print("after pop :",a)

d={"a":1,"b":2,"c":3}

a={1:"abc",2:"xyz"}
print(d)

d.update(a)
print("after update operation : ",d)

d.pop()
print("after pop operation : ",d)

d.items()
print("after show items : ",d)

d.popitem()
print("after pop item :",d)
