# def add(*args):
#     sum = 0
#     for n in args:
#         sum += n
#     return sum
# print(add(1,3,1))
#
# def calculate(n, **kwargs):
#     n += kwargs["add"]
#     n *= kwargs["multiply"]
#     return n
# print(calculate(1, add=3, multiply=5))

class Car:

    def __init__(self, **kw):
        self.brand = kw["brand"]
        #         File
        #         "C:\Users\binid25x\PycharmProjects\PythonProject\day27-start\playground.py", line 17, in __init__
        #         self.brand = kw["brand"]
        #         ~~ ^ ^ ^ ^ ^ ^ ^ ^ ^
        # KeyError: 'brand'
        self.model = kw.get("model")
        # None is no argument
        self.price = kw["price"]
        #         File "C:\Users\binid25x\PycharmProjects\PythonProject\day27-start\playground.py", line 24, in __init__
        #         self.price = kw["price"]
        #         ~~ ^ ^ ^ ^ ^ ^ ^ ^ ^
        # KeyError: 'price'

car = Car(brand="Proton", price=25000)
print(car.model)