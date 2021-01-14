import os
import time
import json

from .Product import Product

class Sale:
    def __init__(self, id):
        self.id = id
        with open("./database/sale.json") as json_file:
            data = json.load(json_file)
            for sale in data["list"]:
                if sale["id"] == id:
                    self.client = sale["client"]
                    self.employee = sale["employee"]
                    self.products = sale["products"]
                    self.created_at = sale["created_at"]
                    break

    def getClient(self):
        from .Client import Client
        return Client(self.client)
    def getEmployee(self):
        from .Employee import Employee
        return Employee(self.employee)
    def getProducts(self):
        from .Product import Product
        products = []
        for product in self.products:
            products.append(Product(product['product']))
        return products
    def getTotal(self):
        value = 0
        for product in self.products:
            value += Product(product['product']).getPrice() * product['quantity']
        return value
    def getSaleInfo(self):
        return self.created_at
    def getCode(self):
        return self.id