class Bank:
    def __init__(self, balance):
        self.__balance = balance  # private variable

    def get_balance(self):
        return self.__balance

b = Bank(10000)
print(b.get_balance())