# a
import os
import time
import json
from time import gmtime, strftime
from prettytable import PrettyTable

from classes.Client import Client
from classes.Employee import Employee
from classes.Market import Market
from classes.Product import Product
from classes.Sale import Sale

class Functions:
    # FUNÇÕES DO FUNCIONARIO
    @staticmethod
    def registerEmployee():
        os.system("cls")
        name, age, address, salary = Functions.__employeeInputs()
        if os.path.exists('./database/employee.json'):
            with open("./database/employee.json") as json_file:
                data = json.load(json_file)
                data["id"] += 1
                data["list"].append({
                    "id": data["id"],
                    "name": name,
                    "age": age,
                    "address": address,
                    "salary": salary,
                    "created_at": strftime("%Y-%m-%d %H:%M:%S", gmtime())   
                })
                with open("./database/employee.json", "w") as output_file:
                    json.dump(data,output_file)
        else:
            with open("./database/employee.json", "w") as output_file:
                    json.dump(
                        {
                            "id": 1,
                            "list": [{
                                "id": 1,
                                "name": name,
                                "age": age,
                                "address": address,
                                "salary": salary,
                                "created_at": strftime("%Y-%m-%d %H:%M:%S", gmtime()) 
                            }]
                        },
                        output_file
                    )

    @staticmethod
    def editEmployee():
        if os.path.exists('./database/employee.json'):
            id = int(input("\nDigite o codigo do funcionario que deseja editar: "))
            employee = Employee(id)
            name, age, address, salary = Functions.__employeeInputs(True)
            if name != '':
                employee.setName(name)
            if age != 0:
                employee.setAge(int(age))
            if address != '':
                employee.setAddress(address)
            if salary != 0:
                employee.setSalary(salary)
        else:
            print("Nenhum funcionario registrado")

    @staticmethod
    def deleteEmployee():
        if os.path.exists('./database/employee.json'):
            id = int(input('\nDigite o codigo do funcionario que deseja apagar: '))
            with open("./database/employee.json") as json_file:
                data = json.load(json_file)
                for i in range(len(data["list"])):
                    if data["list"][i]['id'] == id:
                        del data["list"][i]
                        break
                with open("./database/employee.json", "w") as output_file:
                    json.dump(data,output_file)
        else:
            print("Nenhum funcionario registrado")

    @staticmethod
    def showEmployee():
        if os.path.exists('./database/employee.json'):
            with open("./database/employee.json") as json_file:
                data = json.load(json_file)
                x = PrettyTable(["Codigo", "Nome"])
                x.align["Codigo"] = "l"
                x.align["Nome"] = "l"
                for employee in data["list"]:
                    employee = Employee(employee["id"])
                    x.add_row([employee.getCode(), employee.getName()]) 
                print(x)
                
                id = int(input('\nDigite o codigo do funcionario que deseja visualizar: '))
                x = PrettyTable(["Codigo", "Nome", "Idade", "Endereço", "Salario"])
                x.align["Codigo"] = "l"
                x.align["Nome"] = "l"
                x.align["Idade"] = "l"
                x.align["Endereço"] = "l"
                x.align["Salario em Reais"] = "l"                
                for employee in data["list"]:
                    if employee["id"] == id:
                        employee = Employee(employee["id"])
                        x.add_row([employee.getCode(), employee.getName(), employee.getAge(), employee.getAddress(), "R$" + str(employee.getSalary())]) 
                os.system("cls")
                print(x)
        else:
            print("Nenhum funcionario registrado")

    @staticmethod
    def showAllEmployees():
        if os.path.exists('./database/employee.json'):
            with open("./database/employee.json") as json_file:
                data = json.load(json_file)
                x = PrettyTable(["Codigo", "Nome", "Idade", "Endereço", "Salario"])
                x.align["Codigo"] = "l"
                x.align["Nome"] = "l"
                x.align["Idade"] = "l"
                x.align["Endereço"] = "l"
                x.align["Salario em Reais"] = "l"

                for employee in data["list"]:
                    employee = Employee(employee["id"])
                    x.add_row([employee.getCode(), employee.getName(), employee.getAge(), employee.getAddress(), "R$" + str(employee.getSalary())]) 
                print(x)
        else:
            print("Nenhum funcionario registrado")

    @staticmethod
    def __employeeInputs(edit = False):
        if edit:
            try:
                print()
                name = str(input("Insira o nome do funcionario (caso não queira altera-lo deixe em branco): "))
                age = int(input("Insira a idade de seu funcionario (caso não queira altera-lo digite 0): "))
                address = str(input("Insira o endereço de seu funcionario (caso não queira altera-lo deixe em branco): "))
                salary = float(input("Insira o salario de seu funcionario (caso não queira altera-lo digite 0): "))

                return name, age, address, salary
            except:
                print('\nDigitou algo errado')
                Functions.__employeeInputs(True)
        else:
            try:
                name = str(input("Insira o nome do funcionario: "))
                age = int(input("Insira a idade de seu funcionario: "))
                address = str(input("Insira o endereço de seu funcionario: "))
                salary = float(input("Insira o salario de seu funcionario: "))

                return name, age, address, salary
            except:
                time.sleep(3)
                print('\nDigitou algo errado')
                Functions.__employeeInputs()


    # FUNÇÕES DO CLIENTE
    @staticmethod
    def registerClient():
        os.system("cls")
        name, age, address, cpf, email = Functions.__clientInputs()
        if os.path.exists('./database/client.json'):
            with open("./database/client.json") as json_file:
                data = json.load(json_file)
                data["id"] += 1
                data["list"].append({
                    "id": data["id"],
                    "name": name,
                    "age": age,
                    "address": address,
                    "cpf": cpf,
                    "email": email,
                    "created_at": strftime("%Y-%m-%d %H:%M:%S", gmtime())   
                })
                with open("./database/client.json", "w") as output_file:
                    json.dump(data,output_file)
        else:
            with open("./database/client.json", "w") as output_file:
                    json.dump(
                        {
                            "id": 1,
                            "list": [{
                                "id": 1,
                                "name": name,
                                "age": age,
                                "address": address,
                                "cpf": cpf,
                                "email": email,
                                "created_at": strftime("%Y-%m-%d %H:%M:%S", gmtime())   
                            }]
                        },
                        output_file
                    )

    @staticmethod
    def editClient():
        if os.path.exists('./database/client.json'):
            id = int(input("\nDigite o codigo do cliente que deseja editar: "))
            client = Client(id)
            name, age, address, cpf, email = Functions.__clientInputs(True)
            if name != '':
                client.setName(name)
            if age != 0:
                client.setAge(int(age))
            if address != '':
                client.setAddress(address)
            if cpf != '':
                client.setCPF(cpf)
            if email != '':
                client.setEmail(email)
        else:
            print("Nenhum cliente registrado")

    @staticmethod
    def deleteClient():
        if os.path.exists('./database/client.json'):
            id = int(input('\nDigite o codigo do client que deseja apagar: '))
            with open("./database/client.json") as json_file:
                data = json.load(json_file)
                for i in range(len(data["list"])):
                    if data["list"][i]['id'] == id:
                        del data["list"][i]
                        break
                with open("./database/client.json", "w") as output_file:
                    json.dump(data,output_file)
        else:
            print("Nenhum client registrado")
    
    @staticmethod
    def showClient():
        if os.path.exists('./database/client.json'):
            with open("./database/client.json") as json_file:
                data = json.load(json_file)
                x = PrettyTable(["Codigo", "Nome"])
                x.align["Codigo"] = "l"
                x.align["Nome"] = "l"
                for client in data["list"]:
                    client = Client(client["id"])
                    x.add_row([client.getCode(), client.getName()]) 
                print(x)

                id = int(input('\nDigite o codigo do cliente que deseja visualizar: '))
                x = PrettyTable(["Codigo", "Nome", "Idade", "Endereço", "CPF", "E-mail"])
                x.align["Codigo"] = "l"
                x.align["Nome"] = "l"
                x.align["Idade"] = "l"
                x.align["Endereço"] = "l"
                x.align["CPF"] = "l"
                x.align["E-mail"] = "l"

                for client in data["list"]:
                    if client["id"] == id:
                        client = Client(client["id"])
                        x.add_row([client.getCode(), client.getName(), client.getAge(), client.getAddress(), client.getCPF(), client.getEmail()]) 
                os.system("cls")
                print(x)

        else:
            print("Nenhum funcionario registrado")

    @staticmethod
    def showAllClients():
        if os.path.exists('./database/client.json'):
            with open("./database/client.json") as json_file:
                data = json.load(json_file)
                x = PrettyTable(["Codigo", "Nome", "Idade", "Endereço", "CPF", "E-mail"])
                x.align["Codigo"] = "l"
                x.align["Nome"] = "l"
                x.align["Idade"] = "l"
                x.align["Endereço"] = "l"
                x.align["CPF"] = "l"
                x.align["E-mail"] = "l"

                for client in data["list"]:
                    client = Client(client["id"])
                    x.add_row([client.getCode(), client.getName(), client.getAge(), client.getAddress(), client.getCPF(), client.getEmail()]) 
                print(x)
        else:
            print("Nenhum funcionario registrado")

    @staticmethod
    def __clientInputs(edit = False):
        if edit:
            try:
                print()
                name = str(input("Insira o nome do client (caso não queira altera-lo deixe em branco): "))
                age = int(input("Insira a idade de seu client (caso não queira altera-lo digite 0): "))
                address = str(input("Insira o endereço de seu client (caso não queira altera-lo deixe em branco): "))
                cpf = str(input("Insira o cpf de seu cliente (caso não queira altera-lo deixe em branco): "))
                email = str(input("Insira o email de seu cliente (caso não queira altera-lo deixe em branco): ")) 

                return name, age, address, cpf, email
            except:
                print('\nDigitou algo errado')
                Functions.__employeeInputs(True)
        else:
            try:
                name = str(input("Insira o nome do cliente: "))
                age = int(input("Insira a idade de seu cliente: "))
                address = str(input("Insira o endereço de seu cliente: "))
                cpf = str(input("Insira o cpf de seu cliente: "))
                email = str(input("Insira o email de seu cliente: "))

                return name, age, address, cpf, email
            except:
                print('\nDigitou algo errado')
                __clientInputs()
    

    # FUNÇÕES DO MERCADO
    @staticmethod
    def getMarketInfo():
        if os.path.exists('./database/market.json'):
            with open("./database/market.json") as json_file:
                data = json.load(json_file)
                x = PrettyTable(["Nome", "Endereço", "CNPJ"])
                x.align["Nome"] = "l"
                x.align["Endereço"] = "l"
                x.align["CNPJ"] = "l"
                
                
                market = Market()
                x.add_row([market.getName(), market.getAddress(), market.getCNPJ()])
                print(x)
        else:
            print("Você ainda não registrou informações sobre o mercado")

    @staticmethod
    def editMarketInfo():
        name, address, cnpj = Functions.__marketInputs()
        if os.path.exists('./database/market.json'):
            with open("./database/market.json") as json_file:
                data = json.load(json_file)
                if name != '':
                    data["name"] = name
                if address != '':
                    data["address"] = address
                if cnpj != '':
                    data["cnpj"] = cnpj

                with open("./database/market.json", "w") as output_file:
                    json.dump(data,output_file)
        else:
            with open("./database/market.json", "w") as output_file:
                    json.dump(
                        {
                            "name": name,
                            "address": address,
                            "cnpj": cnpj
                        },
                        output_file
                    )
    
    @staticmethod
    def __marketInputs():
        try:
            print()
            name = str(input('Insira o nome do mercado (caso não queira altera-lo deixe em branco): '))
            address = str(input('Insira a descrição do mercado (caso não queira altera-lo deixe em branco): '))
            cnpj = str(input('Insira o cnpj do mercado (caso não queira altera-lo deixe em branco): '))

            return name, address, cnpj
        except:
            time.sleep(3)
            print('\nDigitou algo errado')
            Functions.__marketInputs()


    # FUNÇÕES DE VENDA
    @staticmethod
    def registerSale():
        os.system("cls")
        client, employee, products = Functions.__saleInputs()
        if os.path.exists('./database/sale.json'):
            with open("./database/sale.json") as json_file:
                data = json.load(json_file)
                data["id"] += 1
                data["list"].append({
                    "id": data["id"],
                    "client": client,
                    "employee": employee,
                    "products": products,
                    "created_at": strftime("%Y-%m-%d %H:%M:%S", gmtime())   
                })
                with open("./database/sale.json", "w") as output_file:
                    json.dump(data,output_file)
        else:
            with open("./database/sale.json", "w") as output_file:
                    json.dump(
                        {
                            "id": 1,
                            "list": [{
                                "id": 1,
                                "client": client,
                                "employee": employee,
                                "products": products,
                                "created_at": strftime("%Y-%m-%d %H:%M:%S", gmtime())   
                            }]
                        },
                        output_file
                    )
        with open("./database/product.json") as json_file:
            data = json.load(json_file)
            for prodInDB in data["list"]:
                for prod in products:
                    if prodInDB["id"] == prod["product"]:
                        prodInDB["quantity"] -= prod["quantity"]
            with open("./database/product.json", "w") as output_file:
                    json.dump(data,output_file)

        print('Venda registrado com sucesso')
        os.system("cls")

    @staticmethod
    def __saleInputs():
        try:
            client = int(input("Digite o codigo do cliente que fez a compra: "))
            employee = int(input("Digite o codigo do Funcionario que fez a venda: "))
            products = []
            continuar = 's'
            while continuar in 'sS' or len(products) == 0:
                products.append({
                    "product": int(input('O codigo do produto vendido: ')),
                    "quantity": int(input('A quantidade dele: '))
                })
                continuar = str(input('Deseja inserir mais um produto na compra? [S/N]'))

            return client, employee, products
        except:
            print('\nDigitou algo errado')
            Functions.__saleInputs(True)

    @staticmethod
    def showSale():
        if os.path.exists('./database/sale.json'):
            with open("./database/sale.json") as json_file:
                data = json.load(json_file)
                x = PrettyTable(["Codigo", "Produtos"])
                x.align["Codigo"] = "l"
                x.align["Produtos"] = "l"
                
                for sale in data["list"]:
                    sale = Sale(sale["id"])
                    products = ""
                    try:
                        i = 0
                        for product in sale.getProducts():
                            if i == 0:
                                products += product.getName()
                            else:
                                products += ", " + product.getName()
                            i += 1
                        x.add_row([sale.getCode(), products])
                    except Exception as e:
                        print (e)
                        time.sleep(2)
                print(x)

                id = int(input('\nDigite o codigo do venda que deseja visualizar: '))
                x = PrettyTable(["Codigo", "Cliente", "Funcionario", "Produtos", "Preço da Venda"])
                x.align["Codigo"] = "l"
                x.align["Cliente"] = "l"
                x.align["Funcionario"] = "l"
                x.align["Produtos"] = "l"
                x.align["Preço da Venda"] = "l"
                
                for sale in data["list"]:
                    if sale["id"] == id:
                        sale = Sale(sale["id"])
                        products = ""
                        try:
                            i = 0
                            for product in sale.getProducts():
                                if i == 0:
                                    products += product.getName()
                                else:
                                    products += ", " + product.getName()
                                i += 1
                            x.add_row([sale.getCode(), sale.getClient().getName(), sale.getEmployee().getName(), products, "R$" + str(sale.getTotal())])
                        except Exception as e:
                            print (e)
                            time.sleep(2)
                os.system("cls")
                print(x)
        else:
            print("Nenhuma venda registrado")

    @staticmethod
    def showAllSales():
        if os.path.exists('./database/sale.json'):
            with open("./database/sale.json") as json_file:
                data = json.load(json_file)
                x = PrettyTable(["Codigo", "Cliente", "Funcionario", "Produtos", "Preço da Venda"])
                x.align["Codigo"] = "l"
                x.align["Cliente"] = "l"
                x.align["Funcionario"] = "l"
                x.align["Produtos"] = "l"
                x.align["Preço da Venda"] = "l"
                
                for sale in data["list"]:
                    sale = Sale(sale["id"])
                    products = ""
                    try:
                        i = 0
                        for product in sale.getProducts():
                            if i == 0:
                                products += product.getName()
                            else:
                                products += ", " + product.getName()
                            i += 1
                        x.add_row([sale.getCode(), sale.getClient().getName(), sale.getEmployee().getName(), products, "R$" + str(sale.getTotal())])
                    except Exception as e:
                        print (e)
                        time.sleep(2)
                print(x)
        else:
            print("Nenhuma venda registrado")


    # FUNÇÕES DE PRODUTO
    @staticmethod
    def registerProduct():
        os.system("cls")
        name, price, description, quantity = Functions.__productInputs() 
        if os.path.exists('./database/product.json'):
            with open("./database/product.json") as json_file:
                data = json.load(json_file)
                data["id"] += 1
                data["list"].append({
                    "id": data["id"],
                    "name": name,
                    "price": price,
                    "description": description,
                    "quantity": quantity,
                })
                with open("./database/product.json", "w") as output_file:
                    json.dump(data,output_file)
        else:
            with open("./database/product.json", "w") as output_file:
                json.dump(
                    {
                        "id": 1,
                        "list": [{
                            "id": 1,
                            "name": name,
                            "price": price,
                            "description": description,
                            "quantity": quantity,
                        }]
                    },
                    output_file
                )

    @staticmethod
    def editProduct():
        if os.path.exists('./database/product.json'):
            id = int(input("\nDigite o codigo do produto que quer editar: "))
            product = Product(id)
            name, price, description, quantity = Functions.__productInputs(True) 
            if name != '':
                product.setName(name)
            if price != 0:
                product.setPrice(price)
            if description != '':
                product.setDescription(description)
            if price != 0:
                product.setQuantity(quantity)
        else:
            print('Nenhum produto registrado')

    @staticmethod
    def deleteProduct():
        if os.path.exists('./database/product.json'):
            id = int(input('\nDigite o codigo do produto que deseja apagar: '))
            with open("./database/product.json") as json_file:
                data = json.load(json_file)
                for i in range(len(data["list"])):
                    if data["list"][i]['id'] == id:
                        del data["list"][i]
                        break
                with open("./database/product.json", "w") as output_file:
                    json.dump(data, output_file)
        else:
            print("Nenhum produto registrado")

    @staticmethod
    def showProduct():
        if os.path.exists('./database/product.json'):
            with open("./database/product.json") as json_file:
                data = json.load(json_file)
                x = PrettyTable(["Codigo", "Nome"])
                x.align["Codigo"] = "l"
                x.align["Nome"] = "l"
                for product in data["list"]:
                    product = Product(product["id"])
                    x.add_row([product.getCode(), product.getName()]) 
                print(x)
                
                id = int(input('\nDigite o codigo do produto que deseja visualizar: '))
                x = PrettyTable(["Codigo", "Nome", "Preço", "Descriçao", "Quantidade"])
                x.align["Codigo"] = "l"
                x.align["Nome"] = "l"
                x.align["Preço"] = "l"
                x.align["Descriçao"] = "l"
                x.align["Quantidade"] = "l"

                for product in data["list"]:
                    if product["id"] == id:    
                        product = Product(product["id"])
                        x.add_row([product.getCode(), product.getName(), "R$" + str(product.getPrice()), product.getDescription(), product.getQuantity()]) 
                os.system("cls")
                print(x)
        else:
            print("Nenhum produto registrado")

    @staticmethod
    def showAllProducts():
        if os.path.exists('./database/product.json'):
            with open("./database/product.json") as json_file:
                data = json.load(json_file)
                x = PrettyTable(["Codigo", "Nome", "Preço", "Descriçao", "Quantidade"])
                x.align["Codigo"] = "l"
                x.align["Nome"] = "l"
                x.align["Preço"] = "l"
                x.align["Descriçao"] = "l"
                x.align["Quantidade"] = "l"

                for product in data["list"]:
                    product = Product(product["id"])
                    x.add_row([product.getCode(), product.getName(), "R$" + str(product.getPrice()), product.getDescription(), product.getQuantity()]) 
                print(x)
        else:
            print("Nenhum produto registrado")

    @staticmethod
    def __productInputs(edit = False):
        if edit:
            try:
                print()
                name = str(input('Insira o nome do produto (caso não queira altera-lo deixe em branco): '))
                description = str(input('Insira a descrição do produto (caso não queira altera-lo deixe em branco): '))
                price = float(input('Insira o valor do produto (caso não queira altera-lo digite 0): '))
                quantity = int(input('Insira a quantidade do produto (caso não queira altera-lo digite 0): '))
                
                return name, price, description, quantity
            except:
                print('\nDigitou algo errado')
                Functions.__employeeInputs(True)
        else:
            try:
                name = str(input('Insira o nome do produto: '))
                description = str(input('Insira a descrição do produto: '))
                price = float(input('Insira o valor do produto: '))
                quantity = int(input('Insira a quantidade do produto: '))

                return name, price, description, quantity
            except:
                time.sleep(3)
                print('\nDigitou algo errado')
                Functions.__productInputs()
