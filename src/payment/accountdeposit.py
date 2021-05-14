class AccountDeposit:
    def __init__(self, name, value, date):
        self.name = name
        self.value = float(value)
        self.date = date

    def __str__(self):
        return "Nome: {}\nValor R${}\nData de pagamento {}".format(self.name, self.value, self.date)