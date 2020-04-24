# let's review class variables
# while insance variables can be different for each instance of this class. class variables are the same among all instances.

# we are going to do a pay raise for each employee as a class variable. the ammount can change, but it will be the same for every person in this class.


class Employee:
    # lets incriment a number of employees each time a new initialization of the class occours (this is our __init__)
    raise_amount = 1.04
    num_of_emps = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

        Employee.num_of_emps += 1

    def fullname(self):
        return('{}, {}'.format(self.first, self.last))

# here is our class variable hard coded:
    def apply_raise(self):
        # NOTE we can not just add raise_amount here. we need to demonstrate that it is part of the class by prefixing it with Employee. or putting self. to note that it is part of an instance of that class.
        self.pay = int(self.pay * Employee.raise_amount)


emp_1 = Employee('Aaron', 'Glenn', 100)
emp_2 = Employee('Test', 'User', 200)

print(emp_1.pay)
emp_1.apply_raise()
print(emp_1.pay)

print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)

# when we try to access an attribute on an instance like on lines 34 and 35, it first checks to see if it exists for that instance, it not, it will then check the class, and then for any classes being inhereted. HEre, when we do the instance of emp_1 and access raise_amount. it do not access it on that instance, but rather on the class itself, as seen on line 33.

# this shows us all the attributes of this instance of the Employee class. NOTE that raise_amount doesnt exist here.
print(emp_1.__dict__)

print(Employee.__dict__)    # NOTE that raise_amount does exist here.

# if we add emp_1.raise_amount = 1.05, it will only change it for that instance becuase it is seached first before the class attribute. NOTE this only works because we did self.raise_amount in the apply_raise method and not Employee.raise_amount.

print(Employee.num_of_emps)
