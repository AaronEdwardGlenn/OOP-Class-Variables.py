# let's review class variables
# while insance variables can be different for each instance of this class. class variables are the same among all instances.

# we are going to do a pay raise for each employee as a class variable. the ammount can change, but it will be the same for every person in this class.


class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def fullname(self):
        return('{}, {}'.format(self.first, self.last))

# here is our class variable hard coded:
    def apply_raise(self):
        self.pay = int(self.pay * 1.04)


emp_1 = Employee('Aaron', 'Glenn', 100)
emp_2 = Employee('Test', 'User', 200)

print(emp_1.pay)
emp_1.apply_raise()
print(emp_1.pay)

# Employee.raise_amount
# emp_1.raise_amount
