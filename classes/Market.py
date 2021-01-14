import os
import time
import json

class Market:
    def _init_(self):
        self.path = "./database/market.json"

    def setName(self, name):
        data = self.__getList()
        data["name"] = name
        self.__saveList(data)

    def setAddress(self, address):
        data = self.__getList()
        data["address"] = address
        self.__saveList(data)

    def setCNPJ(self, cnpj):
        data = self.__getList()
        data["cnpj"] = cnpj
        self.__saveList(data)


    def getName(self):
        data = self.__getList()
        return data["name"]

    def getAddress(self):
        data = self.__getList()
        return data["address"]

    def getCNPJ(self):
        data = self.__getList()
        return data["cnpj"]

    def getRevenue(self):
        from .Sale import Sale
        total = 0
        with open('./database/sale.json') as json_file:
            data = json.load(json_file)
            for sale in data["list"]:
                sale = Sale(sale["id"])
                total += sale.getTotal()

        return total

    def getStorage(self):
        from .Product import Product
        products = []
        with open('./database/product.json') as json_file:
            data = json.load(json_file)
            for product in data["list"]:
                products.append(Product(product["id"]))

        return products

    def getEmployees(self):
        from .Employee import Employee
        employees = []
        with open('./database/product.json') as json_file:
            data = json.load(json_file)
            for employee in data["list"]:
                employees.append(Employee(employee["id"]))

        return employees

    def __getList(self):
        with open("./database/market.json") as json_file:
            data = json.load(json_file)
            return data

    def __saveList(self, data):
        with open("./database/market.json", "w") as output_file:
                json.dump(data,output_file)