
#fibanocci series
import os
os.system('cls')
"""
value=int(input("please enter the number of fibanocci numbers to be printed :"))
fibanoccivalue,stepvalue=0,1
print("the fibanocci series upto ",value,"is :0,",end=" ")
for i in range(value):
    fibanoccivalue,stepvalue=stepvalue,fibanoccivalue+stepvalue
    print(fibanoccivalue,",",end='')
    
"""

#forloop astrick in rows 2

"""import os
os.system('cls')

outer=inner=1
rows=int(input("please enter number of rows you want:"))
outer=rows
inner=2*outer-2
for outer in range(0,outer):
    for inner in range (0,inner):
        print('@',end='')
    inner-=1
    for inner in range(0,outer+1):
        print('*',end='')
    print('\r')
"""


#forloop evennum
"""import os
os.system('cls')

initial=int(input("please enter start range value:"))
final=int(input("please enter end range value:"))
loopstart=initial
for i in range(initial,final+1):
    if (i % 2==0):
        print(i,end=',')
        """
        
        
#forloop no of rows 2
import os
os.system('cls')
printvalue=1
rows=int(input("please enter number of rows to print:"))
for j in range(1,rows+1):
    for i in range(0,j):
        print(printvalue,end=',')
        printvalue+=1
        
    print('\r')
   
   
   
#forloop no of rows 3

"""import os
os.system('cls')
printvalue=1
rows=int(input("please enter number of rows to print:"))
#end=2*rows-2
for j in range(0,rows):
    for i in range(0,j):
        print(end='')
        #end-=2
    for i in range(0,j+1):
        print(printvalue,end=' ')
        printvalue+=1
    print('\r')
    """


#forloop no of rows

"""import os
os.system('cls')

rows=int(input("please enter number of rows to print:"))
for j in range(0,rows):
    printvalue=1
    for i in range (0,j+1):
        print(printvalue,end=',')
        printvalue+=1
    print('\r')
"""


#forloop offset totalsum
"""import os
os.system('cls')

totalsum=0
start=int(input("please enter number to start with:"))
end=int(input("please enter number to end with:"))
offset=int(input("please enter number you want to offset with:"))

for i in range(start,end+1,offset):
    totalsum+=start
    start+=1
    
    
print(totalsum)
"""


#forloop printing squares
"""import os
os.system('cls')

start=int(input("please enter number to start with:"))
end=int(input("please enter number to end with:"))

for i in range (start,end+1):
    print(i ," square is ", i*i)
"""

#forloop reverse in rows
"""import os
os.system('cls')

printvalue=1
rows=int(input("please enter number of rows to print:"))
end=rows-1
for j in range(0,rows):
    printvalue=1
    for i in range(0,end):
        print(end='#')
    end-=1
    for i in range (0,j+1):
        print(printvalue,end=' ')
        printvalue+=1
        
    print('\r')
    """

#forloop reversenum  (error)
"""import os
os.system('cls')
reverse=number=0
number=input("please enter the number to be reversed:")

for loop in range(len(number),0,-1):
    reverse+=number[loop-1]
    
print(reverse)
"""


#forloop squares in list
"""import os
os.system('cls')

mylist=[0,1,2,3,4,5]
for j in mylist:
    print(j*j)
    """
    
    
#forloop totalsum
"""import os
os.system('cls')
totalsum=0
start=int(input("please enter number to start with:"))
end=int(input("please enter number to end with:"))

for i in range (start,end+1):
    totalsum+=start
    start+=1
print("totalsum is :",totalsum)
"""


#forloop totalsum2
"""import os
os.system('cls')

start=int(input("please enter number to start with:"))
end=int(input("please enter number to end with:"))
totalsum=0

for i in range (start,end+1):
    totalsum+=i
print("totalsum is :",totalsum)
"""


#forloop with string
"""import os
os.system('cls')

for i in  "maruthi":
    print(i )
    """
    
    
#nested forloop 2rows
"""import os
os.system('cls')

rows=int(input("please enter number of rows to print:"))

for j in range(rows,0,-1):
    for i in range(0,j):
        print(i,end=' ')
    print('\r')
    """
    
    
#nested for loop 3rows
"""import os
os.system('cls')

rows=int(input("please enter number of rows to print:"))

for j in range(rows,0,-1):
    for i in range(1,j+1):
        print(i,end=' ')
    print('\r')
    """
#nestedfor loop 4
"""import os
os.system('cls')

rows=int(input("please enter number of rows to print:"))

for j in range(1,rows):
    for i in range(j,0,-1):
        print(i,end=' ')
    print('\r')
    """
    
#nestedfor loop 5
"""import os
os.system('cls')

rows=int(input("please enter number of rows to print:"))

for j in range(0,rows):
    for i in range(j,0,-1):
        print(i,end=' ')
    print('\r')
    """
    
    
#nestedfor loop 6
"""import os
os.system('cls')

rows=int(input("please enter number of rows to print:"))

for j in range(1,rows+1):
    for i in range(-1+j,-1,-1):
        print(2**i,end=' ')
    print('\r')
    """
    
#nestedfor loop 7
"""import os
os.system('cls')

rows=int(input("please enter number of rows to print:"))

for j in range(1,rows):
    for i in range(j,0,-1):
        print(i,end=' ')
    for i in range(1 ,j+1,1):
        print(i,end=' ')
        
    print('\r')
    """
    
    
#nestedfor loop 8
"""import os
os.system('cls')

rows=int(input("please enter number of rows to print:"))
value=1
breakvalue=2
for j in range(rows):
    value=1
    for i in range(1,breakvalue):
        print(value,end=' ')
        value+=1
    
    print('\r')
    breakvalue+=2
    """
    

#nestedfor loop 9-1
"""import os
os.system('cls')
rows=int(input("please enter number of rows to print:"))

initial=1
final=2
printvalue=final

for j in range(0,rows+1):
    for i in range(initial,final):
        printvalue-=1
        print(printvalue,end='#' )
        
    print("@")
    initial=final
    final+=j
    printvalue=final
    
    """

#nestedfor loop 10

"""import os
os.system('cls')

rows=int(input("please enter number of rows to print:"))

currentevennum=lastevennum=2*rows
for j in range(1,rows+1):
    for i in range(j):
        print(currentevennum,end=' ')
        currentevennum-=2
    print('\r')
    """
    
    
    
#nestedfor loop 11

"""import os
os.system('cls')

rows=int(input("please enter number of rows to print:"))

for j in range(1,rows+1):
    for i in range(1,j-1):
        print(i,end=' ')
    for i in range(j-1,0,-1):
        print(i,end=' ')
        
    print('\r')
    """
 
#nestedfor loop 12

"""import os
os.system('cls')

rows=int(input("please enter number of rows to print:"))

currentevennum=lastevennum=2*rows
for j in range(1,rows):
    for i in range(1,j+1):
        print(i*j,end=' ')
    print('\r')
    """
  
#nestedfor loop 13

"""import os
os.system('cls')

rows=int(input("please enter number of rows to print:"))

for j in range(0,rows+1):
    for i01 in range(rows-1,j,-1):
        print(i01,end=' ')
    for i02 in range(j):
        print(' ',end=' ')
    for i03 in range(j+1,rows):
        print(i03,end=' ')
    print('\r')
    """
    
#nestedforloop 14
"""import os
os.system('cls')
rows=int(input("please enter number of rows to print:"))
for j in range(1,rows+1):
    for i in range(1,rows+1):
        if i<=j:
            print(j,end=' ')
        else:
            print(i,end=' ')
    print("\r")
    """

#nestedforloop 15
"""import os
os.system('cls')
rows=int(input("please enter number of rows to print:"))
ca01=(2*rows)-2
ca02=0
for j in range(0,rows):
    ca02+=1
    for i in range(0,ca01):
        print(end=' ' )
    ca01-=1
    for i in range(0,j+1):
        print(ca02,end=' ')
    print("\r")
    
ca01=(rows)-2
ca02=rows+2
for j in range(0,rows):
    ca02-=1
    for i in range(0,ca01):
        print(end=' ' )
    ca01+=1
    for i in range(0,j+1):
        print(ca02,end=' ')
    print("\r")
    """
    
    
#nestedforloop17
"""import os
os.system('cls')
rows=int(input("please enter number of rows to print:"))
ca=20
lc=[0]*20
for j in range(rows):
    for i01 in range(1,ca+1):
        print(" ",end=' ')
    lc[j]=1
    for i02 in range(j+1):
        print("%d"%(lc[i02]),end=' ')
    for i02 in range(j,0,-1):
        lc[i02]=lc[i02]+lc[i02-1]
    ca-=3
    print("\r")
    """

  
#nestedforloop 
"""import os
os.system('cls')

rows=int(input("please enter number of rows to print:"))

for j in range(rows):
    for i in range(j+1):
        print(j,end=' ')
    print('\r')"""
     
    
    
    
    
    
    



















