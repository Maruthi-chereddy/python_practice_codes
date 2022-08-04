import os
os.system('cls')

#name,dir
"""
def outerfunc():
    outervar=25
    print(__name__)
    print(dir())
    
    def innerfunc():
        innervar=35
        outervar=45
        print(innervar,outervar)
        return
    innerfunc()
    return
print(__name__)
print(dir())
outerfunc()
"""


#global basic 2
#UnboundLocalError: local variable 'globalcount' referenced before assignment
"""
globalcount=0
def changecounter():
    print(globalcount)
    globalcount+=1
    return
print(globalcount)
changecounter()
print(globalcount)
"""


#global example 1
"""
globalcount=0
def changecounter():
    global globalcount
    print(globalcount)
    globalcount+=1
    return
print(globalcount)
changecounter()
print(globalcount)
"""


#global example 2
"""
globalcount=0
def changecounter():
    global globalcount
    print(globalcount)
    globalcount+=1
    return globalcount
print(globalcount)
finalout=changecounter()
print(finalout)
"""


#global example 4
"""
def changecounter():
    global globalcount
    globalcount=25
    return globalcount
finalout=changecounter()
print(finalout)
"""


#global example 5
"""
globalcount=0
def changecounter(param01):
    print(param01)
    
    return param01+1
print(globalcount)
globalcount=changecounter(globalcount)
print(globalcount)
"""


#global example 6
"""
def changecounter():
    print(dir())
    myvar=25
    global globalcount
    globalcount=25
    print(globalcount)
    print(dir())
    return globalcount
print(dir())
finalout=changecounter()
print(dir())
print(finalout)
"""


#nonlocal basic 2
#NameError: name 'outmsg' is not defined
"""
def outerfunc():
    outmsg="hello! maruthi"
    def innerfunc():
        print("from innerfunc  calling outmsg",outmsg)
        return
    innerfunc()
    return
outerfunc()
print(outmsg)
"""


#nonlocal basic
#UnboundLocalError: local variable 'outvar' referenced before assignment
"""
def outerfunc():
    outvar=24
    def innerfunc():
        outvar+=16
        return
    innerfunc()
    return
outerfunc()
"""


#nonlocal example 1
"""
def multiplierresult(invalue):
    finalresult=0
    def executemultiplication(inmultiplylevel):
        nonlocal finalresult
        
        while inmultiplylevel>0:
            finalresult+=invalue*inmultiplylevel
            inmultiplylevel-=1
        return finalresult
    return executemultiplication
basevalue=int(input("please enter the base value for applying the multiplier:"))
multiplefuncobj=multiplierresult(basevalue)
levelvalue=int(input("please enter the level value for executing the multiplier:"))
print(multiplefuncobj(levelvalue))
"""


#nonlocal example 2
"""
def si(param01,param02,param03):
    si=0
    def calculatesi():
        nonlocal si
        si=(param01*param02*param03)/100
        return si
    return calculatesi
principle=int(input("please enter the principle amount:"))
interest=int(input("please enter the rate of amount:"))
timeperiod=int(input("please enter the time period:"))
siobj=si(principle,interest,timeperiod)
interestval=siobj()
print(interestval)
print(interestval+principle)
"""


#nonlocal example 3

"""
def si(param01,param02):
    si=0
    def calculatesi(param03):
        nonlocal si
        while param03>0:
            si=(param01*param02*param03)/100
            print(param01,param02,param03)
            param03-=1
        return si
    return calculatesi
principle=int(input("please enter the principle amount:"))
interest=int(input("please enter the rate of amount:"))
timeperiod=int(input("please enter the time period:"))
siobj=si(principle,interest)
interestval=siobj(timeperiod)
print(interestval)
print(interestval+principle)
"""