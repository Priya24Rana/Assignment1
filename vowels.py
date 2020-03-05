#find the number of vowels

string=input("Enter a string : ")
con = 0

for i in string:
    if i.lower() in 'aeiou':
        con+=1
print("number if vowels are :" , con)
