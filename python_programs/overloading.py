import os
os.system('cls')

'''
#square rectangle example 1

class boxclass:
    __length=None
    __breadth=None
    
    def __init(self):
        self.__length=0
        self.__breadth=0
        
    def intializesquare(self,inside):
        self.__length=inside
    def intializerectangle(self,inlength,inbreadth):
        self.__length=inlength
        self.__breadth=inbreadth
    def showsquaredim(self):
        print(self.__length)
    def showrectangledim(self):
        print(self.__length)
        print(self.__breadth)
    def calculatesquarearea(self):
        squarearea=self.__length*self.__length
        return squarearea
    def calculaterectanglearea(self):
        rectanglearea=self.__length*self.__breadth
        return rectanglearea
    
squareobject=boxclass()
inside=int(input("please enter the side of box : "))
squareobject.intializesquare(inside)
squareobject.showsquaredim()
squarearea=squareobject.calculatesquarearea()
print(squarearea)

rectangleobject=boxclass()
inlength=int(input("please enter the lenght of box : "))
inbreadth=int(input("please enter the breadth of box : "))
rectangleobject.intializerectangle(inlength,inbreadth)
rectangleobject.showrectangledim()
rectanglearea=rectangleobject.calculaterectanglearea()
print(rectanglearea)

#function overloading

def addinputs(indatatype,*args):
    if indatatype=='int':
        outresult=0
        for extractedargs in args:
            outresult+=extractedargs
        print(outresult)    
    if indatatype=='str':
        outresult=''
        for extractedargs in args:
            outresult=outresult+''+extractedargs
        print(outresult)
    
addinputs('int',5,6)
addinputs('str','ma','ru','thi')


#function overloading 2
#error
def addinputs(inarg01,inarg02):
    returnresult=inarg01+inarg02
    print(returnresult)
def addinputs(inarg01,inarg02,inarg03):
    returnresult=inarg01+inarg02+inarg03
    print(returnresult)
addinputs(25,45)
addinputs(25,45,15)


#multipledispatch 1
from multipledispatch import dispatch

@dispatch(int,int)
def addinputs(inarg01,inarg02):
    returnresult=inarg01+inarg02
    print(returnresult)
    
@dispatch(int,int,int)
def addinputs(inarg01,inarg02,inarg03):
    returnresult=inarg01+inarg02+inarg03
    print(returnresult)
addinputs(25,45)
addinputs(25,45,15)

#multipledispatch 2
from multipledispatch import dispatch

@dispatch(int,int)
def addinputs(inarg01,inarg02):
    returnresult=inarg01+inarg02
    print(returnresult)
    
@dispatch(int,float)
def addinputs(inarg01,inarg02):
    returnresult=inarg01+inarg02
    print(returnresult)

@dispatch(float,int)
def addinputs(inarg01,inarg02):
    returnresult=inarg01+inarg02
    print(returnresult)

@dispatch(float,float)
def addinputs(inarg01,inarg02):
    returnresult=inarg01+inarg02
    print(returnresult)
    
    
addinputs(25,45)
addinputs(25,25.5)
addinputs(23.5,23)
addinputs(23.5,23.5)


#multipledispatch chairs example 
#error
from multipledispatch import dispatch

class boxclass:
    __length=None
    __breadth=None
    
    def __init(self):
        self.__length=0
        self.__breadth=0
    
    @dispatch(int)
    def intializebox(self,inside):
        self.__length=inside
    @dispatch(int,int)
    def intializebox(self,inlength,inbreadth):
        self.__length=inlength
        self.__breadth=inbreadth
    @dispatch(int)
    def showsdim(self,outside):
        outside=self.__length
    @dispatch(int,int)
    def showdim(self,outlength,outbreadth):
        outlength=self.__length
        outbreadth=self.__breadth
    def calculatesquarearea(self):
        squarearea=self.__length*self.__length
        return squarearea
    def calculaterectanglearea(self):
        rectanglearea=self.__length*self.__breadth
        return rectanglearea
    
squareobject=boxclass()
inside=int(input("please enter the side of box : "))
squareobject.intializebox(inside)
squareobject.showdim()
squarearea=squareobject.calculatesquarearea()
print(squarearea)

rectangleobject=boxclass()
inlength=int(input("please enter the lenght of box : "))
inbreadth=int(input("please enter the breadth of box : "))
rectangleobject.intializebox(inlength,inbreadth)
rectangleobject.showdim()
rectanglearea=rectangleobject.calculaterectanglearea()
print(rectanglearea)


#multipledispatch 3

from multipledispatch import dispatch

class sample:
    samplevalue=None
    
    @dispatch()
    def __init__(self):
        self.samplevalue=10
    @dispatch(int)
    def __init__(self,insamplevalue):
        self.samplevalue=insamplevalue
sampleobject01=sample()
print(sampleobject01.samplevalue)
sampleobject02=sample(20)
print(sampleobject02.samplevalue)
'''