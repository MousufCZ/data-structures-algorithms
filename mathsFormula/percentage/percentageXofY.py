class PercXOfY():
    def __init__(self,x ,percent):
        self.x = x
        self.y = None
        self.percent = percent
        self.numOfYears = None

    # Page 64
    def percXofY(self):
        x = self.x
        percent = self.percent

        toDecimal = percent/100
        percentageOfX = toDecimal * x 

        return print(percentageOfX)
    
    def amountAftIncrease(self):
        x = self.x
        percent = self.percent
        multiplier = 1 + (percent / 100)
        multiplyX = multiplier * x
        return print(multiplyX)

    def amountAftDecrease(self):
        x = self.x
        percent = self.percent
        multiplier = 1 - (percent / 100)
        multiplyX = multiplier * x
        return print(multiplyX)
    
    def expressXAsPercOfY(self, y):
        self.y = y
        x = self.x
        percent = (y / x) * 100
        return print(percent)

    def percChange(self, change):
        original = self.x
        self.y = change
        percChange = (self.y / original) * 100
        return print(percChange)
    
    # Page 65
    def findOrigValueFromIncreasePerc(self, y):
        percent = self.percent
        self.y = y
        increasePerc = 100 + percent
        #print(increasePerc)
        find1Perc = self.y / increasePerc
        #print(find1Perc)
        originalVal = find1Perc * 100
        return print(originalVal)

    def findOrigValueFromDecreasePerc(self, y):
        percent = self.percent
        self.y = y
        decreasePerc = 100 - percent
        #print(increasePerc)
        find1Perc = self.y / decreasePerc
        #print(find1Perc)
        originalVal = find1Perc * 100
        return print(originalVal)

    def simpleInterst(self, numOfYears):
        numOfYears = self.numOfYears
        return print(numOfYears)
"""
Implement page 66. Implement simple interest
need new 
self.numOfYears
"""

def testPercXofY():
    x = 1.2
    y = 0.96
    percent = 20
    numOfYears = 4
    
    test = PercXOfY(x, percent)
    test.percXofY()
    print("=====")
    test.amountAftIncrease()
    print("=====")
    test.amountAftDecrease()
    print("=====")
    test.expressXAsPercOfY(y)
    print("=====")
    test.percChange(y)
    print("=====")
    test.findOrigValueFromIncreasePerc(y)
    print("=====")
    print("=====")
    test.findOrigValueFromDecreasePerc(y)
    print("=====")
    print("=====")
    test.numOfYears(y)
    print("=====")


if __name__ == "__main__":
    testPercXofY()