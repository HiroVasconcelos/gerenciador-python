from .Person import Person

import os
import time
import json
import datetime

class Client(Person):
    def __init__(self, id):
        with open("./database/client.json") as json_file:
            data = json.load(json_file)
            for client in data["list"]:
                if client["id"] == id:
                    super().__init__(id, client["name"], client["age"], client["address"], 'client')
                    self.cpf = client["cpf"]
                    self.email = client["email"]
                    self.created_at = client["created_at"]
                    break

    def setCPF(self, cpf):
        data = self.__getList()
        for employee in data["list"]:
            if employee["id"] == self.id:
                employee["cpf"] = cpf
    def setEmail (self, email):
        data = self.__getList()
        for employee in data["list"]:
            if employee["id"] == self.id:
                employee["email"] = email

    def getCPF(self):
        return self.cpf
    def getEmail(self):
        return self.email
    def getCreatedAt(self):
        return self.created_at
    def getSales(self):
        from .Sale import Sale
        sales = []
        with open("./database/sale.json") as json_file:
            data = json.load(json_file)
            for sale in data["list"]:
                if sale["client"] == self.id:
                    sales.append(Sale(sale["id"]))
        return sales