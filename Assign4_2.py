class Temprature:   
    def convertFahrenheit(self,celsius):
        return ((celsius*9/5)+32)
        
    def covertCelsius(self,fahrenheit):
        return ((fahrenheit-32)*5/9)
        
obj=Temprature()
print(obj.convertFahrenheit(82))
print(obj.covertCelsius(32))

        
        
