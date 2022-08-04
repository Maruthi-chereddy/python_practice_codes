#atm using if constract
"""import os
os.system("cls")

currentbalance=100000
minbalance=500

print("please select the options type:")
print("\n1.cashwithdrawal")
print("\n2.cashdepoist")
print("\n3.pinchange")
print("\n4.bankstatement")
print("\n5.balanceenqiury")

yourchoice=float(input("\nplease enter your choice as numbers :"))

if(yourchoice==1):
    amountwithdraw=float(input("\nplease enter the amount for withdraw:"))
    currentbalance-=amountwithdraw
    if(currentbalance<=minbalance):
        print("your account is out of balance please check your account balance",end="\n")
        print ("your transcation is declined")
    else:
        print ("your transcation is successful")
        print("your account balance after the transcation is: %f"%currentbalance) 
        
elif(yourchoice==2):
    cashdepoist =float(input("\nplease enter the amount for depoist:"))
    currentbalance+=cashdepoist
    print ("your account has depoisted with %f"%cashdepoist,"the total balance in your account is %f"%currentbalance,end="\n")
    
elif(yourchoice==3):
    oldpin=int(input("\nplease enter the old pin:"))
    newpin=int(input("\nplease enter the new pin:"))
    if (oldpin==newpin):
        print("your old pin matches with your new pin...please enter a new one")
    else:
        print("your pin changed successfully:")

elif(yourchoice==4):
    print ("please contact the customer care for help",end="\n")

elif(yourchoice==5):
    pin=int(input("\nplease enter the your pin:"))
    print ("your account balance is %f"%currentbalance,end="\n")
    
else:
    print("please enter a vaild input")
    """ 
    
    
    
    
# atm using while atm

import os
os.system("cls")


currentbalance=100000
minbalance=500
loop= True
while loop==True :   
        print("please select the options type:")
        print("\n1.cashwithdrawal")
        print("\n2.cashdepoist")
        print("\n3.pinchange")
        print("\n4.bankstatement")
        print("\n5.balanceenqiury")

        yourchoice=float(input("\nplease enter your choice as numbers :"))

        if(yourchoice==1):
            amountwithdraw=float(input("\nplease enter the amount for withdraw:"))
            currentbalance-=amountwithdraw
            if(currentbalance<=minbalance):
                print("your account is out of balance please check your account balance",end="\n")
                print ("your transcation is declined")
            else:
                print ("your transcation is successful")
                print("your account balance after the transcation is: %f"%currentbalance) 
                
        elif(yourchoice==2):
            cashdepoist =float(input("\nplease enter the amount for depoist:"))
            currentbalance+=cashdepoist
            print ("your account has depoisted with %f"%cashdepoist,"the total balance in your account is %f"%currentbalance,end="\n")
            
        elif(yourchoice==3):
            oldpin=int(input("\nplease enter the old pin:"))
            newpin=int(input("\nplease enter the new pin:"))
            if (oldpin==newpin):
                print("your old pin matches with your new pin...please enter a new one")
            else:
                print("your pin changed successfully:")

        elif(yourchoice==4):
            print ("please contact the customer care for help",end="\n")

        elif(yourchoice==5):
            pin=int(input("\nplease enter the your pin:"))
            print ("\nyour account balance is ",currentbalance,end="\n")
            
        else :
            print("please enter a vaild input")
        
        print("\nY=make another transcation")
        print("N=end transcation here itself")
        userchoice=input("\nplease enter your choice N or Y : ")
        if userchoice== "N" or userchoice=="n" :
            loop=False
print("thanks for using")