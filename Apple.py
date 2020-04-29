from AmountUtil import validAmount
class Apple:

    def __init__(self, amount):
        self.amount = amount
        self.dollar_rate = 5
        self.banana_rate = 2

    def getDollar(self):
        if validAmount(self):
            result = self.amount // self.dollar_rate
            print("output on screen:{}".format(result))

    def getBanana(self):
        if validAmount(self):
            result = self.amount * self.banana_rate
            print("output on screen:{}".format(result))

apple = Apple(5)
apple.getDollar()
apple.getBanana()