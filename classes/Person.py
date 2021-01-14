import json

class Person:
    def __init__(self, id, name, age, address, type):
        self.id = id
        self.name = name
        self.age = age
        self.address = address
        self.type = type
        if type == 'employee':
            self.path = "./database/employee.json"
        if type == 'client':
            self.path = "./database/client.json"

    def setName(self, name):
        data = self.__getList()
        for employee in data["list"]:
            if employee["id"] == self.id:
                employee["name"] = name
        self.__saveList(data)
    def setAge(self, age):
        data = self.__getList()
        for employee in data["list"]:
            if employee["id"] == self.id:
                employee["age"] = age
        self.__saveList(data)
    def setAddress(self, address):
        data = self.__getList()
        for employee in data["list"]:
            if employee["id"] == self.id:
                employee["address"] = address

    def getCode(self):
        return self.id
    def getName(self):
        return self.name
    def getAge(self):
        return self.age
    def getAddress(self):
        return self.address

    
    def __getList(self):
        with open(self.path) as json_file:
            data = json.load(json_file)
            return data

    def __saveList(self, data):
        with open(self.path, "w") as output_file:
                json.dump(data,output_file)
