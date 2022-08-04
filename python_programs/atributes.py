import os 
os.system('cls')


#__name__

def outerfunction():
    outermsg="hello this is outer scope"
    def innerfunction():
        print("data from enclosing variable from inner function is :",outermsg)
        return
        
    print("referencing" ,innerfunction())
    return
    
if __name__=='__main__':
    outerfunction()

#__code__

def squarenumber(op1):
    result=op1*op1
    print("the square of given number is :",result)
    return
    
invalue=int(input("please enter a number : "))
squarenumber(invalue)

print("the names of parameters and local variables used in squarenumber are : ",squarenumber.__code__.co_varnames)
print("the count of parameters used in squarenumber are : ",squarenumber.__code__.co_argcount)
print("the name of constants used in squarenumber are : ",squarenumber.__code__.co_consts)
print("the name of function in call is : ",squarenumber.__code__.co_name)
print(squarenumber.__code__.co_code) # raw complied byte code instrings
print(squarenumber.__code__.co_filename)#name of the file from which code is written

print(squarenumber.__code__.co_firstlineno)# the line number of the first line in code
print(squarenumber.__code__.co_freevars)#the tuple of names of free variables used in function
print(squarenumber.__code__.co_flags)#bitmap flapgs applied in function
#print(squarenumber.__code__.co_celivars)#ceil variable designed in the function
#print(squarenumber.__code__.co_inotab)#the encoded mapping of line numbers to bytecode indices
print(squarenumber.__code__.co_names)#name of the local variables in function
print(squarenumber.__code__.co_nlocals)#no of local variables in function
print(squarenumber.__code__.co_stacksize)#size of stack allocated for function
print(__name__)
print(dir())
print(dir(__builtins__))
print(len(dir(__builtins__)))
print(dir(__name__))
print(len(dir(__name__)))


#builtins
import builtins
invalues=[1,2,3,4,5,6,7,8,9]
totalsum=builtins.sum(invalues)
print(totalsum)
