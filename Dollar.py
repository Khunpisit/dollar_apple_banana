from AmountUtil import validAmount

class Dollar:

    def __init__(self, amount):
        self.amount = amount
        self.apple_rate = 5
        self.banana_rate = 10

    def getApple(self):
        if validAmount(self):
            result = self.amount * self.apple_rate
            print("output on screen:{}".format(result))

    def getBanana(self):
        if validAmount(self):
            result = self.amount * self.banana_rate
            print("output on screen:{}".format(result))

dollar = Dollar(20)
dollar.getApple()
dollar.getBanana()

dollar = Dollar(0)
dollar.getApple()


dollar = Dollar('abc')
dollar.getBanana()