# Decorators
class Calculator:
  def __init__(self,type):
    self.type = type
  def sums(*args):
    return args
  @classmethod
  def calculate_sum(cls, *args): 
        return args
    # cls is just like self which needs to passed as 1st parameter
  @staticmethod
  def calculate_sums( num1, num2): 
        return num1 + num2

print(Calculator.calculate_sum(3,5,"op")) # 
print(type(Calculator.calculate_sum(3,6)))

print(Calculator.calculate_sums(3,15)) # 
print(type(Calculator.calculate_sums(3,6)))

print(Calculator.sums(3,15)) # 
print(type(Calculator.sums(3,6)))

# Inheeritance
class Player:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def run(self):
    return f'{self.name} is running'

class Cricketer(Player): # Syntax to inherit a class
  def catch_ball(self):
    return f'{self.name} Caught the ball'

class Batsman(Cricketer):
  def swing_bat(self):
    return f'what a shot by {self.name}'

player1 = Batsman('Virat Kohli', 31)

print(player1.run())
print(player1.catch_ball())
print(player1.swing_bat())