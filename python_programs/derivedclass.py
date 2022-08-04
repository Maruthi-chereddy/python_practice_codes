import os 
os.system('cls')
'''
#dervied class private 1

class baseclass:
    __baseclassfield=None
    
    def setbaseclassfield(self,inparam):
        self.__baseclassfield=inparam
        
    def getbaseclassfield(self):
        return self.__baseclassfield
        
class derivedclass(baseclass):
    __derivedclassfield=None
    
    def setderivedclassfield(self,inparam):
        self.__derivedclassfield=inparam
        return
        
    def getderivedclassfield(self):
        return self.__derivedclassfield
        
derivedclassobj=derivedclass()
inderivedvalue=int(input("enter value for derived class : "))
derivedclassobj.setderivedclassfield(inderivedvalue)

derivedclassobjvalue=derivedclassobj.getderivedclassfield()
print(derivedclassobjvalue)
'''
#derived class 2
# assinging data to the base class public member using derived class object is not a good practice
class baseclass:
    __baseclassfield=None
    
    def setbaseclassfield(self,inparam):
        self.__baseclassfield=inparam
        
    def getbaseclassfield(self):
        return self.__baseclassfield
        
class derivedclass(baseclass):
    __derivedclassfield=None
    
    def setderivedclassfield(self,inparam):
        self.__derivedclassfield=inparam
        return
        
    def getderivedclassfield(self):
        return self.__derivedclassfield
        
baseclassobj=baseclass()
inbasevalue=int(input("enter value for base class : "))
baseclassobj.setbaseclassfield(inbasevalue)

baseclassobjvalue=baseclassobj.getbaseclassfield()
print(baseclassobjvalue)

derivedclassobj=derivedclass()
inbasederivedvalue=int(input("enter value for base derived class : "))
derivedclassobj.setbaseclassfield(inbasederivedvalue)

basederivedclassobjvalue=derivedclassobj.getbaseclassfield()
print(basederivedclassobjvalue)

#baseclassobjvalue=baseclassobj.getbaseclassfield()
print(baseclassobjvalue)
'''
# derived class
#error

class baseclass:
    __baseclassfield=None
    
    def setbaseclassfield(self,inparam):
        self.__baseclassfield=inparam
        
    def getbaseclassfield(self):
        return self.__baseclassfield
        
class derivedclass(baseclass):
    __derivedclassfield=None
    
    def setderivedclassfield(self):
        baseclassmessagechoice=input("do you want to initiate base class members(y/n):")
        if baseclassmessagechoice=='y' or baseclassmessagechioce=='Y' :
            print("assining the data to base class ")
            inbasederivedvalue=int(input("enter value for base class level : "))
            baseclass.setbaseclassfield(inbasederivedvalue)
            print("assining the data to derived class")
            inderivedvalue=int(input("enter value for derived class level : "))
            self.__derivedclassfield=inderivedvalue
        else:
            print("assining the data to derived class")
            inderivedvalue=int(input("enter value for derived class level : "))
            self.__derivedclassfield=inderivedvalue
        return
        
    def getderivedclassfield(self):
        baseclassmessagechoice=input("do you want to initiate base class members(y/n):")
        if baseclassmessagechoice=='y' or baseclassmessagechoice=='Y' :
            print("accessing data form base class using derived class object")
            basederivedclassobjvalue=derivedclassobj.getbaseclassfield()
            print(basederivedclassobjvalue)
            print(self.__derivedclassfield)
        else:
            print(self.__derivedclassfield)
            
derivedclassobj=derivedclass()
derivedclassobj.setderivedclassfield()
derivedclassobjvalue=derivedclassobj.getderivedclassfield()
print(derivedclassobjvalue)


#derived class super() 1
class baseclass:
    __baseclassfield=None
    
    def setbaseclassfield(self,inparam):
        self.__baseclassfield=inparam
        
    def getbaseclassfield(self):
        return self.__baseclassfield
        
class derivedclass(baseclass):
    __derivedclassfield=None
    
    def setderivedclassfield(self):
        baseclassmessagechoice=input("do you want to initiate base class members(y/n):")
        if baseclassmessagechoice=='y' or baseclassmessagechioce=='Y' :
            print("assining the data to base class ")
            inbasederivedvalue=int(input("enter value for base class level : "))
            super().setbaseclassfield(inbasederivedvalue)
            print("assining the data to derived class")
            inderivedvalue=int(input("enter value for derived class level : "))
            self.__derivedclassfield=inderivedvalue
        else:
            print("assining the data to derived class")
            inderivedvalue=int(input("enter value for derived class level : "))
            self.__derivedclassfield=inderivedvalue
        return
        
    def getderivedclassfield(self):
        baseclassmessagechoice=input("do you want to initiate base class members(y/n):")
        if baseclassmessagechoice=='y' or baseclassmessagechoice=='Y' :
            print("accessing data form base class using derived class object")
            basederivedclassobjvalue=super().getbaseclassfield()
            print(basederivedclassobjvalue)
            print(self.__derivedclassfield)
        else:
            print(self.__derivedclassfield)
            
derivedclassobj=derivedclass()
derivedclassobj.setderivedclassfield()
derivedclassobjvalue=derivedclassobj.getderivedclassfield()
print(derivedclassobjvalue)


# inheritance 1

class baseclass:
    def __init__(self):
        print("hai ,this is from baseclass ")
class derivedclass(baseclass):
    def __init__(self):
        super().__init__()
        print("this is from derived class ")
        
derivedclassobject=derivedclass()

#inheritance 4
#error
class baseclass:
    __baseclassfield=10
    
    def showbasevalue(self):
        print("value from base class attribute is : ",self.__baseclassfield)
class middleclass(baseclass):
    __middleclassfiled=20
    
    def showmiddlevalue(self):
        print("value from middle class attribute is :",self.__middleclassfield)
        
class terminalclass(middleclass):
    __terminalclassfield=30
    
    def showterminalvalue(self):
        return print("value from terminal class attribute is :",self.__terminalclassfield)
        
terminalclassobj=terminalclass()


#inheritance 5
#error
class leftparentclass:
    leftparentfield=None
    
    def showvalue(self):
        print("value from leftparentclass attribute :",self.leftparentfield)
        
class rightparentclass:
    rightparentfield=None
    
    def showvalue(self):
        print("value from leftparentclass attribute :",self.rightparentfield)
        
class childclass(leftparentclass,rightparentclass):
    childclassfield=None
    
    def showvalue(self):
        leftparentclass.showvalue(self)
        rightparentclass.showvalue(self)
        print("value from leftparentclass attribute :",self.childclassfield)
        
childclassobj=childclass()


#inheritance repr()
#error
class sampleclass:
    def __init__(self,inparam01,inparam02):
        self.inparam01=inparam01
        self.inparam02=inparam02
        
    def __repr__(self):
        return (self.inparam01,self.inparam02)
        
sampleobject=sampleclass(4,5)
print(sampleobject)
print([sampleobject])


#inheritance str()

class sampleclass:
    def __init__(self,inparam01,inparam02):
        self.inparam01=inparam01
        self.inparam02=inparam02
        print(self.inparam01)
        print(self.inparam02)
        
sampleobject=sampleclass(4,5)

print(sampleobject.__str__())
'''