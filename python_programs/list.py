import os
os.system('cls')

"""
item01=[["pencils","papers"],"ball pens",["erasers","sticks","exam pads"]]

print("the given list of items are : ",type(item01))
print("the given list of items are : ",len(item01))
print("the given list of items are : ",item01)
print("the given list of items are : ",item01[-1])
print("the status of the item of pencil is:",str(("pencils" in item01)))
print("the given list of items are : ",item01[1])
print("the given list of items are : ",item01[2][2])
print("the given list of items are : ",list(item01))
print("the given list of items are : ",item01[0::3])
"""


#list slicing
"""
numrange=[1,2,3,4,5,6,7,8,9,0]

loop=True
while loop==True:
    start=int(input("please enter the number to start from : "))
    end=int(input("please enter how many numbers you want from starting point : "))
    print("required output is : ",numrange[start:(start+end)])
    
    cont=input("do you want to continue (Y/N): ")
    if (cont==n or cont==N):
        print("thanks for trying")
        loop=False
        
"""

#list insertion
"""
givendata=['cricet','football','shuttle','base ball']

loopstate=True
while loopstate==True:
    print("the list of given data is : ",givendata)
    choosed=input("do you want to update the previous data(y/n) : ")
    if choosed=='y' or choosed=='Y' :
        newvalue=input("please enter the new name to be entered in list : ")
        choice=int(input("please enter the  place of the name to update (number):"))
        print("exceuting your order")
        givendata[choice-1]=newvalue
        print("the list after updation is : ",givendata)
        loop=input("do you want to change another one(y/n): ")
        if loop=='n' or loop=='N':
            loopstate=False
    else:
        break
"""

#list deletion
"""
givendata=['cricet','football','shuttle','base ball']
print("the list of given data is : ",givendata)
loopstate=True
while loopstate==True:
    
    choosed=input("do you want to delete any name from the data(y/n) : ")
    if choosed=='y' or choosed=='Y' :
        
        choice=int(input("please enter the  place of the name to delete (number):"))
        print("exceuting your order")
        del givendata[choice-1]
        print("the list after updation is : ",givendata)
        loop=input("do you want to delete another one(y/n): ")
        if loop=='n' or loop=='N':
            loopstate=False
    else:
        break
        
        """
        
#list merging
"""
list01=[1,2,3,4,5]
list02=[6,7,8,9,0]
print("the given data of first list is :",list01,"and the second list is : ",list02)
choice=input("do you want to merge the given lists(y/n) : ")
if choice=='y' or choice=='Y':
    count=0
    while count<(len(list02)):
        print("the list value in list02 merging is : ",list02[count])
        count+=1
    print("the final result is : ",list01+list02)
"""

#list example
"""
givendata=['cricet','football','shuttle','base ball']
print(str(len(givendata)))
"""
#list example 2
"""
givendata=['cricet','football','shuttle','base ball']
print(givendata)
choice=input("do you want to add a new name to the given list(y/n) : ")
if choice=='y' or choice=='Y':
    newvalue=input("please enter the new name : ")
    givendata.append(newvalue)
    print("printing the updated list : "givedata)
    
"""
#list maximun value
"""
list01=[]
total=int(input("please enter the total number numbers to be added: "))
count=1
while count<=total :
    value=int(input("please enter the number : "))
    list01.append(value)
    count+=1
print("the provided data is : ",list01)
print("the maximum of the provided data is :",max(list01))
print("the minimum of the provided data is : ",min(list01))
"""

#list extend
"""
list01=[1,2,3,4,5]
list02=[6,7,8,9,0]

list01.extend(list02)
print(list01)
list01.append(list02)
print(list01)
"""

#list index
"""
givendata=['cricet','football','shuttle','base ball']
print(givendata)
print(list(givendata))
choice = input("please enter the name to find index of : ")
print("the index of entered data is : ",givendata.index(choice))
"""

#list insert
"""
givendata=['cricet','football','shuttle','base ball']
index=int(input("please enter the index where to add the element :"))
element=input("please enter the element to be added : ")
print(givendata.insert(index,element))
print(givendata)
"""

#list example 3
#pop
"""
givendata=['cricet','football','shuttle','base ball']
print(givendata)
givendata.pop()
"""

#list reverse
"""
givendata=['cricet','football','shuttle','base ball']
print(givendata)
givendata.reverse()
print(givendata)
"""

#list sort
#list sort reverse
"""
givendata=['cricet','football','shuttle','base ball']
print(givendata)
givendata.sort()
print(givendata)
givendata.sort(reverse=True)
print(givendata)
"""

#list string conv
"""
name=input("please enter your name : ")
namelist=list(name)
print("printing your name as a string : ",str(namelist))
"""

#list remove
"""
givendata=['cricet','football','shuttle','base ball']
givendata.remove('cricet')
print(givendata)
"""

#list remove 2
"""
givendata=['cricet','football','shuttle','base ball']
givendata.remove(givendata[1])
print(givendata)
"""

#list duplicate
"""
list01=[1,2,3,4,5]
list02=list01
print(list01)
list02.append(6)
print(list01)
print(id(list01))
print(id(list02))
"""

#list duplicate 2
"""
list01=[1,2,3,4,5]

list02=list01[:]
print(list01)
list02.append(6)
print(list01)
print(list02)
print(id(list01))
print(id(list02))
"""

#list any
"""
list01=[1,2,3,4,5]
search=input("please enter the number you want to search : ")
if any(i in search for j in list01):
    print("hurray your element has been found")
    """
    
#list enumerate

givendata=['cricet','football','shuttle','base ball']

givendata2=enumerate(givendata)
print(list(givendata2))


#list enumerate 2
"""
givendata=['cricet','football','shuttle','base ball']
print(givendata)
for i,j in enumerate(givendata):
    print(i,j)
"""


#list enumerate 3
"""
givendata=['cricet','football','shuttle','base ball']
print(givendata)
for i in enumerate(givendata):
    print(i,end='\n')
   """ 
    
#list enumerate 4
"""
givendata=['cricet','football','shuttle','base ball']
print(givendata)
for i,j in enumerate(givendata,2):
    print('\n',i,'\t\t\t',j)
    """
    
#list enumerate yeild
"""
def myenum(inlist,appliedset=0,offsetlevel=1):
    outindex=appliedset
    for outelement in inlist:
        yield outindex,outelement
        outindex+=offsetlevel
givendata=['cricet','football','shuttle','base ball']
for i,j in myenum(givendata,0,3):
    print(i,'\t\t\t',j)
    """
    
#list example
#list filtering
"""
list01=[1,2,3,4,5]
list02=[]
filterelement=input("please enter the element to be filtered: ")
list02.append(filterelement)
print(list02)
"""

#list lambda
"""
list01=[1,2,3,4,5]
list02=[]
filterelement=input("please enter the element to be filtered: ")
list02.append(filterelement)
print(list02)
list02=list(filter(lambda filterelement:filterelement in list02,list01))
print(list02)
"""

#list func duplicate
"""
def filterduplicates(elementtocheck):
    if elementtocheck in list01ref:
        return False
    else :
        return True
list01=[1,12,3,4,5,2,7]
list02=[12,3,7,8,9,0]
list01ref=list02
outfilterelements=list(filter(filterduplicates,list01))
print(outfilterelements)
list01ref=list01
outfilterelements=list(filter(filterduplicates,list02))
print(outfilterelements)
"""

#list next
"""
givendata=['cricet','football','shuttle','base ball']
sportslistiter=iter(givendata)

loopstate=True
while loopstate:
    enterstate=input("please press enter key to get next element")
    print(next(sportslistiter))
    if enterstate=='':
        continue
    else:
        loopstate=False
        """
        
#list sum
"""
list01=[1,2,3,4,5,6,7]
listsum=sum(list01,5)
print(listsum)
"""

#list tuple conv
"""
tuplesam=(1,2,3,4,5,6)
print(tuplesam)
listsam=list(tuplesam)
del listsam[0]
tuplesam=tuple(listsam)
print(tuplesam)
"""