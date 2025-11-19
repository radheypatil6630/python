import arithmeticModule
# another way is  import artithmeticModule as a       # a.add(1,2)
num1=int(input("enter 1st number : "))
num2=int(input("enter 2nd number : "))

print("addition        : ",arithmeticModule.add(num1,num2))
print("substraction    : ",arithmeticModule.substract(num1,num2))
print("multiplication  : ",arithmeticModule.multiplication(num1,num2))
print("division        : ",arithmeticModule.division(num1,num2))
print("modulus         : ",arithmeticModule.modulus(num1,num2))
print("floor division  : ",arithmeticModule.floor_division(num1,num2))