pi = 3.14
'''radious = float(input("Please enter the radius of a circle: "))

circumference = 2 * pi * radious
print("Cirumference of circle : " ,circumference)'''


def find_circumference(radious):
    return 2 * pi * radious

def find_area(radious):
    return pi*radious**2
    
radious =float(input("Enter the radiou : "))
cir = find_circumference(radious)
print("Circumference of circle is : ", cir)

area = find_area(radious)
print("Area if circle is : " , area)
