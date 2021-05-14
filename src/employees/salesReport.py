class SalesReport():
    def __init__(self, date, value):
        self.date = date
        self.value = value

    def __str__(self):
        return '(Data: {}, Valor: {})'.format(self.date, self.value)