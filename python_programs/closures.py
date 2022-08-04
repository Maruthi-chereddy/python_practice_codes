#__name__,dir()
'''
import os 
os.system("cls")

def outerfunction():
    outervar=25
    def innerfunction():
        innervar=35
        outervar=45
        print(outervar)
        return 
        
    innerfunction()
    
    print(outervar)
    
    
print("\nmain scope of the application begins from here")
print("\n the name of the module in exceution is :",__name__)
print("\nall the identifiers operating under the",__name__,"module are",dir())
print("\nall the identifiers operating under the",__name__,"module are",dir())
print(outerfunction())


#closure basic 1
import os 
os.system("cls")

def outerfunction():
    outervar="enclosing scope"
    print(outervar)
    def innerfunction():
        print("inner scope",outervar)
        
        
    innerfunction()
    
    
if __name__=="__main__":
    outerfunctionobj=outerfunction
    print("outerfunction statement :")
    outerfunction()
    print("duplicate is :")
    outerfunctionobj()
    
#closure basic 2
import os 
os.system("cls")
def outerfunction():
    outervar="hello i am replying from enclosing scope"
    #print(outervar)
    def innerfunction():
        print("inner scope:",outervar)
        
    return innerfunction()
    
    
if __name__=="__main__":
    outerfunctionobj=outerfunction
    print("outerfunction statement :")
    outerfunction()
    print("duplicate is :")
    outerfunctionobj()


#closure basic 3

import os 
os.system("cls")
def outerfunction():
    outervar="hello i am replying from enclosing scope"
    #print(outervar)
    def innerfunction():
        print("inner scope:",outervar)
        
    return innerfunction()
    
    
if __name__=="__main__":
    outerfunctionobj=outerfunction
    print("outerfunction statement :")
    outerfunction()
    print("duplicate is :")
    outretvalue=outerfunctionobj
    print('hii')
    print("outretvalue",outretvalue())

#closure basic 4

import os
os.system("cls")
def outerfunction():
    outervar="enclosing scope"
    print(outervar)
    def innerfunction():
        print("inner scope,outervar")
        
        
    innerfunction()
    
    
if __name__=="__main__":
    outerfunctionobj=outerfunction
    print("outerfunction statement :",outerfunction())
    print("duplicate is :")
    outretvalue=outerfunctionobj
    print("outretvalue:",outretvalue)
    print("outretvaluefunc:",outretvalue())

#closure example 2

import os
os.system("cls")

def addbyvalue(invalue):
    print("given value is:",invalue)
    def valueincrease(inbasevalue):
        print("given base value:",inbasevalue)
        finalresult=inbasevalue+invalue
        return finalresult
    return valueincrease
    
addvaluefunctionobj=addbyvalue(10)
finalretreference=addvaluefunctionobj(20)
print("return of outerfunction:",finalretreference)
#print(finalretreference(40))

#closure example 3

import os
os.system("cls")

def addbyvalue(invalue):
    print("given value is:",invalue)
    def valueincrease(inbasevalue):
        print("given base value:",inbasevalue)
        finalresult=inbasevalue+invalue
        return finalresult
    return valueincrease
    
addvaluefunctionobj=addbyvalue
finalretreference=addvaluefunctionobj(20)
print("return of outerfunction:",finalretreference)
#raisedvalue=finalretreference(40)
print(finalretreference(40))


#closure example 4

import os 
os.system("cls")
def addbyvalue(invalue):
    print("given value is:",invalue)
    def valueincrease(inbasevalue):
        print("given base value:",inbasevalue)
        finalresult=inbasevalue+invalue
        return finalresult
    return valueincrease
    
addvaluefunctionobj=addbyvalue
value01=int(input("please enter the first value:"))
value02=int(input("please enter the decond value to add:"))
finalretreference=addvaluefunctionobj(value01)
#print("return of outerfunction:",finalretreference)
#raisedvalue=finalretreference(value02)
print(finalretreference(value02))


#closure example 5

def addbyvalue(invalue):
    print("given value is:",invalue)
    def valueincrease(inbasevalue):
        print("given base value:",inbasevalue)
        finalresult=inbasevalue+invalue
        return finalresult
    return valueincrease
    
addvaluefunctionobj=addbyvalue
value01=int(input("please enter the first value:"))
value02=int(input("please enter the decond value to add:"))
finalretreference=addvaluefunctionobj(value01)
#print("return of outerfunction:",finalretreference)
raisedvalue=finalretreference(value02)
print(raisedvalue)


#closure example 6

import os
os.system("cls")

def multipliedvalue(inmultipliervalue):
    print("given value is :",inmultipliervalue)
    def multiplyingvalue(multipliervalue):
        print("given value to multiple is:",multipliervalue)
        result=inmultipliervalue*multipliervalue
        return result
        
    
    return multiplyingvalue
value01=int(input("please enter the first value:"))
value02=int(input("please enter the second value:"))

obj=multipliedvalue(value02)
output=obj(value01)
print("the final output is :",output)  

# closure example 7
 SAME AS example 6 where ""result=inmultipliervalue*multipliervalue
        return result"" replaced with ""return inmultipliervalue*multipliervalue""
        
        remaining part remains same

# closure example

import os
os.system("cls")

def outerfunction():
    outermsg="hello outer"
    def innerfunction():
        print("inner with outermsg",outermsg)
        return 111
        
    return innerfunction()
    
outerfunctionobj=outerfunction
print("calling outerfunction",outerfunction())
print("calling outerfunctionobj",outerfunctionobj)

outerretvalue=outerfunctionobj()
print(outerretvalue)


#closure increment 1

import os
os.system("cls")

def offsetincrement(inoffervalue):
    def applyoffset():
        print(f'the value {inoffervalue} offset by 10 is {inoffervalue+10}')
        return 
    return applyoffset
    
    
basevalue=int(input("please enter the value to be incremented: "))

iterlevel=int(input("please enter no of times the offset has to be applied:"))

while iterlevel>0:
    offsetfunctionobj=offsetincrement(basevalue)
    basevalue=basevalue+10
    offsetfunctionobj()
    iterlevel=iterlevel-1
  
  
#closure increment 3

import os
os.system("cls")

def applyincrement(instartvalue):
    print("given value is:",instartvalue)
    def incrementlevel(inincrementvalue):
        print("given value is :",inincrementvalue)
        return instartvalue+inincrementvalue
    return incrementlevel
    
print("closure calling 01")
varstartvalue=int(input("please enter the start value"))
varincrementvalue=int(input("please enter the increment value"))
applyincrementobj01=applyincrement(varstartvalue)
finalvalue=applyincrementobj01(varincrementvalue)
print(f'the final increment value with start value {varstartvalue} app;ied with increment of{varincrementvalue} is {finalvalue}')


print("closure calling 02")
varstartvalue=int(input("please enter the start value"))
varincrementvalue=int(input("please enter the increment value"))
applyincrementobj02=applyincrement(varstartvalue)
finalvalue=applyincrementobj02(varincrementvalue)
print(f'the final increment value with start value {varstartvalue} app;ied with increment of{varincrementvalue} is {finalvalue}')


#closure increment 4

import os
os.system("cls")

def applyincrement(instartvalue):
    print("given value is:",instartvalue)
    def incrementlevel(inincrementvalue):
        print("given value is :",inincrementvalue)
        return instartvalue+inincrementvalue
    return incrementlevel
    
print("closure calling 01")
varstartvalue=int(input("please enter the start value"))
varincrementvalue=int(input("please enter the increment value"))
applyincrementobj01=applyincrement(varstartvalue)
finalvalue=applyincrementobj01(varincrementvalue)
print(f'the final increment value with start value {varstartvalue} app;ied with increment of{varincrementvalue} is {finalvalue}')


#closure increment 5

import os
os.system("cls")

def applyincrement(instartvalue):
    print("given value is:",instartvalue)
    def incrementlevel(inincrementvalue):
        print("given value is :",inincrementvalue)
        return instartvalue+inincrementvalue
    return incrementlevel
    
    
applyincrementobj=applyincrement(10)
print("the data type of \"applyincrementobj\" is :",(type(applyincrementobj)))
print("the reference pointed by object  \"applyincrementobj\" is : %s"%(applyincrementobj.__closure__))
print("the data type of \"applyincrementobj : cell\"attribute is :%s"%(type(applyincrementobj.__closure__[0])))
print("the data type of \"applyincrementobj : cell\"attributepointing  is :%s"%(type(applyincrementobj.__closure__[0].cell_contents)))
print("the data that is pointed by \"applyincrementobj : cell\" attribute is %s" %(applyincrementobj.__closure__[0].cell_contents))
'''

#closure type increment 1

import os
os.system("cls")

def applyincrement(instartvalue):
    print("given value is:",instartvalue)
    def incrementlevel(inincrementvalue):
        print("given value is :",inincrementvalue)
        return instartvalue+inincrementvalue
    return incrementlevel
    
    
applyincrementobj01=applyincrement(10)
print("the data type of \"applyincrementobj01\" is :",(type(applyincrementobj01)))
print("the reference pointed by object  \"applyincrementobj01\" is : %s"%(applyincrementobj01.__closure__))
print("the data type of \"applyincrementobj01 : cell\"attribute is :%s"%(type(applyincrementobj01.__closure__[0])))
print("the data type of \"applyincrementobj01 : cell\"attributepointing  is :%s"%(type(applyincrementobj01.__closure__[0].cell_contents)))
print("the data that is pointed by \"applyincrementobj01 : cell\" attribute is %s" %(applyincrementobj01.__closure__[0].cell_contents))


applyincrementobj02=applyincrement(10)
print("the data type of \"applyincrementobj02\" is :",(type(applyincrementobj02)))
print("the reference pointed by object  \"applyincrementobj02\" is : %s"%(applyincrementobj02.__closure__))
print("the data type of \"applyincrementobj02 : cell\"attribute is :%s"%(type(applyincrementobj02.__closure__[0])))
print("the data type of \"applyincrementobj02 : cell\"attributepointing  is :%s"%(type(applyincrementobj02.__closure__[0].cell_contents)))
print("the data that is pointed by \"applyincrementobj02 : cell\" attribute is %s" %(applyincrementobj02.__closure__[0].cell_contents))
