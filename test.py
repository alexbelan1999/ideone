class Worker:
    def __init__(self, name: str, salary: float):
        self.name = name
        self.salary = salary

    def profit(self, k: float):
        self.salary = self.salary * k


class Manager(Worker):
    def __init__(self, name: str, salary: float, sales: float):
        super().__init__(name, salary)
        self.sales = sales

    def profit(self, H: float):
        if self.sales > H:
            self.salary = self.salary + H / 100.0


class Engineer(Worker):
    def __init__(self, name: str, salary: float, project: int):
        super().__init__(name, salary)
        self.project = project

    def profit(self):
        self.salary = self.salary + 4.8 * self.project


worker1 = Worker('Bob', 500)
print("Имя: ", worker1.name, " доход: ", worker1.salary)
worker1.profit(1.1)
print("Имя: ", worker1.name, " доход: ", worker1.salary)

manager1 = Manager('Tom', 600, 5.5)
print("Имя: ", manager1.name, " доход: ", manager1.salary, " продажи: ", manager1.sales)
manager1.profit(6.0)
print("Имя: ", manager1.name, " доход: ", manager1.salary, " продажи: ", manager1.sales)
manager1.profit(5.0)
print("Имя: ", manager1.name, " доход: ", manager1.salary, " продажи: ", manager1.sales)

engineer1 = Engineer('Bill', 700, 3)
print("Имя: ", engineer1.name, " доход: ", engineer1.salary, " проекты: ", engineer1.project)
engineer1.profit()
print("Имя: ", engineer1.name, " доход: ", engineer1.salary, " проекты: ", engineer1.project)
