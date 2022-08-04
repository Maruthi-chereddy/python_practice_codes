import os 
os.system('cls')
"""
value01=float(input("please enter first value: "))
value02=float(input("please enter your second value: "))

result=lambda:value01+value02
print("the result of the given numbers after addition is :",result())
"""


"""
message=input("please enter a message : ")
messageout=lambda : print("the message your entered is : ",message)
messageout()
"""

"""
#def listsquares(inlistelement):
 #   return inlistelement*inlistelement
    

mylist=list([])
loop=True
while loop==True:
    getvalue=int(input("please enter the integer you want to get square of :"))
    mylist.append(getvalue)
    choice=input("do you want to add one more(Y/N): ")
    if choice=="n" or choice=="N":
        loop=False
print("the total length of the list you entered is:",len(mylist))
print("printing the squares for entered integers")

squaredvalue=list(map(lambda listsquares:(listsquares*listsquares),mylist))
print(squaredvalue)
#finalsquares=list(squaredvalue)
#print("the squares are :",finalsquares)
"""

"""
value01=float(input("please enter first value: "))
value02=float(input("please enter your second value: "))

result=lambda inparam01,inparam02:inparam01+inparam02
print("the result of the given numbers after addition is :",result(value01,value02))
"""

"""
import functools
mytemp=[1,2,3,4,5,6,7,8,9,0]
#eventemperature=list(filter(lambda eventemp:(eventemp%2==0),mytemp))
#print(eventemperature)

cumpricelist=functools.reduce(lambda value01,value02:value01-value02,mytemp)
print(cumpricelist)
"""

import functools

myprices=[1,2,3,4,5,6,7,8,9]
myquantity=[7,6,5,4,3,2,1]

finalcost=functools.reduce(lambda price,quantity:((price*quantity)+(price*quantity)),myprices,myquantity)

finalcostwithtax=liat(finalcost)
print(finalcostwithtax)