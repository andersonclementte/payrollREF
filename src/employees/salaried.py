from employees.employee import Employee
from employees.salesReport import SalesReport
from payment.accountdeposit import AccountDeposit
from payment.mailcheck import MailCheck
from payment.cashcheck import CashCheck
import datetime

class Salaried(Employee):
    def __init__(self, name, address, salary):
        super().__init__(name, address)
        self.kind = "Assalariado"
        self._salary = float(salary)
        self.paymentMethod = None
        self.wallet = []
        self.netIncome = float(0)

    def EditSalaried(self, name, address, salary):
        self.name = name
        self.address = address
        self._salary = float(salary)
    
    def setPaymentMethod(self, method):
        self.paymentMethod = method

    def GetIncome(self):
        return self._salary
    
    def PutInWallet(self, payment):
        self.wallet.append(payment)

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
        return super().__str__() + 'Tipo de empregado: {}'.format(self.kind)
    
    


class Comissioned(Salaried):
    def __init__(self, name, address, salary, bonus):
        super().__init__(name, address, salary)
        self.kind = "Comissionado"
        self._bonus = float(bonus)
        self.paymentMethod = None
        self.wallet = []
        self.lastIndexPayed = 0
        self.netIncome = float(0)
    #     self.date = None
    #     self.value = None

    # def SalesReport(self, date, value):
    #     self.date = date
    #     self.value = value

    def EditComissioned(self, name, address, salary, bonus):
        self.name = name
        self.address = address
        self.salary = salary
        self.bonus = bonus

    def SetLastIndex(self, index):
        self.lastIndexPayed = index
    
    def getLastIndex(self):
        return self.lastIndexPayed

    def setPaymentMethod(self, method):
        self.paymentMethod = method

    def GetIncome(self, sales):
        if (len(sales) == 0):
            return self._salary
        else:
            balance = 0
            for i in range(self.lastIndexPayed, len(sales)):
                balance += sales[i].value
            self.lastIndexPayed = len(sales)
            income = ((self._bonus)/100)*balance + self._salary
            return income

    def GetSalary(self):
        return self._salary
    
    def GetBonus(self):
        return self._bonus

    def PutInWallet(self, payment):
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
    #     if (bool(self.date)):
    #         return super().__str__() + 'Resultado de vendas:\nData: {}\nValor {}\n'.format(self.date, self.value)
    #     else:
        return super().__str__()
