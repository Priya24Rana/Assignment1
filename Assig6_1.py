thistuple =tuple(input("Enter the value of tuple : "))
print(thistuple)

print("This is the tuple value :" ,thistuple)

thislist=list(thistuple)
print("This is the list value after converting to the tuple \n  ", thislist)
x=thislist
if thislist != []:
    thislist.pop(0)
    thislist.pop(-1)

thistuple=tuple(thislist)
print("Updated tuple is " , thistuple)














