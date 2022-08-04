import os 
os.system('cls')

#pre-decorator 1

import os
os.system("cls")
'''
def myouterfunction(infunction):
    def innerfunction():
        print("before calling the infunction")
        infunction()
        print("after calling the infunction")
    return innerfunction
def raisemessage():
    print("this is infunction")
    
if __name__=="__main__":
    output=myouterfunction(raisemessage)
    output()


#pre-decorator 2
#error
import os
os.system("cls")

def myouterfunction(infunction):
    def innerfunction():
        print("before calling the infunction")
        infunction()
        print("after calling the infunction")
    return innerfunction
def raisemessage():
    print("this is infunction")
    
if __name__=="__main__":
    infunction=input("please enter the name of the function:")
    output=myouterfunction(infunction)
    output()


#pre-decorator 4

import os
os.system("cls")

def myouterfunction(infunction):
    def innerfunction():
        print("before calling the infunction")
        infunction()
        print("after calling the infunction")
        return 'hii'
    return innerfunction
def raisemessage():
    print("this is infunction")
    
if __name__=="__main__":
    output=myouterfunction(raisemessage)
    print("the message returned is:",output())


#pre-decorator basic multiplication

import os
os.system("cls")

def applymultiplier(inparam01,inparam02):
    print(f"the given values for applying multiplier are:{inparam01} and {inparam02}")
    return inparam01*inparam02
    
if __name__=="__main__":
    invalue01=int(input("please enter the value to be multiplied:"))
    invalue02=int(input("please enter the value to be multiplied:"))
    finalvalue=applymultiplier(invalue01,invalue02)
    print(f"the result of {invalue01} and {invalue02} multiplied is {finalvalue}")

 
#day schedule


from datetime import datetime


currenthour=datetime.now().today
print("the current hour in the clock is:",currenthour())

#pre-decorator greetingmessage

def greetingmessage01(inname):
    return f'hello! {inname}'
def greetingmessage02(inname):
    return f'hai{inname},this is a great day'
def greetperson(greetfunctionname):
    return greetfunctionname('maruthi')
messagetype=input("please enter the type of greeting message you need(b/a) : ")
if messagetype=='a':
    print(greetperson(greetingmessage02))
if messagetype=='b':
    print(greetperson(greetingmessage01))
   
    
    
#pre-decorator greetingmessage 2

def greetperson(param):
    def greetingmessage01(inname):
        return f'hello! {inname}'
    def greetingmessage02(inname):
        return f'hai{inname},this is a great day'
    if param=='a':
        return greetingmessage02
    else:
        return greetingmessage01
   
messagetype=input("please enter the tyoe of greeting message you need(b/a) : ")
name=input("please enter your name: ")
if messagetype=='a':
    advanceobj=greetperson(messagetype)
    print(advanceobj(name))
elif messagetype=='b':
    basicobj=greetperson(messagetype)
    print(basicobj(name))
else:
    print("please enter a valid input")
    

#pre-decorator multiplier
#partial functions

from functools import partial

def applymultiplier(inparam01,inparam02):
    print(inparam01)
    print(inparam02)
    return inparam01*inparam02
invalue01=int(input("please enter the value to be multiplied: "))
print("\n1.apply multiplication\n2.double the value\n3.triple the value\n4.quadra\n5.pentaple\n0.exit")
readchoice=int(input("please enter your choice: "))

if readchoice==1:
    invalue02=int(input("pleas enter the value to multiply :"))
    finalvalue=applymultiplier(invalue01,invalue02)
    print(finalvalue)
elif readchoice==2:
    doublevalue=partial(applymultiplier,2)
    print(doublevalue(invalue01))
    
elif readchoice==3:
    triplevalue=partial(applymultiplier,3)
    print(triplevalue(invalue01))
elif readchoice==4:
    quadravalue=partial(applymultiplier,4)
    print(quadravalue(invalue01))
elif readchoice==5:
    pentavalue=partial(applymultiplier,5)
    print(pentavalue(invalue01))
else:
    sys.exit()

    
#pre-decorator simple interest 

from functools import partial

def calcsi(principle,interest,time):
    print(principle, interest, time)
    return (principle*interest*time)/100
def yearone(principle,interest):
    return calcsi(principle,interest,1)
def yeartwo(principle,interest):
    return calcsi(principle,interest,2)
def yearthree(principle,interest):
    return calcsi(principle,interest,3)
def yearfour(principle,interest):
    return calcsi(principle,interest,4)
    
    
amount=int(input("please enter the amount: "))
rate=float(input("please enter the rate : "))
timeperiod=float(input("please enter the time taken : "))

finalvalue=partial(calcsi,amount)
print("interest for the given details is : ",finalvalue(rate,timeperiod))

'''
#decorator 1

def myouterfunc(infuncname):
    def myinnerfunc():
        print("operationas before the function is called")
        infuncname()
        print("operations after the function is called")
    return myinnerfunc()
@myouterfunc
def callfunc():
    print("hello this func is meddling in between the main func call")
    
#callfunction=myouterfunc(callfunc)
#print(callfunction)
callfunc

'''
#decorator 2

def decodiv(infuncname):
    def divvalidate(num,denom):
        print("the given value for the numerator :",num)
        print("the given value for the denominator : ",denom)
        if denom==0:
            print("sorry division cannot be done")
            return
        return infuncname(num,denom)
    return divvalidate
@decodiv
def getquotient(pnum,pdenom):
    print("the quotient is : ",(pnum/pdenom))
innum=float(input("please enter the numerator value : "))
indenom=float(input("please enter the denominator value : "))
getquotient(innum,indenom)


#decorator 3

def myouterfunc(infuncname):
    def myinnerfunc():
        print("operationas before the function is called")
        print("reference function is :",infuncname.__name__)
        infuncname()
        print("operations after the function is called")
        print("reference function is :",infuncname.__name__)
    return myinnerfunc
@myouterfunc
def callfunc():
    print("hello this func is meddling in between the main func call")
    
#callfunction=myouterfunc(callfunc)
#print(callfunction)
callfunc()


#decorator math example

from math import sin,cos,tan
def infuncing(infuncname):
    def infuncwrapper(inparam):
        print("reference func before the call:",infuncname.__name__)
        mathresult=infuncname(inparam)
        print("the",infuncname.__name__,"applied wit value of",inparam,'is:',mathresult)
        print("the reference func after the call :",infuncname.__name__)
    return infuncwrapper
    
sin=infuncing(sin)
cos=infuncing(cos)
tan=infuncing(tan)

for i in (sin,cos,tan):
    i(0)
    


#decorator random example

from random import random,randint,choice

def infuncing(infuncname):
    def infuncwrapper(*args):
        print("reference func before the call:",infuncname.__name__)
        mathresult=infuncname(*args)
        print(f'the {infuncname.__name__} is {mathresult}')
        print("reference func after the call:",infuncname.__name__)
        return
    return infuncwrapper
random=infuncing(random)
randint=infuncing(randint)
choice=infuncing(choice)
random()
randint(0,10)
choice([1,2,3,4,5])


#decorator with args

def myouterfunc(infuncname):
    def myinnerfunc(*args):
        print("*"*50)
        infuncname(*args)
        print("operations after the function is called")
    return myinnerfunc
@myouterfunc
def callfunc(name):
    print(f"hello!{name}")
    
inname=input("please enter the name: ")
callfunc(inname)


#decorator 4

def makeuppercase(string):
    def change():
        print("printing the upper case")
        appliedstring=string()
        return appliedstring.upper()
    return change
@makeuppercase
def outmessage():
    return "we are totally an e otional generation"
print("calling func normally:",outmessage())


#decorator 5

def makeuppercase(string):
    def change():
        appliedstring=string()
        return appliedstring.upper()
    return change
@makeuppercase
def outmessage():
    return "we are totally an e otional generation"
changecase=outmessage()
print("calling func normally:",changecase)


#multiple decorators

def makeuppercase (instringfunc):
    def changeuc():
        appliedstring=instringfunc()
        return appliedstring.upper()
    return changeuc
def applystringsplit(instringfunc):
    def stringsplitter():
        instringsplitter = instringfunc()
        return instringsplitter.split()
    return stringsplitter

@applystringsplit
@makeuppercase
def outmessage():
    infullname=input("please enter the name : ")
    return infullname
print("output",outmessage())


#decorator 6

def makeuppercase(string):
    def changeuc(instringfunc):
        def change():
            
            return string.upper()+","+instringfunc().upper()
        return change    
    return changeuc
@makeuppercase("maruthi")
def outmessage():
    return "we are totally an emotional generation"
print("calling func normally:",outmessage())



#decorator 7

import math 
import time

def costcalc(infuncname):
    def funcexecuter(*args):
        starttime=time.time()
        infuncname(*args)
        endtime=time.time()
        print("the cost of the func is :",infuncname.__name__,(endtime-starttime))
    return funcexecuter
@costcalc
def factorial(invalue):
    print(math.factorial(invalue))
    
invalue=int(input("please enter the value for calculating factorial : "))
factorial(invalue)
'''