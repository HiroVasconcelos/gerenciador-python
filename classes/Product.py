import os
import time
import json

class Product:
    def __init__(self, id):
        self.id = id    
        with open("./database/product.json") as json_file:
            data = json.load(json_file)
            for product in data["list"]:
                if product["id"] == id:
                    self.name = product["name"]
                    self.price = product["price"]
                    self.description = product["description"]
                    self.quantity = product["quantity"]
                    break

    def setName(self, name):
        data = self.__getList()
        for product in data["list"]:
            if product["id"] == self.id:
                product["name"] = name
        self.__saveList(data)

    def setPrice(self, price):
        data = self.__getList()
        for product in data["list"]:
            if product["id"] == self.id:
                product["price"] = price
        self.__saveList(data)

    def setDescription(self, description):
        data = self.__getList()
        for product in data["list"]:
            if product["id"] == self.id:
                product["description"] = description
        self.__saveList(data)

    def setQuantity(self, quantity):
        data = self.__getList()
        for product in data["list"]:
            if product["id"] == self.id:
                product["quantity"] = quantity
        self.__saveList(data)

    def getCode(self):
        return self.id

    def getName(self):
        return self.name

    def getPrice(self):
        return self.price

    def getDescription(self):
        return self.description

    def getQuantity(self):
        return self.quantity

    def __getList(self):
        with open("./database/product.json") as json_file:
            data = json.load(json_file)
            return data

    def __saveList(self, data):
        with open("./database/product.json", "w") as output_file:
                json.dump(data,output_file)

    