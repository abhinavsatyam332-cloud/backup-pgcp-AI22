from itertools import count

# from DailyPracticals.Day2.DemoSets import value


class Car:
    count = 0
    def __init__(self,make,model,price,segment="Economy"):
        Car.count+=1
        self._make = make
        self._model = model
        self._price = price
        self._segment = segment

    def __str__(self):  # informal representation
        return f'Model Name: {self._model} ,Model price: {self._price}, Make: {self._make} '

    def __repr__(self): # formal representation     give output like   className.me
        # return f'Car({self._model}, {self._price}, {self._make} ) '
        return f'Car({repr(self._model)}, {repr(self._price)}, {repr(self._make)} ) '

    def caclulate_premium(self,tenure):
        if self._segment == 'Economy':
            return tenure * self._price * 0.15
        else:
            return tenure * self._price * 0.20

    @staticmethod       # decorator used for representing static method
    def showCount():
        print(f'Total cars: {Car.count}')

    # compulsory to make property then onlywe can write setter
    @property
    def make(self):
        return self._make

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, val):
        if val <=0:
            raise ValueError ("price count should be positive")
        else:
            self._price = val

    @classmethod     # change class level val
    def set_count(cls):
        count= 800

    @classmethod # create new instance of class    another way like constructor
    def from_string(cls,data):
        make,model,price = data.split(',')
        return  cls(make,model,price)

newCar = Car("aa","fd",10000)
newCar.price = 3
print(newCar.price)

print(newCar)
print(repr(newCar))