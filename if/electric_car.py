class Car():
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def desc(self):
        return self.make + ' ' + self.model + ' ' + str(self.year)

"""
    集成自Car
"""
class ElectricCar(Car):
    """电动汽车"""
    def __init__(self,make,model,year):
        """初始化父类的属性"""
        """super() 注意括号"""
        super().__init__(make,model,year)


my_tesla = ElectricCar('tesla','model s', 2017)
print(my_tesla.desc())