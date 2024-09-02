class Employee:
    def __init__(self, salary):
        self.salary = salary

    def __add__(self, other):
        return self.salary + other.salary

    def __mul__(self, other):
        return self.salary * other.salary

    # def __suv__(self, other)
    # div
    # mod

if __name__ == '__main__':
    emp1 = Employee(100)
    emp2 = Employee(200)
    print(emp1 + emp2)
    print(emp1 * emp2)