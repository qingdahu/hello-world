class Employee:

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@live.ca'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * 1.04)


emp_1 = Employee('Yun', 'Pan', 50000)
emp_2 = Employee('user', 'name', 60000)

print (emp_1.pay)
emp_1.apply_raise()
print (emp_1.pay)

print (emp_1.fullname())

#print (emp_1)
#print (emp_2)
#emp_1.first = 'Yun'
#emp_1.last = 'Pan'
#emp_1.email = 'yun.pan@live.ca'
