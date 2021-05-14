from employees.employee import Employee
from payment.accountdeposit import AccountDeposit
from payment.mailcheck import MailCheck
from payment.cashcheck import CashCheck
import datetime

class Hourly(Employee):
    def __init__(self, name, address, salary):
        super().__init__(name, address)
        self.kind = "Horista"
        self._salary = float(salary)
        self.workedHours = 0
        self.workedExtraHours = 0
        self.paymentMethod = None
        self.wallet = []
        self.netIncome = float(0)
        # self.defaultPayDay = True
        # self.paymentRecord = []

    def setPaymentMethod(self, method):
        self.paymentMethod = method

    def TimeCard(self, hours):
        if (hours <= 8):
            self.workedHours += hours
        else:
            self.workedHours += 8
            self.workedExtraHours += (hours - 8)
    
    def EditHourly(self, name, address, salary):
        self.name = name
        self.address = address
        self._salary = float(salary)

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

    # def CheckIfPayed(self, todaysdate):
    #     if not self.paymentRecord:  #check if paymentRecord[] is empty
    #         print("{} ainda não foi pago".format(self.name))
    #         return False 
    #     else:
    #         if (self.paymentRecord[-1].month == todaysdate.month):
    #             print("{} já foi pago".format(self.name))
    #             return True
    #         else:
    #             print("{} ainda não foi pago".format(self.name))
    #             return False
    
    # def PaymentVoucher(self, payday):
    #     self.paymentRecord.append(payday)

    # def PrintLastPaymentVoucher(self):
    #     if not self.paymentRecord:
    #         print("{} ainda não foi pago".format(self.name))
    #     else:
    #         print(self.paymentRecord[-1])


    def __str__(self):
        return super().__str__() + 'Tipo de empregado: {}\nHoras trabalhadas: {}\nHoras extras trabalhadas: {}'.format(self.kind, self.workedHours, self.workedExtraHours)

# k1 = Hourly("Rafa", "Matao", 500, 1.04)
# print(k1)