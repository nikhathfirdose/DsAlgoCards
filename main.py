# The task is to create a class SoccerPlayer with name and goals attributes, then create 3 player objects and then using a function find out the maximum goals and print that.

# class  SoccerPlayer:
#   def __init__(self, name, goals):
#     self.name = name
#     self.goals = goals
# def CalculateMaxGoals(self, *args):
#   print(args)
#   return max(*args)

# p1= SoccerPlayer("a",100)
# p2= SoccerPlayer("b",12)
# p3=SoccerPlayer("c", 23)
# print(p1.goals)
# max_goals = CalculateMaxGoals(p1.goals, p2.goals,p3.goals)
# print(f'max goals are {max_goals}')
class SoccerPlayer:
  def __init__(self, name, goals):
    self.name = name
    self.goals = goals


def calculateMaxGoals(*args):
  print(args)
  return max(*args)

messi = SoccerPlayer('messi', 10)
ronaldo = SoccerPlayer('ronaldo',22)
neymar = SoccerPlayer('neymar', 8)

max_goals = calculateMaxGoals(messi.goals, ronaldo.goals, neymar.goals)
print(f'The highest number of goals is {max_goals} goals')
