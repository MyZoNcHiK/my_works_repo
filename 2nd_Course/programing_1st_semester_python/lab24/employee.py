class Employee:
    def __init__(self, name):
        self.name = name

    def work(self):
        return "Working"


class Manager(Employee):
    def manage(self):
        return "Managing team"


class Programmer(Employee):
    def code(self):
        return "Writing code"


class TechLead(Manager, Programmer):
    def work(self):
        return f"{self.manage()} and {self.code()}"


tech_lead = TechLead("Олександр")

print("Ім'я:", tech_lead.name)
print("Work:", tech_lead.work())
print("Manage:", tech_lead.manage())
print("Code:", tech_lead.code())

manager = Manager("Марія")
print("Ім'я:", manager.name)
print("Work:", manager.work())
print("Manage:", manager.manage())

programmer = Programmer("Андрій")
print("Ім'я:", programmer.name)
print("Work:", programmer.work())
print("Code:", programmer.code())

print("\nMRO класу TechLead:")
print(TechLead.__mro__)

