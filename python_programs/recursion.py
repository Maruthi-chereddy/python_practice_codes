
import os 
os.system('cls')

#func sumofseries recursion
"""
def recursiveseriessum(param01,param02):
    if (param01>param02):
        return 0
        
    else:
        nextval=param01+1
        currentsum=recursiveseriessum(nextval,param02)
        returnfinalseriessum=param01+currentsum
        return returnfinalseriessum
startrange=int(input("please enter the number to start with : "))
endrange=int(input("please enter the number to end with : "))

finalsum=recursiveseriessum(startrange,endrange)
print("the final sum of numbers in given range is :",finalsum)
"""


#func sumofseries recursion 2
"""
def recursiveseriessum(param01,param02):
    if (param01>param02):
        return 0
        
    else:
        #nextval=param01+1
        #currentsum=recursiveseriessum(nextval,param02)
        #returnfinalseriessum=param01+currentsum
        return param01+recursiveseriessum(param01+1,param02)
startrange=int(input("please enter the number to start with : "))
endrange=int(input("please enter the number to end with : "))

finalsum=recursiveseriessum(startrange,endrange)
print("the final sum of numbers in given range is :",finalsum)
"""

#func naturalnum ifelse
"""
def generateseries(inparam01):
    if (inparam01>1):
        generateseries(inparam01-1)
        print(inparam01,",",end=' ')
    else:
        print(inparam01,',',end=' ')
    return
generatevalues=int(input("please enter the number of natural numbers to be generated: "))
print("generating the natural numbers from 1 to :",generatevalues)
generateseries(generatevalues)
"""

#func factorial recursion
"""
def calculatefactorial(inparam):
    if inparam==0:
        return 1
    else:
        return inparam*calculatefactorial(inparam-1)
        
factorialvalue=int(input("please enter the number to calculate its factorial: "))
finalresult=calculatefactorial(factorialvalue)
print("the factorial of given value is : ",finalresult)
"""

#func tenpower
"""
def tenpower(inparam):
    if inparam==0:
        return 1
    else:
        return tenpower(inparam-1)*10
        
invalue=int(input("please enter the number to calculate its tenpower: "))
finalresult=tenpower(invalue)
print("the tenpower of given value is : ",finalresult)
"""

#func GCD recursion
"""
def findgcd(inparam01,inparam02):
    if inparam02==0:
        return inparam01
    else:
        return findgcd(inparam02,(inparam01%inparam02))
        
infirstvalue=int(input("please enter the first number to calculate gcd:"))
insecondvalue=int(input("please enter the second number to calculate gcd:"))
outgcdvalue=findgcd(infirstvalue,insecondvalue)
print("the gcd of ",infirstvalue,"and",insecondvalue,"is:",outgcdvalue)
"""


#func factorial recursion 2
"""
def calfactorial(inparam):
   
    if inparam==0:
        return 1
    else:
        return inparam*calfactorial(inparam-1)
        #currentfactvalue=inparam*calfactorial(inparam-1)
        #return currentfactvalue
    
factorialvalue=int(input("please enter the number to find the factorial of : "))

if factorialvalue==0:
    print("zero's factorial cannot be calculated")
    sys.exit
elif factorialvalue==1:
    print("the factorial of 1 is 1")
    sys.exit
else:
    finalout=calfactorial(factorialvalue)
    print("the factorial of given number is:",finalout)
    """
    
#func fibanocci
"""
def getfibonacci(inparam):

    fibanoccivalue,stepvalue=0,1
    print("the fibanocci series upto ",inparam,"is :0,",end=" ")
    for i in range(inparam):
        fibanoccivalue,stepvalue=stepvalue,fibanoccivalue+stepvalue
        print(fibanoccivalue,",",end='')
    return
value=int(input("please enter the number of fibanocci numbers to be printed :"))
if value==0:
    print("0")
elif value==1:
    print("0,1")
elif value==2:
    print("0,1,1")
else:
    getfibonacci(value)
    """
    
#func fibanocci
#unsatisfied result
"""
def getfibonacci(inparam):

    fibanoccivalue,stepvalue=0,1
    print("the fibanocci series upto ",inparam,"is :0,",end=" ")
    for i in range(inparam):
        fibanoccivalue,stepvalue=stepvalue,fibanoccivalue+stepvalue
        return fibanoccivalue
value=int(input("please enter the number of fibanocci numbers to be printed :"))
if value==0:
    print("0")
if value==1:
    print("0,1")
if value==2:
    print("0,1,1")

print(getfibonacci(value))
"""

#func fibonacci recursion
#func fibanocci
"""
def getfibonacci(inparam):
    if inparam<=1:
        return inparam
    else:
        return (getfibonacci(inparam-1)+getfibonacci(inparam-2))
    
value=int(input("please enter the number of fibanocci numbers to be printed :"))
if value==0:
    print("0")
elif value==1:
    print("0,1")
elif value==2:
    print("0,1,1")
for i in range(value):
    print(getfibonacci(i))
    """

#func multiples recursion
"""
def generatemultiple(param01,param02):
    if param01==1:
        return param02
    else:
        return generatemultiple(param01-1,param02)+param02
multipleseries=int(input("please enter the value for generating the multiples:"))
print("generating series with the multiples of ",multipleseries,"are:",end='')
for seriesindex in range(1,11):
    print(generatemultiple(seriesindex,multipleseries),end=',')
    
print()
"""

#recursion offset
"""
def recursiveseriessum(instart,inend,basevalue):
    if (instart>inend):
        return basevalue
    return recursiveseriessum(instart+1,inend,instart+basevalue)
start=int(input("please enter the initial value to calculate the sum of series:"))
end=int(input("please enter the end value :"))
outfinal=recursiveseriessum(start,end,0)
print("the sum of series from",start,"to",end ,"is",outfinal)
"""


#tail recursion
#factorial example

def calfactorial(inparam,basevalue):
   
    if inparam==0:
        return basevalue
    else:
        return calfactorial(inparam-1,inparam*basevalue)
        
    
factorialvalue=int(input("please enter the number to find the factorial of : "))

if factorialvalue==0:
    print("zero's factorial cannot be calculated")
    sys.exit
elif factorialvalue==1:
    print("the factorial of 1 is 1")
    sys.exit
else:
    finalout=calfactorial(factorialvalue,1)
    print("the factorial of given number is:",finalout)