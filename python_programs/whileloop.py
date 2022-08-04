#sum of even numbers odd numbers squares and cubes in  certain range
#fibonacci in specified range


"""import time
import os
os.system("cls")

loopcontrol=1
loopterminator=int(input("\nplease enter the number of times to iterate:"))
print("\ninitiating the loop for execution..please wait..",end='\n')
time.sleep(2)
 
while (loopcontrol <= loopterminator):
	print(">>>")
	loopcontrol=loopcontrol+1
    """
    
    
    
#ifelse while loop

"""import os
os.system("cls")

factvalue=factindex=1

factnumber=int(input("please enter a number to get its factorial:"))

if factnumber==0:
    factvalue=0
elif factnumber==1:
    factvalue=1
else:
    factindex=factnumber
    while (factindex>=1):
        factvalue=factvalue*factindex
        factindex-=1
    
print(f"the factorial of given number {factnumber} is {factvalue}")
"""
	 
#whileloop 2
"""import os
os.system("cls")

loopcontrol=1
loopterminator=int(input("please enter the number of times to iterate:"))
print("executing your command")
while loopcontrol<=loopterminator:
    print(f"this is the iterator number {loopcontrol}")
    loopcontrol+=1
    
print("out of your iterator")
    """
    
    
    
#whileloop 3
"""import os
os.system("cls")

start=int(input("please enter a number to start with:"))
end=int(input("please enter a number to end:"))

while start<=end:
    print(f"{start},")
    start+=1
    """
    
    
#whileloop 4

"""import os
os.system("cls")

start=int(input("please enter a number to start with:"))
end=int(input("please enter a number to end and caluculate the sum:"))
loopstart=start
totalsum=0

while start<=end:
    totalsum+=start
    start+=1
    
print(f'the total sum of numbers from {loopstart} and {end} is {totalsum}')
"""




#whileloop 5
"""import os 
os.system("cls")

printchars='a'
while (printchars<='z'):
    print(f'{printchars}',end=",")
    printchars=chr(ord(printchars)+1)
    """
    
    
#whileloop 6
"""import os
os.system("cls")

printchars=0
while (printchars<=122):
    print("%c"%(printchars),end=",")
    printchars+=1
    """
    
    
#whileloop 7
"""import os
os.system("cls")

start=int(input("please enter a number to start with:"))
end=int(input("please enter a number to end :"))

while start<=end:
    if(start%2==0):
        print(f'{start}',end=',')
    start+=1
    """
    
    
#whileloop 8
"""import os
os.system("cls")

tableindex=int(input("please enter the number you want upto:"))
tablenumber=int(input("please enter the number you wnat to get the table of:"))

loopindex=0
while loopindex<=tableindex:
    print(f'{tablenumber} * {loopindex} = {tablenumber*loopindex}')
    loopindex+=1
"""



#whileloop 9
"""import os
import math
os.system("cls")

number=int(input("please enter the number  upto which \"square root\" ,\"cube root\",\"square\" is to found :"))
loopindex=1

while(loopindex<=number):
    square=loopindex*loopindex
    cube=loopindex*loopindex*loopindex
    squareroot=math.sqrt(loopindex)
    print(loopindex)
    print(f"square is {square} ,cube is {cube} ,squareroot is {squareroot} ")
    loopindex+=1
"""


#while loop

"""import os
os.system("cls")

loopindex=1
iteration=int(input("please enter number of times to be iterated:"))

while loopindex<=iteration:
    print("this is iteration number",loopindex)
    loopindex+=1
    """
    
    
#while if even or odd

"""import os
os.system("cls")
print("1.even \n2.odd")
choice=int(input("please enter your choice:"))
start=int(input("please enter a number to start with:"))
end=int(input("please enter a number to end :"))

if choice==1:
    print("printing the even numbers")
    while start<=end:
        if(start%2==0):
            
            print(f'{start}',end=',')   
        start+=1
elif choice==2:
    print("printing the odd numbers")
    while start<=end:
        if (start%2!=0):
             print(f'{start}',end=',')
        start+=1
             
else:
    print("please enter correct choice provided")
    """
    
    
    
#whileif timer
"""import os
import time
os.system('cls')

hour=minute=second=0
while True:
    os.system("cls")
    print(f'{hour}:{minute}:{second}')
    second+=1
    if second==60:
        minute+=1
        second=0
    if minute==60:
        hour+=1
        minute=0
    if hour==24:
        hour=0
        minute=0
        second=0
        
    time.sleep(1)
    """
    
    
#whileloop finding factors
"""import os
os.system('cls')

loopindex=1
number=int(input("please enter the number:"))
print("printing factors of %d:"%number)
while loopindex<=number:
    if (number%loopindex==0):
        print(loopindex,end=",")
    loopindex+=1
    
    """
    
    
#whileloop fionance

"""import os
os.system('cls')

start=0
end=int(input("please enter the number to stop the series:"))
increment=1
fibonaccicount=0

while fibonaccicount<end:
    print(start,end=',')
    nextlevel=start+increment
    start=increment
    increment=nextlevel
    fibonaccicount+=1
    """
    
    
    
#whileloop ifelse alphabets
"""import os
os.system('cls')

print("1.small letters \n2.capital letters")
choice=int(input("please enter your choice:"))

if choice==1:
    printchars="a"
    while (printchars<="z"):
        print(f'{printchars}',end=",")
        printchars=chr(ord(printchars)+1)
      
elif choice==2:
    printchars="A"
    while (printchars<="Z"):
        print(f'{printchars}',end=",")
        printchars=chr(ord(printchars)+1)
        
else:
    print("please enter a valid number:")
    """
    
    
#whileloop simpleinterest

"""import os
os.system('cls')

p=float(input("please enter amount:"))
t=float(input("please enter time:"))
r=float(input("please enter rate:"))
loop=1
while loop<=t:
    interest=(p*r*loop)/100
    p=p+interest
    print(f"interest for the {loop} year is {interest}")
    loop+=1
    """
    
    
#whileloop totalsum
"""import os
os.system('cls')
 
end=int(input("please enter the end number to calculate the sum:"))
loop=0
totalsum=0

while loop<=end:
    print(loop,end=",")
    totalsum=totalsum+loop
    loop+=1
    print("the sum upto given value is %d"%totalsum)
    
"""


#nested whileloop with timer
"""import time
import os
os.system('cls')

inner=outer=1
while outer<=5:
    inner=1
    print(outer)
    time.sleep(3)
    while inner<=outer:
        print(inner)
        time.sleep(3)
        inner+=1
        if inner>outer:
            print("inner is terminated")
            time.sleep(3)
    outer+=1
    
    time.sleep(3)
    """
    
    
#nested whileloop

"""import os
os.system("cls")

outer=inner=1

while outer<=5:
    inner=1
    while inner<=outer:
        print(inner,end=",")
        inner+=1
    print("-")
    outer+=1
    """
    
#nested whileloop3
"""import os
os.system('cls')

outer=inner=1

while outer<=5:
    inner=1
    while inner<=outer:
        print("*",end="")
        inner+=1
    print("")
    outer+=1
    """
    
    
#nested whileloop4

"""outer=inner=1

while outer<=5:
    inner=1
    while inner<=outer:
        print(f"{inner}",end="")
        inner+=1
    print("")
    outer+=1
    """
    
#nested whileloop 5
"""import os
os.system('cls')

outer=inner=1
while outer<=10:
    inner=1
    while inner<=10:
        print(f'{outer*inner}')
        inner+=1
    print("\n")
    outer+=1
    """


#nested whileloop6
"""import os
os.system('cls')

outer=inner=0
outer=int(input("please enter the controller for outer loop:"))
#inner=int(input("please enter the controller for inner loop:"))
while outer>=0:
    if outer!=0:
        print(outer,end="")
        inner=outer-1
        
    while inner>=0:
        print("#",end="")
        inner-=1
    print("\n")
    outer-=1
    """
    
    
#nested whileloop7
"""import os
os.system('cls')
outer=5
while outer>0:
    inner=1
    while inner<=outer:
        print("*",end="")
        inner+=1
    print("\n")    
    outer-=1
"""


#nestedwhileloop players score
"""import os
os.system('cls')
player=1
while player<=11:
    attempts=1
    while attempts<=7:
        print(f'player {player} attempt number {attempts} , score:')
        attempts+=1
    player+=1
    """
    
    
#nestedwhileloop reversenum
"""import os
os.system('cls')

number=reverse=remainder=original=0
number=int(input("please enter the number :"))
original=number

while number!=0:
    remainder=number%10
    print(remainder)
    reverse=int((reverse*10)+remainder)
    print(reverse)
    number=int(number/10)
    print(number)
print(f'{original} and {reverse}')
"""
    