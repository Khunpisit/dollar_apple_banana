def validAmount(self):
    if not isinstance(self.amount, int):
        print("Your payment is incorrect format. Please try again!")
        return False
    elif self.amount < 1:
        print("Please pay money before!")
        return False
    else:
        return True