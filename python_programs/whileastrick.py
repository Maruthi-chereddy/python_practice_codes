
'''outerloopindex=innerloopindex=0
outerloopindex=int(input("\nplease enter the number to control outerloopindex:"))
innerloopindex=int(input("\nplease enter the number to control innerloopindex:"))

while outerloopindex>=0 :
	if (innerloopindex!=0):
		print("%d=>"%(innerloopindex),end='')
		innerloopindex=outerloopindex-1
		
	while(outerloopindex>=0):
		print("*",end="")
		outerloopindex=outerloopindex-1
		
	print("\n")
	outerloopindex=outerloopindex-1'''
    
    
    
import os
os.system("cls")

outerloopindex=innerloopindex=0
outerloopindex=int(input("\nplease enter the number to control outerloopindex:"))
innerloopindex=int(input("\nplease enter the number to control innerloopindex:"))

while innerloopindex>=0 :
	if (outerloopindex!=0):
		print("%d=>"%(outerloopindex),end='')
		innerloopindex=outerloopindex-1
		
	while(outerloopindex>=0):
		print("*",end="")
		outerloopindex=outerloopindex-1
		
	print("\n")
	outerloopindex=outerloopindex-1