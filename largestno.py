# Find the Largest number from given 3 number
number1 = int(input("Enter the first number : "))
print(number1)
number2 = int(input("Enter the second number : "))
print(number2)
number3=int(input("Enter the third number : "))
print(number3)

if(number1>number2 and number1>number3):
    print( number1 , "Number 1 is the  largest number")
elif(number2>number3 and number2>number3):
    print(number2 , "Number2 is the largest number")
else:
    print(number3 ,"Number3 is the largest number")
    
