import os
os.system("cls")

#func def sample
"""def functionname():
    print("this is the message from the function")
    return
    
print("this is the message from the main scope ")
print("calling the function")
functionname()

print("completed the function scope")
"""


#func add values
"""
def addvalues():
    operand01=int(input("please enter the first value: "))
    operand02=int(input("please enter the second value: "))
    
    result=operand01+operand02
    print("the sum of the given values is :",result)
    return
    
print("please give the values to continue the operation")

addvalues()
"""


#func add values 2
"""
def addvalues(param01,param02):
    
    result=operand01+operand02
    print("the sum of the given values is :",result)
    return
    
operand01=int(input("please enter the first value: "))
operand02=int(input("please enter the second value: "))

addvalues(operand01,operand02)
"""


#func add values 3
"""
def addvalues():
    operand01=int(input("please enter the first value: "))
    operand02=int(input("please enter the second value: "))
    
    result=operand01+operand02
    print("the sum of the given values is :")
    return result
    
print("please give the values to continue the operation")

output=addvalues()
print(output)
"""


#func add values 4
"""
def addvalues(param01,param02):
    
    result=operand01+operand02
    print("the sum of the given values is :",end=" ")
    return result
    
operand01=int(input("please enter the first value: "))
operand02=int(input("please enter the second value: "))

output=addvalues(operand01,operand02)

print(output)
"""

#func givendata
"""
def givendata():
    firstname=input("\nplease enter your first name: ")
    middlename=input("\nplease enter your middel name:")
    lastname=input("\nplease enter your lastname:")
    inage=input("\nplease enter your current age:")
    inheight=input("\nplease enter your current height:")
    return outputdata(firstname,middlename,lastname,inage,inheight)
    
    
def outputdata(firstname,middlename,lastname,inage,inheight):    
    print("\n THE GIVEN DETAILS ARE:")
    print("\n NAME:",firstname,middlename,lastname,end="\n")
    print("\n with age and height is:",inage ,"years and ",inheight,"cms",end="\n")
    
    return 
    
givendata()
"""


#calucaltor with the help of functions
"""
def addition(operand01,operand02):
    result=operand01+operand02
    print( result)
def subtraction(operand01,operand02):
    result=operand01-operand02
    print(result)
def multiply(operand01,operand02):
    result=operand01*operand02
    print(result)
def division(operand01,operand02):
    result=operand01/operand02
    print(result)
def remainder(operand01,operand02):
    result=(operand01%operand02)
    print(result)
def floordivision(operand01,operand02):
    result=operand01//operand02
    print(result)
def exponent(operand01,operand02):
    result=operand01**operand02
    print(result)
    
num01=float(input("please enter the first number : "))
num02=float(input("please enter the second number : "))

print("1.addition\n2.subtraction\n3.multiplication\n4.division(with quotient as result)\n5.division(with remainder as result)\n6.floor division\n7.expoentation")
loop=True
while loop==True:
    choice=int(input("please enter your choice : "))
    if choice==1:
        addition(num01,num02)
    elif choice==2:
        subtraction(num01,num02)
    elif choice==3:
        multiply(num01,num02)
    elif choice==4:
        division(num01,num02)
    elif choice==5:
        remainder(num01,num02)
    elif choice==6:
        floordivision(num01,num02)
    elif choice==7:
        exponent(num01,num02)
    else:
        print("please enter the correct choice")
        break
    
    oncemore=input("\n\ndo you want to continue (Y/N): ")
    if oncemore != 'y' or oncemore != 'Y':
        loop=False
"""


#func add values addresses
"""
def addvalues(param01,param02):
    
    print("the addresses of the given first number is : ",id(param01),"the raw addresses is : ",hex(id(param01)),end="\n")
    print("the addresses of the given first number is : ",id(param02),"the raw addresses is : ",hex(id(param02)),end="\n")
    result=param01+param02
    
    print("the sum of the given values is :",end=" ")
    return result
    
operand01=int(input("please enter the first value: "))
operand02=int(input("please enter the second value: "))

print("the addresses of the given first number is : ",id(operand01),"the raw addresses is : ",hex(id(operand01)),end="\n")
print("the addresses of the given first number is : ",id(operand02),"the raw addresses is : ",hex(id(operand02)),end="\n")

output=addvalues(operand01,operand02)

print(output)
"""


#func parameters types 2

import time

def incrementvalue(inparam):
    print("the given value is :",inparam)
    inparam+=10
    print("the value is :",inparam)
    return
    
operand01=int(input("please enter a value :"))
incrementvalue(operand01)