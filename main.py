class Developer:
  def __init__(self, name, language):
    self.name = name
    self.language = language

  def introduce(self, age):
    print(f'Hi! I am {self.name}. I code in {self.language} ans aged {age}')

dev = Developer('Matt', 'Python')
# print(dev.introduce(4))
# print(dir(dev))

class Employee:
  secret_code = 'secret'

class Manager(Employee):
  secret_code = 'm123'

class Accountant(Employee):
  secret_code = 'a123'

class Owner(Employee):
  pass

person = Owner()
# print(person.secret_code)
# print(Owner.mro()) 

from functools import reduce

numbers = [1,2,3,4]
def accumulat(acc, curr):
  return acc * curr

sum = reduce(accumulat, numbers, 1)
print(sum) # 10
print(int(pow(2,63)-1))
print(int(0xa5))
print('foo\\bar\nbaz')
print('a' + 'x' if '123'.isdigit() else 'y' + 'b')


names = ['John', 'Peter', 'Elon', 'Joseph']

# make all names upper cased
uppercased = list(map(lambda name: str.capitalize(name), names))

users = [('Mary', 23), ('Emilie', 10), ('Katie', 30)]

sorted_by_name = sorted(users)
print(sorted_by_name) 
# [('Emilie', 10), ('Katie', 30), ('Mary', 23)]

sorted_by_age = sorted(users, key = lambda item: item[0]) 
# using age as key for sorting 

print(sorted_by_age)
# From a list of names, filter out the duplicate names and store in a list.
names = [
    'Harry', 'Johnny', 'Lewis', 'Harry', 'Buck', 'Nick', 'David', 'Harry',
    'Lewis', 'Michael'
]


dup = {name for name in names if names.count(name)>1}
print(list(dup))


def logger(func, args):  # higher order function
    print(f'The result of the passed function is {func(*args)}')


def sum(num1, num2):
    return num1 + num2


logger(sum, (1, 5))

def random(): # Higher order function

  return special
def special():
  return "ppp"


random_value = random()
random_value() # I am something special
# One line way
print(random()())


def starmaker(func):
  '''
  A decorator function which accepts a function
  and then wraps some goodness into it and
  returns it back!
  '''
  def wrapper():
    func()
    print('You are a star now!')
    print('*********')
  return wrapper

# @starmaker
def layman():
  print('I am just a layman')

# print(starmaker(layman()))


test_user = {
    'name': 'Jackson',
    'valid': True
}

another_user = {
  'name': 'Nathan',
  'valid': False
}

def authenticated(fn):
  def wrapper(args):
    if args['valid']:
      fn(args)
  return wrapper

@authenticated
def message_friends(user):
    print('message has been sent')

message_friends(test_user) # message has been sent
message_friends(another_user) # (Does nothin