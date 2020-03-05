'''thislist=list(input("Enter the value of list :"))
print(thislist)

print("This is the list value :",thislist)'''
thislist = [1,2,3,4,5,6,7,8,9,10]

OddList = []
EvenList = []

for x in thislist:
    if x%2 == 0:
        EvenList.append(x)
    else:
        OddList.append(x)
print("Even Number" ,EvenList)
print("Odd Number" , OddList)
   
