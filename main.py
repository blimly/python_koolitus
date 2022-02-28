

def add(a, b):
    return a + b


class Employee:
    def __init__(self, name, address, salary):
        self.name = name
        self.address = address
        self.salary = salary


if __name__ == '__main__':
    # Function
    c = add(2, 2)
    print(c)

    # Class / object
    employee1 = Employee("John", "Tallinn", 500)  # employee1 is an object of class Employee
    print(employee1.address)
    employee1.address = "Tartu"
    print(employee1.address)
