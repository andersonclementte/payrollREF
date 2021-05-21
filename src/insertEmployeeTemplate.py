from abc import ABC, abstractmethod
from employees.hourly import Hourly
from employees.salaried import Salaried, Comissioned

class InsertEmployee(ABC):


    @abstractmethod
    def instantiate(self):
        pass
    
    def add(self):
        self.name = input("Digite o nome: ")
        self.address = input("Digite o endereço: ")
        self.salary = float(input("Digite o salario: "))
        return self.instantiate() #maldito self
    
class InsertHourly(InsertEmployee):

    def instantiate(self):
        self.employee = Hourly(self.name, self.address, self.salary)
        return self.employee

class InsertSalaried(InsertEmployee):

    def instantiate(self):
        self.employee = Salaried(self.name, self.address, self.salary)
        return self.employee

class InsertComissioned(InsertEmployee):

    def instantiate(self):
        self.bonus = float(input("Digite o bônus percentual (%): "))
        self.employee = Comissioned(self.name, self.address, self.salary, self.bonus)
        return self.employee