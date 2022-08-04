import os
os.system('cls')

'''
#destructor basic
#error
class sample:
    samplevalue=None
    
    def __init__(self,insamplevalue):
        self.samplevalue=insamplevalue
        
    def __del__(self):

#destructor exmple 1

def createobject():
    sampleobject01=sample(30)
    print(sampleobject01.samplevalue)
    return

class sample:
    samplevalue=None
    def __init__(self,insamplevalue):
        self.samplevalue=insamplevalue
    def __del__(self):
        self.samplevalue=None
        
createobject()
sampleobject=sample(10)
print(sampleobject.samplevalue)      

#destructor basic

def createobject():
    sampleobject01=sample(30)
    print(sampleobject01.samplevalue)
    return

class sample:
    samplevalue=None
    def __init__(self,insamplevalue):
        self.samplevalue=insamplevalue
    def __del__(self):
        self.samplevalue=None
        
sampleobject=sample(10)
print(sampleobject.samplevalue)   
del sampleobject
sampleobject.__del__()
print(sampleobject.samplevalue)  

#destructor basic 4

def createobject():
    sampleobject02=sample02(10)
    
    return

class sample01:
    
    def __init__(self,sampleobject02):
        self.sampleobject02=sampleobject02
        print(self.sampleobject02)
    def __del__(self):
        print("hii")
        
class sample02:
    def __init__(self,insamplevalue):
        self.sampleobject01=sample01(self)
    def __del__(self):
        print("hii")
        
createobject()
'''