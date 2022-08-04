import os
os.system('cls')

# emptyclass copyobject reference
'''
class emptyclass :
    pass
    
emptyclassobject01=emptyclass()
print("id of emptyclass is : ",id(emptyclass))
print("reference address of class :",emptyclass())
print("reference addressof object 01 is : ",emptyclassobject01)
print("allocated object id of 01 is : ",id(emptyclassobject01))
print("associated class type of 01 is : ",type(emptyclassobject01))

emptyclassobject02=emptyclass()

print("reference addressof object 02 is : ",emptyclassobject02)
print("allocated object id of 02 is : ",id(emptyclassobject02))
print("associated class type of 02 is : ",type(emptyclassobject02))

emptyclassobject03=emptyclassobject02

print("reference addressof object 03 is : ",emptyclassobject03)
print("allocated object id of 03 is : ",id(emptyclassobject03))
print("associated class type of 03 is : ",type(emptyclassobject03))


#emptyclass attributes

class emptyclass :
    pass
    
emptyclassobject01=emptyclass()

emptyclassobject01.emptyobjid=1
emptyclassobject01.emptyobjfirstname="chereddy"
emptyclassobject01.emptyobjmiddlename="maruthi"
emptyclassobject01.emptyobjlastname="cm"
emptyclassobject01.emptyobjdob="30/01/2002"

print("emptyobjid : ",emptyclassobject01.emptyobjid)
print("emptyobjfirstname :",emptyclassobject01.emptyobjfirstname)
print("emptyobjmiddlename ",emptyclassobject01.emptyobjmiddlename)
print("emptyobjlastname : ",emptyclassobject01.emptyobjlastname)
print("emptyobjdob : ",emptyclassobject01.emptyobjdob)


#emptyclass attributes2
class emptyclass :
    pass

emptyclass.emptyobjid=1
emptyclass.emptyobjfirstname="chereddy"
emptyclass.emptyobjmiddlename="maruthi"
emptyclass.emptyobjlastname="cm"
emptyclass.emptyobjdob="30/01/2002"

print("emptyid : ",emptyclass.emptyobjid)
print("emptyfirstname :",emptyclass.emptyobjfirstname)
print("emptymiddlename ",emptyclass.emptyobjmiddlename)
print("emptylastname : ",emptyclass.emptyobjlastname)
print("emptydob : ",emptyclass.emptyobjdob)

#emptyclass__dict__
class emptyclass :
    pass
print(emptyclass.__dict__)

emptyclass.emptyobjid=1
emptyclass.emptyobjfirstname="chereddy"
emptyclass.emptyobjmiddlename="maruthi"
emptyclass.emptyobjlastname="cm"
emptyclass.emptyobjdob="30/01/2002"
print(emptyclass.__dict__)

#class function application

def myoutputfunction(inobject):
    print(inobject.emptyobjid)
    print(inobject.emptyobjname)
    print(inobject.emptyobjdob)
def myinputfunction(inobject):
    inobject.emptyobjid=20
    inobject.emptyobjname='chereddy'
    inobject.emptyobjdob='30012003'
class emptyclass:
    pass
emptyclassobj01=emptyclass()
emptyclassobj01.emptyobjid=10
emptyclassobj01.emptyobjname='maruthi'
emptyclassobj01.emptyobjdob='30012002'

myoutputfunction(emptyclassobj01)
myinputfunction(emptyclassobj01)
myoutputfunction(emptyclassobj01)

#class object initalization

class sample :
    samplevalue=10
    
sampleobject=sample()
print(sampleobject.samplevalue)

#class modifingclass data

class sample :
    samplevalue=10
    
sampleobject01=sample()
print(sampleobject01.samplevalue)
sampleobject02=sample()
print(sampleobject02.samplevalue)
sampleobject02.samplevalue=20
print(sampleobject01.samplevalue)
print(sampleobject02.samplevalue)
sampleobject03=sample()
print(sampleobject03.samplevalue)
sampleobject03.samplevalue=30
print(sampleobject01.samplevalue)
print(sampleobject02.samplevalue)
print(sampleobject03.samplevalue)
sampleobject01.samplevalue=40
print(sampleobject01.samplevalue)
print(sampleobject02.samplevalue)
print(sampleobject03.samplevalue)
sample.samplevalue=50
print(sampleobject01.samplevalue)
print(sampleobject02.samplevalue)
print(sampleobject03.samplevalue)

#class modifingclass data

class sample :
    samplevalue=10
    
sampleobject01=sample()
print(sampleobject01.samplevalue)
sampleobject02=sample()
print(sampleobject02.samplevalue)
sample.samplevalue=20
print(sampleobject01.samplevalue)
print(sampleobject02.samplevalue)
sampleobject03=sample()
print(sampleobject03.samplevalue)

#class function application 3

def myoutfunc(inobject):
    print("the object id is : ",inobject.samplevalue)
    return
def myinputfunc(inobject):
    inobject.samplevalue=20
    return
    
class sample:
    samplevalue=10

sampleobject=sample()
myoutfunc(sampleobject)
myinputfunc(sampleobject)
myoutfunc(sampleobject) 

#class globaldata and datachange

samplevalue=10
class sample(): 
    def myoutfunc(self):
        print("the object is : ",samplevalue)
        return
    def myinputfunc(self):
        samplevalue=20
        return

sampleobject=sample()
sampleobject.myoutfunc()
sampleobject.myinputfunc()
sampleobject.myoutfunc()  


#classdata object

class personclass:
    personobjid=10
    personobjfirstname="maruthi"
    personobjlastname="chereddy"
    personobjdob="30012002"
    
personobject01=personclass()

print("the person id is :",personobject01.personobjid)
print("the person first name is :",personobject01.personobjfirstname)
print("the person last name is :",personobject01.personobjlastname)
print("the person full name is :",personobject01.personobjfirstname,personobject01.personobjlastname)
print("the person dob is :",personobject01.personobjdob)

personobject01.personobjid=20

print("the person id is :",personobject01.personobjid)



#class method

class personclass:
    personobjid=10
    personobjfirstname="maruthi"
    personobjlastname="chereddy"
    personobjdob="30012002"
    
    def persondataoutput(self):
        print("the person id is :",self.personobjid)
        print("the person first name is :",self.personobjfirstname)
        print("the person last name is :",self.personobjlastname)
        print("the person full name is :",self.personobjfirstname,self.personobjlastname)
        print("the person dob is :",self.personobjdob)
        
    def persondatainput(self):
        personobjid=20
        self.personobjfirstname="venkateswarlu"
        self.personobjlastname="chereddy"
        self.personobjdob="01011950"

personobject01=personclass()
personobject01.persondataoutput()
personobject01.persondatainput()        
personobject01.persondataoutput()

#class private objref

class sample:
    __samplevalue=10
    
sampleobject01=sample()
print(sampleobject01.__samplevalue)
sampleobject01.__samplevalue=20
print(sampleobject01.__samplevalue)

#class private objref2

class sample:
    __samplevalue=10
    
sampleobject01=sample()

sampleobject01.__samplevalue=20
print(sampleobject01.__samplevalue)
sampleobject02=sample()
print(sampleobject02.__samplevalue)

#class getter,setter

class sample():
    __samplevalue=10
    def getsamplevalue(self):
        print("the value of private attribute is : ",self.__samplevalue)
    def setsamplevalue(self):
        self.__samplevalue=20
        return
        
sampleobject01=sample()
sampleobject01.getsamplevalue()
sampleobject01.setsamplevalue()
sampleobject01.getsamplevalue()

#class getter,setter handcoding

class sample():
    __samplevalue=10
    def getsamplevalue(self):
        print("the value of private attribute is : ",self.__samplevalue)
    def setsamplevalue(self,inputdata):
        self.__samplevalue=inputdata
        return
        
sampleobject01=sample()
sampleobject01.getsamplevalue()
inputdata=int(input("please enter the value : "))
sampleobject01.setsamplevalue(inputdata)
sampleobject01.getsamplevalue()

#class getter,setter handcoding

class sample():
    __samplevalue=10
    def getsamplevalue(self):
        return self.__samplevalue
    def setsamplevalue(self,inputdata):
        self.__samplevalue=inputdata
        return
        
sampleobject01=sample()
orgvalue=sampleobject01.getsamplevalue()
print(orgvalue)
inputdata=int(input("please enter the value : "))
sampleobject01.setsamplevalue(inputdata)
objvalue=sampleobject01.getsamplevalue()
print(objvalue)

#class protected

class sample:
    _samplevalue=10
sampleobject=sample()
print(sampleobject. _samplevalue)

#class protected assinging data

class sample:
    _samplevalue=10
    
sampleobject01=sample()
print(sampleobject01._samplevalue)
sampleobject01._samplevalue=20
print(sampleobject01._samplevalue)

#class protected objcopy

class sample:
    _samplevalue=10
    
sampleobject01=sample()

sampleobject01._samplevalue=20
print(sampleobject01._samplevalue)
sampleobject02=sample()
print(sampleobject02._samplevalue)

#class getter,setter

class sample():
    _samplevalue=10
    def getsamplevalue(self):
        print("the value of private attribute is : ",self._samplevalue)
    def setsamplevalue(self):
        self._samplevalue=20
        return
        
sampleobject01=sample()
sampleobject01.getsamplevalue()
sampleobject01.setsamplevalue()
sampleobject01.getsamplevalue()

#class application
class person:
    __firstname=None
    __middlename=None
    __lastname=None
    __housenumber=None
    __streetname=None
    __cityname=None
    __statename=None
    __pincode=None
    __gender=None
    __dob=None
    def getpersondata(self):
        self.__firstname='maruthi'
        self.__middlename='chereddy'
        self.__lastname='chowdary'
        self.__housenumber='3-20'
        self.__streetname='donakonda'
        self.__cityname='ongole'
        self.__statename='ap'
        self.__pincode='522035'
        self.__gender='male'
        self.__dob='30012002'
    def putpersondata(self):
        print("the first name is :",self.__firstname )
        print("the last  name is : ",self.__middlename)
        print("the middle name is : ",self.__lastname)
        print("the full name is : ",self.__firstname,self.__middlename,self.__lastname)
        print("the gender  is : ",self.__gender)
        print("the dob  is : ",self.__dob)
        
personobject=person()
personobject.getpersondata()
personobject.putpersondata()

#class application 2 
class person:
    __firstname=None
    __middlename=None
    __lastname=None
    __housenumber=None
    __streetname=None
    __cityname=None
    __statename=None
    __pincode=None
    __gender=None
    __dob=None
    def getpersondata(self):
        self.__firstname=input("please enter firstname : ")
        self.__middlename=input("please enter middle name:")
        self.__lastname=input("please enter last name : ")
        self.__housenumber='3-20'
        self.__streetname='donakonda'
        self.__cityname='ongole'
        self.__statename='ap'
        self.__pincode='522035'
        self.__gender=input("please enter gender : ")
        self.__dob=input("please enter the dob : ")
    def putpersondata(self):
        print("the first name is :",self.__firstname )
        print("the last  name is : ",self.__middlename)
        print("the middle name is : ",self.__lastname)
        print("the full name is : ",self.__firstname,self.__middlename,self.__lastname)
        print("the gender  is : ",self.__gender)
        print("the dob  is : ",self.__dob)
        
personobject=person()
personobject.getpersondata()
personobject.putpersondata()


#class chairs example

class chair :
    __height=None
    __no_legs=None
    __type_material=None
    __color=None
    
    def getchairdata(self):
        self.__height=float(input("enter height of the chair : "))
        self.__no_legs=int(input("enter no of legs  : "))
        self.__type_material=input("please enter the type of material :")
        self.__color=input("enter chair color :")
        
    def showdata(self):
        print("the height of chair :",self.__height)
        print("no of legs :",self.__no_legs)
        print("type of material :",self.__type_material)
        print("color of chair :",self.__color)
        
chairobject=chair()
chairobject.getchairdata()
chairobject.showdata()
        '''