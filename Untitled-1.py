
class Employee:

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.'+ last + '@company.com'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)


emp_1 = Employee('Daniel', 'Fabi', 70000)
emp_2 = Employee('Peter', 'Fabi', 90000)



print(emp_1.fullname())
