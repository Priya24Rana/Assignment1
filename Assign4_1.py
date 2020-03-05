class circle:
    def __init__(self,radius):
        self.radius = radius

    def getArea(self):
        return self.radius**2*3.14
    
    def getCircumferance(self):
        return 2*self.radius*3.14

obj=circle(8)
print(obj.getArea())
print(obj.getCircumferance())
