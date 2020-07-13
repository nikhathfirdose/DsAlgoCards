class Employee:
  def __init__(self, name):
    self.name = name
    print(f'{self.name} is an employee')

class Manager(Employee):
  def __init__(self, department, name):
    self.department = department
    self.name = name
    # super().__init__(name)
    # print(super())
    print(f'Manager, {self.department} department')

staff_1 = Manager('HR', 'Andy')
print(dir(staff_1))
class Developer:
  def __init__(self, name, language):
    self.name = name
    self.language = language

  def introduce(self):
    print(f'Hi! I am {self.name}. I code in {self.language}')

dev = Developer('Matt', 'Python')

print(dir(dev))
