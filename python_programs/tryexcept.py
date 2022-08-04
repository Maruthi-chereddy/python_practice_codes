import os
os.system('cls')

#try except 1
"""
try:
    print("my name is : ",myname)
except:
    print("some thing is fishy")
    """
#try except 2
"""
try:
    print("my name is : ",myname)
except NameError:
    print("some thing is fishy")
except:
    print("something is behond fishy")
    """
    
#try except 3
"""
num=float(input("please enter the numerator :"))
denom=float(input("please enter the denomenator : "))
try:
    quotientvalue=num/denom
    print("the result is : ",quotientvalue)
except:
    print("denominator cannot be zero")
finally:
    print("the process is executed")
    """
    
#try except 4
"""
import sys
nu=float(input("please enter the numerator :"))
denom=float(input("please enter the denomenator : "))
try:
    quotientvalue=num/denom
    print("the result is : ",quotientvalue)
except ZeroDivisionError:
    print("denominator cannot be zero")
except:
    print("the error raised is other than zerodivisionerror")
    print("the error is ",sys.exc_info()[0])
else:
    print("the process is executed")   
"""    

#try except 6
"""
import sys
listforreiprocals=[1,2,3,4,5,]
for extracteddata in listforreiprocals:
    try:
        print("extracted value : ",extracteddata)
        reciprocalvalue=1/int(extracteddata)
    except Exception as expobj:
        print("the system responded with ",sys.exc_info()[0])
        print("the exception class that is identified is :",expobj.__class__)
    else:
        print("the reciprocal of %d is : %0.2f"%(extracteddata,reciprocalvalue))
    finally:
        print("this is from finally block")
"""

#try except reciprocals 2
"""
import sys
listforreiprocals=[1,2,3,4,5,]
for extracteddata in listforreiprocals:
    try:
        print("extracted value : ",extracteddata)
        reciprocalvalue=1/int(extracteddata)
    except Exception as expobj:
        print("the system responded with ",sys.exc_info()[0])
        print("the exception class that is identified is :",expobj.__class__)
    finally:
        print("the reciprocal of %d is : %0.2f"%(extracteddata,reciprocalvalue))
"""    

#try if else except 2
"""
import sys
listforreiprocals=[1,2,3,24,15,]
for extracteddata in listforreiprocals:
    try:
        print("extracted value : ",extracteddata)
        if extracteddata>10:
            print("sorry reciprocal cannot be calculated (limit exceeded)")
            raise Exception("data beyond acceptable limitations")
        reciprocalvalue=1/int(extracteddata)
    except Exception as expobj:
        print("the system responded with ",sys.exc_info()[0])
        print("the exception class that is identified is :",expobj.__class__)
    else:
        print("the reciprocal of %d is : %0.2f"%(extracteddata,reciprocalvalue))
    finally:
        print("this is from finally block")
        """
        
#try if else except 3
"""
import sys
listforreiprocals=[1,2,0,3,24,15,'e']
for extracteddata in listforreiprocals:
    try:
        print("extracted value : ",extracteddata)
        try:
            if extracteddata>10:
                print("sorry reciprocal cannot be calculated (limit exceeded)")
                raise Exception("data beyond acceptable limitations")
            reciprocalvalue=1/int(extracteddata)
        except Exception as e:
            print(e)
            print("the system responded with ",sys.exc_info()[0])
            print("the exception class that is identified is :",e.__class__)
        else:
            print("the reciprocal of %d is : %0.2f"%(extracteddata,reciprocalvalue))
    except ZeroDivisionError:
        print("zero cannot be in denominator")
    except ValueError:
        print("denomenator is having a object other than an integer")
    except:
        print("the exception encountered is : ",sys.exc_info()[0])
    finally:
        print("this is from finally block")
        """
        
#try raise except 2
"""
try:
    invalue=int(input("please enter any positive integer :"))
    if invalue<=0:
        raise ValueError("sorry expected positive integer")
    else:
        print("the given value is :",invalue)
except ValueError as valerr:
    print(valerr)
    """
#try raise except
"""
invalue=int(input("please enter any positive integer :"))
if invalue<=0:
    raise ValueError("sorry expected positive integer")
else:
    print("the given value is :",invalue)
    """
    
#assert basic
"""
innum=float(input("please enter the numerator value : "))
indenom=float(input("please enter the denominator value : "))

print("the value of the quotient is :")
assert indenom!=0,"sorry denominator cannot be zero"
quotient=innum/indenom
print(quotient)
"""