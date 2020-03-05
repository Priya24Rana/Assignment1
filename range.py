number = int(input("Enter anu number :"))
print(number)

#last 10 gigits by for loop
for x in range(number,number-10,-1):
    print(x)

# last 10 digits by while loop
y=10
while(y>0):
    print(number)
    y-=1
    number-=1
    
