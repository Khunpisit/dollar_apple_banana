from AmountUtil import validAmount

class Banana:

    def __init__(self, amount = 0):
        self.amount = amount
        self.dollar_rate = 10
        self.apple_rate = 2

    def getDollar(self):
        if validAmount(self):
            result = self.amount / self.dollar_rate
            print("output on screen:{}".format(result))

    def getApple(self):
        if validAmount(self):
            result = self.amount / self.apple_rate
            print("output on screen:{}".format(result))

banana = Banana(5)
banana.getDollar()
banana.getApple()