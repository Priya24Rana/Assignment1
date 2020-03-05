import math
def area_rectangle(height,width):
    return  width * height

def peri_rectangle(height,width):
    return  2 * ( width + height)

width = int(input("Enter the value for area of rectangle : "))
height =int(input("Enter the height for area of rectangle : "))

area = area_rectangle(height,width)
print("Area of rectangle is " , area)

perimeter = peri_rectangle(height,width)
print("Perimeter of rectangle is : " , perimeter)



''' width = int(input("Enter the value for area of rectangle : "))
height =int(input("Enter the height for area of rectangle : "))

area = width * height
perimeter = 2 *(width + height)
print("Area of rectangle is :" , area)
print("Perimeter of rectangle is : " , perimeter)'''


 
