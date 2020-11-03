class Employee():
    __name = 'Employee'
    __salary = 0.0
    __bonus = 110.0

    def __init__(self, name: str, salary: float, bonus: float):
        self.__name = name
        self.__salary = salary
        self.__bonus = bonus

    @property
    def name(self):
        return "the name is  %s " % (self.__name)

    @property
    def salary(self):
        return "the salary is  %s " % (self.__salary)

    @salary.setter
    def salary(self, salary):
        self.__salary = int(salary)

    @property
    def set_bonus(self):
        return "the bonus is  %s " % (self.__bonus)

    def to_pay(self):
        total = self.__bonus + self.__salary
        return "the total is  %s " % (total)


class SalesPerson(Employee):
    __percent = 150

    def __init(self, name, salary, percent):
        self.__name = name
        self.__salary = salary
        self.__percent = percent

    def set_bonus(self, bonus=110.0):
        if self.__percent > 200:
            self.__bonus = 3 * bonus
        elif self.__percent > 100:
            self.__bonus = 2 * bonus
        else:
            self.__bonus = bonus
        return "the bonus is  %s " % (self.__bonus)


class Manager(Employee):
    __quantity = 0

    def __init__(self, name, salary, amount=__quantity):
        self.__quantity = int(amount)
        Employee.__init__(self, name, salary)
