class Person:
    def __init__(self,name, occupation):
        print("Hey  i am person ")
        self.name = name
        self.occupation = occupation
    def info(self):
        print(f"{self.name} is a {self.occupation}")

a = Person("Soham", "Student")
b = Person("Venom", "Esports Athlete")

a.info()
b.info()
class NoxiousSurge:
    def __init__(self, name,role):
        self.name = name
        self.role = role
        
    def showdetails(self):
            print(f"{self.name} is a {self.role} playing for Noxious Surge ")

P1 = NoxiousSurge("VenomOP", "freeman")
P1.showdetails()