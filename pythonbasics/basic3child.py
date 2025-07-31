from basic1parent import Calculator


class ChildImp1(Calculator):

    num3 = 300

    #creating const in child 2 cz parent also has const to define variables - its mandatory
    def __init__(self):
        Calculator.__init__(self, 7, 6)

    def getFullData(self):
        return self.num3 + self.num + self.summation()
    
obj4 = ChildImp1()
print(obj4.getFullData())