import datetime as dt
from employees.employee import Employee
from employees.hourly import Hourly
from employees.salaried import Salaried, Comissioned
from employees.salesReport import SalesReport
from union.union import Union
from payment.accountdeposit import AccountDeposit
from payment.mailcheck import MailCheck
from payment.cashcheck import CashCheck
from os import system

#global variables and stuff
clear = lambda: system('clear')
deletedIds = []
lastId = 0
unionID = 0
today = dt.datetime(2021,1,28)

#Add employee block
def getId():
    if (len(deletedIds) > 0):
        return deletedIds.pop(0) #return first item in list and deletes it
    else:
        global lastId
        lastId += 1
        return lastId

def getUnionId():
    global unionID
    unionID += 1
    return unionID

def menu():
    print("Escolha uma opção:")
    print("(1) - Adicionar Funcionário")
    print("(2) - Remover Funcionário")
    print("(3) - Exibir quantidade de funcionários cadastrados")
    print("(4) - Ver dados individuais")
    print("(5) - Adicionar ao sindicato")
    print("(6) - Lançar cartão de ponto")
    print("(7) - Lançar resultado de vendas")
    print("(8) - Ver resultado de venda")
    print("(9) - Lançar taxa de serviço")
    print("(10) - Editar funcionário")
    print("(0) - Voltar")
    ans = int(input())
    return ans

def employeeChoose():
    clear()
    print("Escolha uma opção:")
    print("(1) - Horista")
    print("(2) - Assalariado")
    print("(3) - Comissionado")
    print("(0) - Cancelar")
    ans = int(input())
    return ans

def insertHourly():
    #e2 = Hourly('ze', "friburgo", 500, 1.04)
    clear()
    print("Registro de funcionário Horista:")
    name = input("Digite o nome: ")
    address = input("Digite o endereço: ")
    salary = float(input("Digite o salario: "))
    employee = Hourly(name, address, salary)
    clear()

    return employee

def insertSalaried():
    #e3 = Salaried('figo', "porto", 5000)
    clear()
    print("Registro de funcionário assalariado:")
    name = input("Digite o nome: ")
    address = input("Digite o endereço: ")
    salary = float(input("Digite o salario: "))
    employee = Salaried(name, address, salary)
    clear()

    return employee

def insertComissioned():
    # e4 = Comissioned("tiao", "mcz", 2000, 140)
    clear()
    print("Regitro de funcionário comissionado:")
    name = input("Digite o nome: ")
    address = input("Digite o endereço: ")
    salary = float(input("Digite o salario: "))
    bonus = float(input("Digite o bônus percentual (%): "))
    employee = Comissioned(name, address, salary, bonus)
    clear()
    return employee

def addEmployee(option):

    if option == 1:
       employee = insertHourly()
    elif option == 2:
        employee = insertSalaried()
    elif option == 3:
        employee = insertComissioned()
    
    return employee
#add employee end block
#-----------------------
#remove employee block
def removeFromSchedule(key, schedule):
    if key in schedule['weekly']:
        schedule['weekly'].remove(key)
    if key in schedule['bi-weekly']:
        schedule['bi-weekly'].remove(key)
    if key in schedule['monthly']:
        schedule['monthly'].remove(key)

def removeEmployee(dictionary, schedule):
    clear()
    key = int(input("Digite o ID do funcionário: "))
    if (key not in dictionary):
        print("Id inválida, nenhum funcionário deletado.")
        #return dictionary
    else:
        name = dictionary[key]['worker'].name
        deletedIds.append(key)
        removeFromSchedule(key, schedule)
        del dictionary[key]
        print("Operação bem sucedida, funcionário {} deletado.".format(name))
        #return dictionary
#end of remove employee block
#---------------------------
#payment method block
def choosePaymentMethod():
    clear()
    print("Escolha uma opção:")
    print("(1) - Deposito em conta")
    print("(2) - Cheque em mãos")
    print("(3) - Cheque pelos correios")
    ans = int(input())
    return ans

def employeeStats(dictionary):
    clear()
    if len(dictionary) == 1:
        print("A folha de pagamento contém 1 funcionário(a).\n")
    else:
        print("A folha de pagamento contém %d funcionários(as).\n" %len(dictionary))

def findEmployee(dictionary, uniondict, schedule):
    clear()
    key = int(input("Digite o ID do funcionário: "))
    if (key not in dictionary):
        print("ID inválida.")
    else:
        print("-----------------------------------")
        print(dictionary[key]['worker'])
        if (dictionary[key]['worker'].kind == 'Comissionado'):
            print("Sales report: {}".format(len(dictionary[key]['sales'])))
            
        if key in schedule['weekly']:
            print("Funcionário pago semanalmente")
        elif key in schedule['bi-weekly']:
            print("Funcionário pago bi-semanalmente")
        elif key in schedule['monthly']:
            print("Funcionário pago mensalmente")
        print("Forma de pagamento: {}".format(dictionary[key]['worker'].paymentMethod))
        dictionary[key]['worker'].GetNetIncome()
        dictionary[key]['worker'].PrintLastPayment()
        print("-----------------------------------")

        print("Informações sindicais:")
        if ('unionKey' in dictionary[key]):
            print("Empregado sindicalizado.")
            print(uniondict[ dictionary[key]['unionKey'] ])
        else:
            print("Empregado não sindicalizado.")
        print("--------------------------------")

def unionStatus(dictUnion):
    key = int(input("Digite o ID do funcionário: "))
    if (key not in dictUnion):
        print("ID inválida.")
    else:
        print("------------------------------")
        print(dictUnion[key])
        print("------------------------------")

def globalParameters():
    clear()
    print("Id deletadas: {}".format(deletedIds))
    #print(deletedIds)
    print("Proxima id livre: {}".format(lastId+1))

def sendTimeCard(dictionary):
    clear()
    key = int(input("Digite o Id do funcionario: "))
    if (key not in dictionary):
        print("ID inválida.")
        print("------------------------------")
        #return
    elif (dictionary[key]['worker'].kind != "Horista"):
        print("Id inválida, funcionário não horista.")
        print("-------------------------------------")
    else:
        print("Funcionário:",format(dictionary[key]['worker'].name))
        hours = float(input("Digite as horas trabalhadas: "))
        dictionary[key]['worker'].TimeCard(hours)
        print("Cartão submetido com sucesso.")
        print("-----------------------------")

def sendSalesReport(dictionary):
    clear()
    key = int(input("Digite o Id do funcionario: "))
    if (key not in dictionary):
        print("ID inválida.")
        print("------------------------------")
        #return

    elif (dictionary[key]['worker'].kind != "Comissionado"):
        print("Id inválida, funcionário não comissionado.")
        print("------------------------------------------")
    else:
        print("Funcionário:",format(dictionary[key]['worker'].name))
        dateTime = input("Digite a data: ")
        value = float(input("Digite o valor: "))
        saleReport = SalesReport(dateTime, value)
        dictionary[key]['sales'].append(saleReport)
        print("Resultado de vendas submetido com sucesso.")
        print("------------------------------------------")
    
def showSaleReport(dictionary):
    clear()
    key = int(input("Digite o Id do funcionario: "))
    if (key not in dictionary):
        print("ID inválida.")
        print("------------------------------")
    elif (dictionary[key]['worker'].kind != "Comissionado"):
        print("Id inválida, funcionário não comissionado.")
        print("------------------------------------------")
    else:
        print("Funcionário:",format(dictionary[key]['worker'].name))
        print("Resultados de vendas: %d" %len(dictionary[key]['sales']))
        if (len(dictionary[key]['sales']) > 0):
            print("Ultimo resultado de venda: ")
            print(dictionary[key]['sales'][-1])
        print("--------------------------")

def addToUnion(dictionary, unionDic):
    clear()
    key = int(input("Digite o Id do funcionario: "))
    if (key not in dictionary):
        print("ID inválida.")
        print("------------------------------")
    else:
        if ('unionKey' in dictionary[key]):
            print("Funcionário já sindicalizado.")
        else:
            unionId = getUnionId()
            dictionary[key]['unionKey'] = unionId
            unionDic[unionId] = Union(unionId)
            print("Funcionario filiado ao sindicado. ID  sindical número {}". format(unionID))

def sendUnionFee(dictionary, unionDic):
    clear()
    key = int(input("Digite o Id do funcionario: "))
    if (key not in dictionary):
        print("ID inválida.")
        print("------------------------------")
    else:
        if ('unionKey' not in dictionary[key]):
            print("Empregado não sindicalizado.")
        else:
            print("Id sindical: %d" %dictionary[key]['unionKey'])
            value = float(input("Digite o valor da taxa:"))
            unionDic[dictionary[key]['unionKey']].incrementFee(value)
            print("Taxa adicionada com sucesso.")

#Edit employee block
def editEmployeeOptions():
    clear()
    print("Escolha uma opção:")
    print("(1) - Editar dados pessoais")
    print("(2) - Editar tipo de funcionário")
    print("(3) - Alterar vinculo sindical")
    print("(4) - Alterar agenda de pagamentos")
    print("(5) - Alterar metodo de pagamento")
    print("(0) - Cancelar")
    ans = int(input())
    return ans

def changePersonalData(dictionary, key):
    # newName = input("Digite o novo nome: ")
    # newAddress = input("Digite o novo endereço: ")
    # newSalary = float(input("Digite o novo salário: "))
    # if (dictionary[key]['worker'].kind == 'Horista'):
    #     dictionary[key]['worker'].EditHourly(newName, newAddress, newSalary)
    #     print("Funcionário editado com sucesso.")
    #     print("--------------------------------")

    # elif (dictionary[key]['worker'].kind == 'Assalariado'):
    #     dictionary[key]['worker'].EditSalaried(newName, newAddress, newSalary)
    #     print("Funcionário editado com sucesso.")
    #     print("--------------------------------")

    # elif (dictionary[key]['worker'].kind == 'Comissionado'):
    #     newBonus = float(input("Digite o novo bonus: "))
    #     dictionary[key]['worker'].EditComissioned(newAddress, newAddress, newSalary, newBonus)
    #     print("Funcionário editado com sucesso.")
    #     print("--------------------------------")
    dictionary[key]['worker'].EditData(dictionary, key)
    print("Funcionário editado com sucesso.")
    print("--------------------------------")

def changeToHourly(dictionary, key):
    name = dictionary[key]['worker'].name
    address = dictionary[key]['worker'].address
    salary = dictionary[key]['worker']._salary
    editedEmployee = Hourly(name, address, salary)
    dictionary[key]['worker'] = editedEmployee
    print("Tipo de funcionário editado com sucesso!")
    print(dictionary[key]['worker'])

def changeToSalaried(dictionary, key):
    name = dictionary[key]['worker'].name
    address = dictionary[key]['worker'].address
    salary = dictionary[key]['worker']._salary
    editedEmployee = Salaried(name, address, salary)
    dictionary[key]['worker'] = editedEmployee
    print("Tipo de funcionário editado com sucesso!")
    print(dictionary[key]['worker'])

def changeToComissioned(dictionary, key):
    name = dictionary[key]['worker'].name
    address = dictionary[key]['worker'].address
    salary = dictionary[key]['worker']._salary
    bonus = float(input("Digite o bônus do funcionário: "))
    editedEmployee = Comissioned(name, address, salary, bonus)
    dictionary[key]['worker'] = editedEmployee
    print("Tipo de funcionário editado com sucesso!")
    print(dictionary[key]['worker'])

def changeEmployeeType(dictionary, key):
    if (dictionary[key]['worker'].kind == 'Horista'):
        print("Escolha o novo tipo para o funcionário: ")
        print("(1) - Comissionado")
        print("(2) - Assalariado")
        choose = int(input())
        if (choose == 1):
            changeToComissioned(dictionary, key)
        elif (choose == 2):
            changeToSalaried(dictionary, key)
        else:
            print("Cancelando...")
        

    elif (dictionary[key]['worker'].kind == 'Assalariado'):
        print("Escolha o novo tipo para o funcionário: ")
        print("(1) - Comissionado")
        print("(2) - Horista")
        choose = int(input())
        if (choose == 1):
            changeToComissioned(dictionary, key)
        elif (choose == 2):
            changeToHourly(dictionary, key)
        else:
            print("Cancelando...")
        

    elif (dictionary[key]['worker'].kind == 'Comissionado'):
        print("Escolha o novo tipo para o funcionário: ")
        print("(1) - Horista")
        print("(2) - Assalariado")
        choose = int(input())
        if (choose == 1):
            changeToHourly(dictionary, key)
        elif (choose == 2):
            changeToSalaried(dictionary, key)
        else:
            print("Cancelando...")

def changePaymentMethod(dictionary, key):
    if (dictionary[key]['worker'].paymentMethod == 'Deposito em conta'):
        print("Escolha o novo metodo de pagamento: ")
        print("(1) - Cheque em maos")
        print("(2) - Cheque pelos correios")
        choose = int(input())
        if (choose == 1):
            dictionary[key]['worker'].setPaymentMethod('Cheque em maos')
        elif (choose == 2):
            dictionary[key]['worker'].setPaymentMethod('Cheque pelos correios')
        else:
            print("Cancelando...")
        

    elif (dictionary[key]['worker'].paymentMethod == 'Cheque em maos'):
        print("Escolha o novo metodo de pagamento: ")
        print("(1) - Deposito em conta")
        print("(2) - Cheque pelos correios")
        choose = int(input())
        if (choose == 1):
            dictionary[key]['worker'].setPaymentMethod('Deposito em conta')
        elif (choose == 2):
            dictionary[key]['worker'].setPaymentMethod('Cheque pelos correios')
        else:
            print("Cancelando...")
        

    elif (dictionary[key]['worker'].paymentMethod == 'Cheque pelos correios'):
        print("Escolha o novo metodo de pagamento: ")
        print("(1) - Cheque em maos")
        print("(2) - Deposito em conta")
        choose = int(input())
        if (choose == 1):
            dictionary[key]['worker'].setPaymentMethod('Cheque em maos')
        elif (choose == 2):
            dictionary[key]['worker'].setPaymentMethod('Deposito em conta')
        else:
            print("Cancelando...")

def changeUnionStatus(dictionary, key, unionDic):
    if ('unionKey' in dictionary[key]): 
        unionID = dictionary[key]['unionKey']
        del unionDic[unionID]
        del dictionary[key]['unionKey']
        #print("Funcionário {} foi removido do sindicato".format(dictionary[key]['worker'].name))
        print("Removido do sindicato.")
        
    else:
        unionId = getUnionId()
        dictionary[key]['unionKey'] = unionId
        unionDic[unionId] = Union(unionId)
        print("Funcionario filiado ao sindicado. ID sindical numero {}". format(unionId))

def schedulePaymentOptions():
    clear()
    print("Escolha uma opção:")
    print("(1) - Pagamento semanal")
    print("(2) - Pagamento bi-semanal")
    print("(3) - Pagamento mensal")
    print("(0) - Cancelar")
    ans = int(input())
    return ans

def changePaymentSchedule(option, key, schedule):
    if key in schedule['weekly']:
        schedule['weekly'].remove(key)
    if key in schedule['bi-weekly']:
        schedule['bi-weekly'].remove(key)
    if key in schedule['monthly']:
        schedule['monthly'].remove(key)

    if(option == 1):
        schedule['weekly'].add(key)
    elif (option == 2):
        schedule['bi-weekly'].add(key)
    elif (option == 3):
        schedule['monthly'].add(key)

def editEmployee(dictionary, unionDic, schedule):
    clear()
    print("Atenção, editar um funcionário pode invalidar alguns atributos previamente configurados.")
    res = input("Deseja continuar? (S/n)")
    if (res == 's' or res == 'S'):
        key = int(input("Digite o Id do funcionario: "))
        if (key not in dictionary):
            print("ID inválida.")
            print("------------------------------")
        else:
            option = editEmployeeOptions()
            if (option == 1):
                changePersonalData(dictionary, key)
            elif (option == 2):
                changeEmployeeType(dictionary, key)
            elif (option == 3):
                changeUnionStatus(dictionary, key, unionDic)
            elif (option == 4):
                payoption = schedulePaymentOptions()
                if (payoption > 3):
                    print("Cancelado")
                else:
                    changePaymentSchedule(payoption, key, schedule)
                    print("Agenda alterada com sucesso.")
            elif (option == 5):
                changePaymentMethod(dictionary, key)

    else:
        print("Cancelando...")
#end of edit block

def openPayRoll(employeeDict, unionDict, payrollSchedule):
        while True:
            menuoption = menu()
            
            if menuoption == 1:
                individualDict = {}
                value = getId()
                employeeOption = employeeChoose()
                if (employeeOption != 0):
                    newEmployee = addEmployee(employeeOption)

                    if (employeeOption == 1):
                        try:
                            payrollSchedule['weekly'].add(value)
                        except KeyError:
                            payrollSchedule['weekly'] = {value}

                    elif (employeeOption == 2):
                        try:
                            payrollSchedule['monthly'].add(value)
                        except KeyError:
                            payrollSchedule['monthly'] = {value}

                    elif (employeeOption == 3):
                        try:
                            payrollSchedule['bi-weekly'].add(value)
                        except KeyError:
                            payrollSchedule['bi-weekly'] = {value}
                        individualDict['sales'] = []

                    paymentOption  = choosePaymentMethod()
                    if paymentOption == 1:
                        newEmployee.setPaymentMethod('Deposito em conta')
                    elif paymentOption == 2:
                        newEmployee.setPaymentMethod('Cheque em maos')
                    elif paymentOption == 3:
                        newEmployee.setPaymentMethod('Cheque pelos correios')
                    
                    individualDict['worker'] = newEmployee
                    #individualDict['worker'] = addEmployee(employeeOption)
                    
                        
                    unionOption = input("Deseja entrar no sindicato? (S/N)")
                    if (unionOption == 's' or unionOption == 'S'):
                        unionId = getUnionId()
                        individualDict['unionKey'] = unionId
                        unionDict[unionId] = Union(unionId)
                        print("Funcionario filiado ao sindicado. ID sindical numero {}". format(unionId))
                    else:
                        print("Funcionário não filiado ao sindicato.")

                    employeeDict[value] = individualDict
                    print("Operação bem sucedida, Id do funcionário: %d" %value)
                    print("------------------------------")
                else:
                    print("Voltando...")
                    print("------------------------------")


            elif menuoption == 2:
                removeEmployee(employeeDict, payrollSchedule)

            elif menuoption == 3:
                employeeStats(employeeDict) 

            elif menuoption == 4:
                findEmployee(employeeDict, unionDict, payrollSchedule)

            elif menuoption == 5:
                addToUnion(employeeDict, unionDict)

            elif menuoption == 6:
                if (len(employeeDict) > 0):
                    sendTimeCard(employeeDict)
                else:
                    print("A folha de pagamento está vazia")
                    print("------------------------------")

            elif menuoption == 7:
                if (len(employeeDict) > 0):
                    sendSalesReport(employeeDict)
                else:
                    print("A folha de pagamento está vazia")
                    print("------------------------------")
            
            elif menuoption == 8:
                showSaleReport(employeeDict)

            elif menuoption == 9:
                sendUnionFee(employeeDict, unionDict)

            elif menuoption == 10:
                editEmployee(employeeDict, unionDict, payrollSchedule)

            else:
                print("Saindo...")
                clear()
                break

#runs the payments begin:
def checkIfFriday(day):
    if (day.weekday() == 4):
        return True
    else:
        return False

def checkLastWorkDay(day):
    thimonth = day.month
    nextmonth = thimonth+1
    tomorrow = day + dt.timedelta(days=1)
    nextMonday = day + dt.timedelta(days=3)
    if (day.weekday() >= 0 and day.weekday() <= 4 and tomorrow.month == nextmonth):
        return True
    elif (day.weekday() >= 0 and day.weekday() <= 4 and nextMonday.month == nextmonth):
        return True
    else:
        return False

def calcPaymentValue(dictionary, unionDict, key):
    if(dictionary[key]['worker'].kind == 'Horista'):
        result = dictionary[key]['worker'].GetIncome()
        #print("Rendimentos: R${}".format(result))
    elif(dictionary[key]['worker'].kind == 'Assalariado'):
        result = dictionary[key]['worker'].GetIncome()
        #print("Rendimentos: R${}".format(result))
    elif(dictionary[key]['worker'].kind == 'Comissionado'):
        salary = dictionary[key]['worker'].GetSalary()
        bonusPercentage = (dictionary[key]['worker'].GetBonus())/100
        salesResult = 0
        for sale in dictionary[key]['sales']:
            salesResult += sale.value
        dictionary[key]['sales'].clear()
        result = bonusPercentage*salesResult + salary
        #print("Rendimentos: R${}".format(result))

    if ('unionKey' in dictionary[key]):
        fee = unionDict[ dictionary[key]['unionKey'] ].getFee()
        return result - fee
    else:
        return result

def weeklyPayment(dictionary, unionDic, schedule, day):
    for key in schedule['weekly']:  #weekly payment
                payment = calcPaymentValue(dictionary, unionDic, key)
                if (dictionary[key]['worker'].paymentMethod == 'Deposito em conta'):
                    deposit = AccountDeposit(dictionary[key]['worker'].name, payment, day)
                    dictionary[key]['worker'].PutInWallet(deposit)
                    print("Pagamento semanal efetuado")

                elif (dictionary[key]['worker'].paymentMethod == 'Cheque em maos'):
                    check = CashCheck(dictionary[key]['worker'].name, payment, day)
                    dictionary[key]['worker'].PutInWallet(check)
                    print("Pagamento semanal efetuado")

                elif (dictionary[key]['worker'].paymentMethod == 'Cheque pelos correios'):
                    check = MailCheck(dictionary[key]['worker'].name, payment, day)
                    dictionary[key]['worker'].PutInWallet(check)
                    print("Pagamento semanal efetuado")

def biweeklyPayment(dictionary, unionDic, schedule, day):
    for key in schedule['bi-weekly']:   #bi-weekly payment
                payment = calcPaymentValue(dictionary, unionDic, key)
                if (dictionary[key]['worker'].paymentMethod == 'Deposito em conta'):
                    deposit = AccountDeposit(dictionary[key]['worker'].name, payment, day)
                    dictionary[key]['worker'].PutInWallet(deposit)
                    print("Pagamento bi-semanal efetuado")
                elif (dictionary[key]['worker'].paymentMethod == 'Cheque em maos'):
                    check = CashCheck(dictionary[key]['worker'].name, payment, day)
                    dictionary[key]['worker'].PutInWallet(check)
                    print("Pagamento bi-semanal efetuado")
                elif (dictionary[key]['worker'].paymentMethod == 'Cheque pelos correios'):
                    check = MailCheck(dictionary[key]['worker'].name, payment, day)
                    dictionary[key]['worker'].PutInWallet(check)
                    print("Pagamento bi-semanal efetuado")

def monthlyPayment(dictionary, unionDic, schedule, day):
    for key in schedule['monthly']:  #weekly payment
                payment = calcPaymentValue(dictionary, unionDic, key)

                if (dictionary[key]['worker'].paymentMethod == 'Deposito em conta'):
                    deposit = AccountDeposit(dictionary[key]['worker'].name, payment, day)
                    dictionary[key]['worker'].PutInWallet(deposit)
                    print("Pagamento mensal efetuado")

                elif (dictionary[key]['worker'].paymentMethod == 'Cheque em maos'):
                    check = CashCheck(dictionary[key]['worker'].name, payment, day)
                    dictionary[key]['worker'].PutInWallet(check)
                    print("Pagamento mensal efetuado")

                elif (dictionary[key]['worker'].paymentMethod == 'Cheque pelos correios'):
                    check = MailCheck(dictionary[key]['worker'].name, payment, day)
                    dictionary[key]['worker'].PutInWallet(check)
                    print("Pagamento mensal efetuado")

def payEmployees(dictionary, unionDic, schedule, day):
    if len(dictionary) == 0:
        print("Não há funcionários para serem pagos")
    elif (day.weekday() > 4):
        print("É fim de semana, nenhum pagamento feito.")
    else:
        if (checkIfFriday(day) or checkLastWorkDay(day)):
            weeklyPayment(dictionary, unionDic, schedule, day)
            biweeklyPayment(dictionary, unionDic, schedule, day)
            monthlyPayment(dictionary, unionDic, schedule, day)
        else:
            print("Nenhum pagamento agendado hoje.")


        

def runPayRoll(employeeDict, unionDict, schedule):
    global today
    payEmployees(employeeDict, unionDict, schedule, today)
    today += dt.timedelta(days=1)

def mainMenuOptions():
    print("(1) - Abrir folha de pagamento")
    print("(2) - Rodar folha de pagamento")
    print("(9) - Fechar programa")
    ans = int(input())
    print("---------------------------------------------")
    return ans

# def mainMenu():
#     while True:
#         menuOption = mainMenu()
#         if (menuOption == 1):
#             openPayRoll()


def main():
    employeeDict = {}
    unionDict = {}
    payrollSchedule = {}
    payrollSchedule['weekly'] = set()
    payrollSchedule['bi-weekly'] = set()
    payrollSchedule['monthly'] = set()

    while True:
        print("---------------------------------------------")
        print("Bem vindo.\nData do sistema: {:%A, %d %b %Y}.".format(today) )
        menuOption = mainMenuOptions()
        if (menuOption == 1):
            openPayRoll(employeeDict, unionDict, payrollSchedule)
        elif (menuOption == 2):
            runPayRoll(employeeDict, unionDict, payrollSchedule)
        elif (menuOption == 9):
            print("Saindo...")
            break
        else:
            clear()
            continue

    #openPayRoll(employeeDict, unionDict, payrollSchedule)
    #runPayRoll(employeeDict, unionDict, schedule)


    # date1 = dt.datetime(2021,4,30)
    # checkLastWorkDay(date1)
    # date2 = dt.datetime(2021,5,23)

    # k1 = Hourly("Rafa", "Matao", 500)
    # k1.PaymentVoucher(date1)
    # k1.PaymentVoucher(date2)
    #k1.PrintLastPaymentVoucher()


    
    

   
main()