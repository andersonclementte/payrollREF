from abc import ABC, abstractmethod
class Employee(ABC):
    @abstractmethod
    def __init__(self, name, address):
        self.name = name
        self.address = address

    def companyEmail(self):
        return '{}@company.com'.format(self.name)
    
    def __str__(self):
        return 'Dados do funcionário:\nNome: {}\nEndereco: {}\n'.format(self.name, self.address)