def factorial(a):
    
    fact =1

    if(a<0):
        print("Invalid input",a)
    elif(a==0):
        print("factorial of 0 is 1")
    else:
        for i in range(1,a+1):
            fact=fact*i
        print("factorial of " ,a , "is" ,fact)
