import os,fnmatch
os.system('cls')


#decode()
"""
try:
    myfile=open("C:/python programs/textfile.py",mode='rb')
    print("this is data read operation using read binary mode")
    dataread=myfile.readline().decode('utf-8')
    
    print("the data read from the file is :",dataread)
finally:
    print("closing the file opened")
    myfile.close()
    """
    
#append()
"""
try:
    myfile=open("C:/python programs/textfile.py",mode='a',encoding='cp1252')
    print("this is data read operation using read binary mode")
    fileposition=myfile.tell()
    print("the data read from the file is :",fileposition)
    if fileposition!=0:
        print("file opened for appending the data")
        invalue=input("please enter the data :")
        myfile.write("\n\n"+invalue+"\n\n")
    fileposition=myfile.tell()
    print("the data read from the file is :",fileposition)
finally:
    print("closing the file opened")
    myfile.close()
"""

#files binary mode
"""
try:
    myfile=open("C:/python programs/textfile.py",mode='rb')
    print("this is data read operation using read binary mode")
    dataread=myfile.readline()
    
    print("the data read from the file is :",dataread)
finally:
    print("closing the file opened")
    myfile.close()
    """
    
#files bytearray 2
"""
try:
    indata=input("please enter any data and when finished press enter key : ")
    myfile=open("C:/python programs/textfile.py",mode='wb')
    finaldata=bytearray(indata,"utf8")
    myfile.write(finaldata)
finally:
    print("closing the file opened")
    myfile.close()
    """
    
#files bytearray
"""
try:
    indata=input("please enter any data and when finished press enter key : ")
    myfile=open("C:/python programs/textfile.py",mode='wb')
    finaldata=bytearray(indata,"utf8")
    print("the given data is : ",finaldata)
finally:
    print("closing the file opened")
    myfile.close()
    """
    

    
#files chdir()
"""
print("the current directory to which you are connected is :",os.getcwd())
dirname=input("please enter the name of the directory : ")
os.chdir(dirname)
print("the current directory to which you are connected id : ",os.getcwd())
"""

#files columns,rows 2
#error
"""
deptdata=[[10,"accounting","new york"],[20,"research","dallas"],[30,"sales","chicago"]]
columnstowrite=len(deptdata[0])
writedeptdata=open("C:/python programs/textfile.py",'w',encoding='cp1252')
for columnid in range(1,columnstowrite+1):
    writedeptdata.write(columnid)
writedeptdata.write("\n")
for extracteddeptrecord in deptdata:
    for deptcolumn in extracteddeptrecord:
        writedeptdata.write(deptcolumn)
    writedeptdata.write('\n')
writedeptdata.close()
"""

#files columns,rows 3




#files writing
"""
myfile=open("C:/python programs/textfile.py",mode='w',encoding='cp1252')
writedata=input("please enter any text : ")
myfile.write(writedata+'\n')
myfile.close() 
"""

#files reading
"""
myfile=open("C:/python programs/textfile.py",'r',encoding='cp1252')
readdata=myfile.read()
myfile.close() 
print(readdata)
"""

#files readable()
"""
myfile=open("C:/python programs/textfile.py",'r',encoding='cp1252')
readdata=myfile.readlines(None)
myfile.close() 
print(readdata)
"""

#files bytes written
"""
try:
    myfile=open("C:/python programs/textfile.py",mode='wb')
    indata=input("please enter any data and when finished press enter key : ")
    byteswritten=myfile.write(indata)
    print("the total number of bytes written in this batch are : ",byteswritten)
    
finally:
    print("closing the file opened")
    myfile.close()
    """
    
#files rhyme writing
"""
myfile=open("C:/python programs/textfile.py",mode='w')
listitems=[]
loop=True
while loop:
    rhymelist=input()
    listitems.append(rhymelist+'\n')
    terminatorchar=rhymelist[-1:]
    if terminatorchar != '.':
        continue
    else:
        loop=False

myfile.writelines(listitems)
myfile.close()
"""

#files read lines
"""
myfile=open("C:/python programs/textfile.py",mode='r')
filereaddata=myfile.readlines()
myfile.close()
loopcounter=0
while ( loopcounter<len(filereaddata)):
    print(filereaddata[loopcounter],end="\n")
    loopcounter=loopcounter+1
    """
    
#files writelines(),readlines(),search
"""
myfile=open("C:/python programs/textfile.py",mode='w')
listitems=[]
loopstate=True
while loopstate:
    purchitems=input()
    listitems.append(purchitems +"\n")
    terminatorchar=purchitems[-1:]
    if terminatorchar !='.':
        continue
    else:
        loopstate=False
    myfile.writelines(listitems)
myfile=open("C:/python programs/textfile.py",mode='r')
filereaddata=myfile.readlines()
for itemindex,purchitemname in enumerate(filereaddata,start=1):
    print(itemindex,purchitemname)
myfile.close()
searchitem=int(input("please enter the index number to search for : "))
currentitemnumber=1
for itemindex,purchitemname in enumerate(filereaddata,start =1):
    if (currentitemnumber == searchitem):
        print(itemindex,purchitemname)
        break
    currentitemnumber=currentitemnumber+1
"""

#files listdir()
"""
capturefiles=os.listdir("C:/python programs/")
print("the files are",capturefiles)
"""

#files details

myfile=open("C:/python programs/textfile.py",mode='w')
writedata=input("please enter any text: ")
myfile.write(writedata +"\n")
print(myfile.name)
print(myfile.closed)
print(myfile.mode)
    
