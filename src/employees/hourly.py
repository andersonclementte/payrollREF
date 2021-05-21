from employees.employee import Employee
from changeDataStrategy import SimpleChange

class Hourly(Employee):

    #Strategy = SimpleChange()

    def __init__(self, name, address, salary):
        super().__init__(name, address)
        self.kind = "Horista"
        self._salary = float(salary)
        self.workedHours = 0
        self.workedExtraHours = 0
        self.paymentMethod = None
        self.wallet = []
        self.netIncome = float(0)

    def setPaymentMethod(self, method):
        self.paymentMethod = method

    def TimeCard(self, hours):
        if (hours <= 8):
            self.workedHours += hours
        else:
            self.workedHours += 8
            self.workedExtraHours += (hours - 8)
    
    def Edit(self, name, address, salary):
        self.name = name
        self.address = address
        self._salary = float(salary)

    def EditData(self, dictionary, key):
        SimpleChange.changePersonalData(self, dictionary, key)

    def GetIncome(self):
        self.income = (self.workedHours*self._salary) + (1.5*(self._salary)*(self.workedExtraHours))
        return self.income

    def PutInWallet(self, payment):
        self.workedHours = 0
        self.workedExtraHours = 0
        self.wallet.append(payment)

    def GetLastPaymentDay(self):
        if (len(self.wallet) == 0):
            return None
        else:
            return self.wallet[-1].date

    def GetNetIncome(self):
        if (len(self.wallet) > 0):
            for x in self.wallet:
                self.netIncome += x.value
        print("Saldo Bancário: R${}".format(self.netIncome))

    def PrintLastPayment(self):
        if (len(self.wallet) > 0):
            print(self.wallet[-1].date)
        else:
            print("Nenhum pagamento recebido")


    def __str__(self):
        return super().__str__() + 'Tipo de empregado: {}\nHoras trabalhadas: {}\nHoras extras trabalhadas: {}'.format(self.kind, self.workedHours, self.workedExtraHours)
