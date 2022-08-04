import os
os.system('cls')

'''
#constructor basic

class sample:
    samplevalue=10
    
sampleobject=sample()

print(sampleobject.samplevalue)

#constructor basic 2

class sample:
    samplevalue=None
    def __init__(self):
        self.samplevalue=10
    
sampleobject=sample()

print(sampleobject.samplevalue)


#constructor assining data

class sample:
    samplevalue=20
    def __init__(self):
        self.samplevalue=10
    
sampleobject=sample()

print(sampleobject.samplevalue)
print(sample.samplevalue)


#constructor getters, setters

class sample:
    samplevalue=20
    def __init__(self):
        self.samplevalue=10
    def getdata(self): 
        return self.samplevalue
        #return self.__samplevalue error
    
sampleobject=sample()

print(sampleobject.samplevalue)
print(sample.samplevalue)
print(sampleobject.getdata())


#constructors getters,setters

class sample:
    samplevalue=None
    def __init__(self):
        self.samplevalue=10
    def getsamplevalue(self): 
        self.__samplevalue=int(input())
    def putsamplevalue(self):
        print(self.samplevalue)
    
sampleobject=sample()

print(sampleobject.samplevalue)
print(sample.samplevalue)
sampleobject.getsamplevalue()
sampleobject.putsamplevalue()


#constructor id ref

class sample:
    samplevalue=20
    def __init__(self):
         print(id(self))
        self.samplevalue=10
    
sampleobject=sample()

print(id(sampleobject))
print(sampleobject.samplevalue)
print(sample.samplevalue)
print(id(sample.samplevalue))
print(id(sample))
print(id(sampleobject.samplevalue))


#constructor assining data 2

class sample:
    __samplevalue=20
    def __init__(self):
        print(id(self))
        self.__samplevalue=10
    
sampleobject=sample()

print(id(sampleobject))
#print(sampleobject.samplevalue)  error
print(sample.__samplevalue)  
#print(id(sample.__samplevalue)) error
#print(id(sample.samplevalue)) error
print(id(sample))


#constructor private

class sample:
    classsamplevalue=20
    def __init__(self):
        self.__samplevalue=10
    def getdata(self): 
        return self.__samplevalue
    
sampleobject=sample()

#print(sampleobject.__samplevalue) #error
print(sample.classsamplevalue)
print(sampleobject.classsamplevalue)
print(id(sample.classsamplevalue))
print(id(sampleobject.classsamplevalue))
print(sampleobject.getdata())
print(sample.getdata(sampleobject))

#constructors private 2 

class sample:
    
    def __init__(self):
        self.__samplevalue=10
    def getsamplevalue(self): 
        self.__samplevalue=int(input())
        return self.__samplevalue
    def putsamplevalue(self):
        return print(self.__samplevalue)   
    
sampleobject=sample()
sampleobject.putsamplevalue()
#print(sampleobject.samplevalue) error
#print(sample.samplevalue) error
sampleobject.getsamplevalue()
sampleobject.putsamplevalue()


#constructors private 3

class sample:
    
    def __init__(self):
        self.__samplevalue=10
        self.putsamplevalue()
    def getsamplevalue(self): 
        self.__samplevalue=int(input())
    def putsamplevalue(self):
        print(self.__samplevalue)
    
sampleobject=sample()

#print(sampleobject.samplevalue)
#print(sample.samplevalue) error
print(sampleobject.getsamplevalue())
print(sampleobject.putsamplevalue())


#constructors private 4

class sample:
    
    def __init__(self):
        self.__samplevalue=10
        self.getsamplevalue()
        self.putsamplevalue()
    def getsamplevalue(self): 
        self.__samplevalue=int(input())
    def putsamplevalue(self):
        print(self.__samplevalue)
    
sampleobject=sample()

#print(sampleobject.samplevalue)
#print(sample.samplevalue) error
#print(sampleobject.getsamplevalue())
#print(sampleobject.putsamplevalue())

#constructor param 1

class sample:
    __samplevalue=None
    
    def __init__(self,insamplevalue):
        self.__samplevalue=insamplevalue
        
    def getsample(self):
        return self.__samplevalue
        
sampleobject01=sample(10)
print(sampleobject01.getsample())
sampleobject02=sample(20)
print(sampleobject02.getsample())
sampleobject03=sample(30)
print(sampleobject03.getsample())


#constructor basic 3

class sample:
    __samplevalue=None
    
    def __init__(self,insamplevalue):
        self.__samplevalue=insamplevalue
        
    def getsample(self):
        return self.__samplevalue
        
sampleobject01=sample(10)
print(sampleobject01)
print(sampleobject01.getsample())
sampleobject02=sample(20)
print(sampleobject02)
print(sampleobject02.getsample())
sampleobject03=sample(30)
print(sampleobject03)
print(sampleobject03.getsample())
print(sampleobject02.getsample())
print(sampleobject01.getsample())



#constructor private,personal

class sample:
    __samplevalue01=None
    samplevalue02=None
    
    def __init__(self,insamplevalue):
        self.__samplevalue01=insamplevalue
        
    def getsample(self):
        return self.__samplevalue01
        
sampleobject01=sample(10)
print(sampleobject01.getsample())
sampleobject01.samplevalue02=25
print(sampleobject01.samplevalue02)


#constructor handcoding

class sample:
    __samplevalue01=None
    
    def __init__(self,insamplevalue):
        self.setsample(insamplevalue)
    def setsample(self,inparam01):
        self.__samplevalue01=inparam01
    def getsample(self):
        return self.__samplevalue01
invalue=int(input("enter a value :"))        
sampleobject01=sample(invalue)
print(sampleobject01.getsample())
invalue01=int(input("enter a new number :"))
sampleobject01.setsample(invalue01)
print(sampleobject01.getsample())

#constructor handcoding 2

class sample:
    __samplevalue01=None
    
    def __init__(self):
        insamplevalue=10
        self.setsample(insamplevalue)
    def __init__(self,insamplevalue):
        self.setsample(insamplevalue)
    def setsample(self,inparam01):
        self.__samplevalue01=inparam01
    def getsample(self):
        return self.__samplevalue01
invalue=int(input("enter a value :"))        
sampleobject01=sample(invalue)
print(sampleobject01.getsample())
invalue01=int(input("enter a new number :"))
sampleobject01.setsample(invalue01)
print(sampleobject01.getsample())
'''