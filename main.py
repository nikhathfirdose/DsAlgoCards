# Polymorphism

class ProgLanguage:
  def __init__(self, name):
    self.name = name

class JavaScript(ProgLanguage):
  def comment(self):
    print(f'// is a comment in {self.name}')

class Python(ProgLanguage):
  def comment(self):
    print(f'# is a comment in {self.name}')


obj1 = JavaScript("JavaScript")
obj2= Python("Python")

for i in [obj1,obj2]:
  i.comment()

obj1.comment()
obj2.comment()