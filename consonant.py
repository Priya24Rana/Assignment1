#find the Consonant

string = input("Enter any string : ")
con = 0

for i in string:
    if i.lower() not in "aeiou" :
        con+=1
print("number of constant are :" , con)


