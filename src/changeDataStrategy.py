from abc import ABC, abstractmethod

class ChangeData(ABC):

    @abstractmethod
    def changePersonalData(self, dictionary, key):
        pass

class SimpleChange(ChangeData):
    
    def changePersonalData(self, dictionary, key):
        newName = input("Digite o novo nome: ")
        newAddress = input("Digite o novo endereço: ")
        newSalary = float(input("Digite o novo salário: "))
        dictionary[key]['worker'].Edit(newName, newAddress, newSalary)
    
class DifferentChange(ChangeData):

    def changePersonalData(self, dictionary, key):
        newName = input("Digite o novo nome: ")
        newAddress = input("Digite o novo endereço: ")
        newSalary = float(input("Digite o novo salário: "))
        newBonus = float(input("Digite o novo bonus: "))
        dictionary[key]['worker'].Edit(newName, newAddress, newSalary, newBonus)
