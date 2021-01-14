import os
import time
import json
import datetime

from functions import Functions

def mainMenu():
    os.system("cls")
    try:
        option = int(input("Digite para selecionar:\n\n1 - Funcionarios\n2 - Clientes\n3 - Mercado\n4 - Vendas\n5 - Estoque\n\nQualquer outro numero para encerrar o programa: "))
        if option == 1:
            employeeMenu()
        if option == 2:
            clientMenu()
        if option == 3:
            marketMenu()
        if option == 4:
            salesMenu()
        if option == 5:
            productMenu()
        if option not in [1, 2, 3, 4, 5]:
            os.system("cls")
    except:
        os.system("cls")
        print("\nPor favor digite uma opcao valida\n")
        time.sleep(2)
        mainMenu()

def employeeMenu():
    os.system("cls")
    try:
        option = int(input("Digite para selecionar:\n\n1 - Registrar novo funcionario\n2 - Editar funcionario\n3 - Apagar funcionario\n4 - Para ver um funcionario especifico\n5 - Para ver a lista de funcionarios\n\nQualquer outro numero para voltar ao menu principal o programa: "))
        print(option)
        if option == 1:
            os.system("cls")
            Functions.registerEmployee()
            input("\nAperte enter para voltar a tela anterior")
            employeeMenu()
        if option == 2:
            os.system("cls")
            Functions.showAllEmployees()
            Functions.editEmployee()
            input("\nAperte enter para voltar a tela anterior")
            employeeMenu()
        if option == 3:
            os.system("cls")
            Functions.showAllEmployees()
            Functions.deleteEmployee()
            input("\nAperte enter para voltar a tela anterior")
            employeeMenu()
        if option == 4:
            os.system("cls")
            Functions.showEmployee()
            input("\nAperte enter para voltar a tela anterior")
            employeeMenu()
        if option == 5:
            os.system("cls")
            Functions.showAllEmployees()
            input("\nAperte enter para voltar a tela anterior")
            employeeMenu()

        if option not in [1, 2, 3, 4, 5]:
            mainMenu()
    except Exception as e:
        print(e)
        print("\nPor favor digite uma opcao valida\n")
        time.sleep(2)
        employeeMenu()

def clientMenu():
    os.system("cls")
    try:
        option = int(input("Digite para selecionar:\n\n1 - Registrar novo cliente\n2 - Editar cliente\n3 - Apagar cliente\n4 - Para ver um cliente especifico\n5 - Para ver a lista de clientes\n\nQualquer outro numero para voltar ao menu principal o programa: "))
        if option == 1:
            os.system("cls")
            Functions.registerClient()
            input("\nAperte enter para voltar a tela anterior")
            clientMenu()
        if option == 2:
            os.system("cls")
            Functions.showAllClients()
            Functions.editClient()
            input("\nAperte enter para voltar a tela anterior")
            clientMenu()
        if option == 3:
            os.system("cls")
            Functions.showAllClients()
            Functions.deleteClient()
            input("\nAperte enter para voltar a tela anterior")
            clientMenu()
        if option == 4:
            os.system("cls")
            Functions.showClient()
            input("\nAperte enter para voltar a tela anterior")
            clientMenu()
        if option == 5:
            os.system("cls")
            Functions.showAllClients()
            input("\nAperte enter para voltar a tela anterior")
            clientMenu()
        if option not in [1, 2, 3, 4, 5]:
            mainMenu()

    except Exception as e:
        print(e)
        print("\nPor favor digite uma opcao valida\n")
        time.sleep(2)
        clientMenu()

def marketMenu():
    os.system("cls")
    try:
        option = int(input("Digite para selecionar:\n\n1 - Verificar informações do mercado\n2 - Editar informações do mercado\n\nQualquer outro numero para voltar ao menu principal o programa: "))
        if option == 1:
            os.system("cls")
            Functions.getMarketInfo()
            input("\nAperte enter para voltar a tela anterior")
            marketMenu()
        if option == 2:
            os.system("cls")
            Functions.getMarketInfo()
            Functions.editMarketInfo()
            input("\nAperte enter para voltar a tela anterior")
            marketMenu()
        if option not in [1, 2]:
            mainMenu()
    except:
        os.system("cls")
        print("\nPor favor digite uma opcao valida\n")
        time.sleep(2)
        marketMenu()

def salesMenu():
    os.system("cls")
    try:
        option = int(input("Digite para selecionar:\n\n1 - Registrar nova venda\n2 - Para ver uma venda especifica\n3 - Para ver a lista de vendas\n\nQualquer outro numero para voltar ao menu principal o programa: "))
        if option == 1:
            os.system("cls")
            Functions.registerSale()
            input("\nAperte enter para voltar a tela anterior")
            salesMenu()
        if option == 2:
            os.system("cls")
            Functions.showSale()
            input("\nAperte enter para voltar a tela anterior")
            salesMenu()
        if option == 3:
            os.system("cls")
            Functions.showAllSales()
            input("\nAperte enter para voltar a tela anterior")
            salesMenu()
        if option not in [1, 2, 3]:
            mainMenu()
    except Exception as e:
        print(e)
        os.system("cls")
        print("\nPor favor digite uma opcao valida\n")
        time.sleep(2)
        salesMenu()

def productMenu():
    os.system("cls")
    try:
        option = int(input("Digite para selecionar:\n\n1 - Registrar novo produto no inventario\n2 - Editar produto\n3 - Apagar produto\n4 - Para ver um produto especifico\n5 - Para ver a lista de itens\n\nQualquer outro numero para voltar ao menu principal o programa: "))
        if option == 1:
            os.system("cls")
            Functions.registerProduct()
            input("\nAperte enter para voltar a tela anterior")
            productMenu()
        if option == 2:
            os.system("cls")
            Functions.showAllProducts()
            Functions.editProduct()
            input("\nAperte enter para voltar a tela anterior")
            productMenu()
        if option == 3:
            os.system("cls")
            Functions.showAllProducts()
            Functions.deleteProduct()
            input("\nAperte enter para voltar a tela anterior")
            productMenu()
        if option == 4:
            os.system("cls")
            Functions.showProduct()
            input("\nAperte enter para voltar a tela anterior")
            productMenu()
        if option == 5:
            os.system("cls")
            Functions.showAllProducts()
            input("\nAperte enter para voltar a tela anterior")
            productMenu()
        if option not in [1, 2, 3, 4, 5]:
            mainMenu()
    except Exception as e:
        print(e)
        os.system("cls")
        print("\nPor favor digite uma opcao valida\n")
        time.sleep(2)
        productMenu()


mainMenu()
