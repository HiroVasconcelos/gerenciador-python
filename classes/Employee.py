from .Person import Person
import os
import json

class Employee(Person):
    def __init__(self, id):
        with open("./database/employee.json") as json_file:
            data = json.load(json_file)
            for employee in data["list"]:
                if employee["id"] == id:
                    super().__init__(id, employee["name"], employee["age"], employee["address"], 'employee')
                    self.salary = employee["salary"]
                    self.created_at = employee["created_at"]
                    break

    def setSalary(self, salary):
        data = self._Person__getList()
        for employee in data["list"]:
            if employee["id"] == self.id:
                employee["salary"] = salary
        self._Person__saveList(data)

    def getSalary(self):
        return self.salary
    def getCreatedAt(self):
        return self.created_at

    def getSales(self):
        from .Sale import Sale
        sales = []
        with open("./database/sale.json") as json_file:
            data = json.load(json_file)
            for sale in data["list"]:
                if sale["employee"] == self.id:
                    sales.append(Sale(sale["id"]))
        return sales
