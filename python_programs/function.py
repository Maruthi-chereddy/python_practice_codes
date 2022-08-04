import os
os.system("cls")

#func def sample
"""
def printmessage():
    #this is documentation
    print("this is from function")
    return
    
print("this is before calling the function")
printmessage()
print("this is after calling the function")
"""

#func add values
"""
def addvalues():
   #this is an example of without accepting parameters and not returning any values
   operand01=int(input("please enter the first value : "))
   operand02=int(input("please enter the second value : "))
   result=operand01+operand02
   print("the sum of the given two numbers is :",result)
   
   return
addvalues()
"""


#func add values 2
"""
def addvalues(operand01,operand02):
   #this is an example of with accepting parameters and not returning any values
  
   result=operand01+operand02
   print("the sum of the given two numbers is :",result)
   
   return

operand01=int(input("please enter the first value : "))
operand02=int(input("please enter the second value : "))
addvalues(operand01,operand02)
"""

#func add values 3
"""
def addvalues():
   #this is an example of without accepting parameters and returning any values
   operand01=int(input("please enter the first value : "))
   operand02=int(input("please enter the second value : "))
   result=operand01+operand02
   
   
   return result

printresult=addvalues()
print("the sum of the given values is :",printresult)
"""

#func add values 4
"""
def addvalues(operand01,operand02):
   #this is an example of with accepting parameters and  returning any values
   print("the address of operand01: ",id(operand01),"the raw address o fthe operand01 is :",hex(id(operand01)))
   print("the address of operand01: ",id(operand02),"the raw address o fthe operand01 is :",hex(id(operand02)))
   result=operand01+operand02
   return result
operand01=int(input("please enter the first value : "))
operand02=int(input("please enter the second value : "))
printresult=addvalues(operand01,operand02)

print("the address of operand01: ",id(operand01),"the raw address o fthe operand01 is :",hex(id(operand01)))
print("the address of operand01: ",id(operand02),"the raw address o fthe operand01 is :",hex(id(operand02)))
print("the sum of the given two numbers is :",printresult)
"""


#func givendata
"""
def gettingdetails():
    firstname=input("\nplease enter your first name: ")
    middlename=input("\nplease enter your middel name:")
    lastname=input("\nplease enter your lastname:")
    inage=input("\nplease enter your current age:")
    inheight=input("\nplease enter your current height:")
    
    printingdetails(firstname,middlename,lastname,inage,inheight)
    return
def printingdetails(firstname,middlename,lastname,inage,inheight):    
    print("\n THE GIVEN DETAILS ARE:")
    print("\n NAME:",firstname,middlename,lastname,end="\n")
    print("\n with age and height is:",inage ,"years and ",inheight,"cms",end="\n")
    return
    
gettingdetails()
"""


#func parameters types
"""
def paramchange(param01):
    print("the given value of operand01 is :",param01)
    print("assinging new value to operand01")
    param01=25
    print("the new assinged value of operand01 is :",param01)
    return
operand01=45
print("the value of the operand01 is :",operand01)
print("calling the func")
paramchange(operand01)
print("after calling the func")
print("the new value of operand01 is :",operand01)
"""


#func list example
"""
def add2list(mylist):
    print("the given list is :",mylist)
    print("address of mylist before append: ",id(mylist))
    addvalue=int(input("please enter the new to be added: "))
    mylist.append(addvalue)
    print("the updated list is : ",mylist)
    print("address of mylist after append: ",id(mylist))
    return
    
list01=[0,1,2,3,4,5,6]
print("address of mylist before calling func: ",id(list01))
choice=input("do you want to add any values to list(y/n):")
if choice=='y' or choice=='Y' : 
    add2list(list01)
    print("address of mylist after calling func: ",id(list01))
else : print("you choiced not to add any items to the list")
print("the list after calling the func is :",list01)
"""

#func parameters example
"""
def incrementvalue(invalue):
    print("the original value assinged to formal parameter is :",invalue)
    invalue+=10
    print("the incremented value is :",invalue)
    return

invalue=int(input("please enter the value: "))
print("the given value is : ",invalue)
incrementvalue(invalue)
print("the value after returning from the function call is :",invalue)
"""


#func students data2
"""
def studentsmarks():
    mathsmarks=float(input("please enter the marks obtained in maths : "))
    englishmarks=float(input("please enter the marks obtained in english : "))
    physicsmarks=float(input("please enter the marks obtained in physics : "))
    chemistrymarks=float(input("please enter the marks obtained in chemistry : "))
    totalofthestudent(mathsmarks,englishmarks,physicsmarks,chemistrymarks)
    return 
def totalofthestudent(mathsmarks,englishmarks,physicsmarks,chemistrymarks):
    totalmarks=mathsmarks+englishmarks+physicsmarks+chemistrymarks
    print("the total marks obtained by the student is :",totalmarks) 
    percentofstudent(totalmarks,total)
    return 
def percentofstudent(totalmarks,total):
    percent=(totalmarks/(total*4))*100
    print("the percentage obtained is :",percent,"%")
    return 
    
print("the process is ready to enter your student data")
total=int(input("please enter the maximum marks per subject : "))
loop=True
while loop==True:
    studentsmarks()
    choice=input("do you want to enter another students data (y/n): ")
    if choice!='y' or choice!='Y' :
        loop=False
"""

#func parameters types 4
#default argument
"""
def addvalues(operand01,operand02=0):
   #this is an example of with accepting parameters and not returning any values
  
   result=operand01+operand02
   print("the sum of the given two numbers is :",result)
   
   return

operand01=int(input("please enter the first value : "))
operand02=int(input("please enter the second value : "))
addvalues(operand01)
"""

#func args example
#passing parameters dynamically at run time
"""
def addvalues(*args):
    calculatesum=0
    for myvalueindex in args:
        print("the value read is :",myvalueindex)
        calculatesum+=myvalueindex
        print("the total sum of all the arguments is : ",calculatesum)
    return
operand01=int(input("please enter the first number : "))
operand02=int(input("please enter the second number : "))
operand03=int(input("please enter the thirdnumber : "))
operand04=int(input("please enter the fourth number : "))
operand05=int(input("please enter the fifth number : "))
addvalues(operand01,operand02,operand03,operand04,operand05)
"""


#func sumofseries forloop
"""
def normalseriessum(param01,param02):
    print("calculating the sum of numbers in given range")
    if param01>param02:
        returnsum=0
        for loopindex in range (param01,param02,-1):
            returnsum+=loopindex
        return returnsum
    else :
        returnsum=0
        for i in range (param01,param02):
            returnsum+=i
        return returnsum
        
startrange=int(input("please enter the number to start with : "))
endrange=int(input("please enter the number to end with : "))

finalsum=normalseriessum(startrange,endrange)
print("the final sum of numbers in given range is :",finalsum)
"""