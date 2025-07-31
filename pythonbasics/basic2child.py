from basic1parent import Calculator


class ChildImp(Calculator):

    num2 = 200

    def getCompleteData(self):
        return self.num2 + self.summation() + self.num
    
#there is self in method so we need to call the method by creating obj
obj2 = ChildImp(5, 6)
print(obj2.getCompleteData())