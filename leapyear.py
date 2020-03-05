#Check for the leap year
year=int(input("Please Enter the year :"))
print(year)

if((year%400 == 0) or ((year%4 == 0) and (year%100 !=0))):
    print(year , " Is the leap year")
else :
    print("Not Leap year")
