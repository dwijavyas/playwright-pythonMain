#self key is mandatory to call variables in methods
#class and instance var are diff
#instance var is attached to object
#constructor name should be __init__

class Calculator:

    num = 100 #class variable - constant

    def __init__(self, a, b):       #whenever call variable inside methods/func, call it using self obj
        self.firtnumber = a
        self.secondnumber = b
        print('i am default constructor, called automatically when obj is created')

    def getData(self):
        print("i am now executing")

    def summation(self):
        return self.firtnumber + self.secondnumber + Calculator.num



#constructor is auto called when obj of class is created
#def __init__(self) is the default constructor - auto called when obj i screated
#when obj not created we need to expilicitly define
obj = Calculator(2, 3)
obj.getData()
print(obj.num)
print(obj.summation())

obj1 = Calculator(4, 5)
obj1.getData()
print(obj1.summation())

