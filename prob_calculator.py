import copy
import random
# Consider using the modules imported above.

class Hat:
  def __init__(self, **ball_list):
    self.contents = list()
    for key, value in ball_list.items():
      for x in range(value):
        self.contents.append(key)
    
  def draw(self, draws):
    if draws > len(self.contents):
      return self.contents
    drawn_balls = list()
    for x in range(draws):
      random_ball = random.choice(self.contents)
      drawn_balls.append(random_ball)
      self.contents.remove(random_ball)
    return drawn_balls
    
def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  good_outcome = 0
  for x in range(num_experiments):
    disposable_hat = copy.deepcopy(hat)
    drawn = disposable_hat.draw(num_balls_drawn)
    broke = False
    for key,value in expected_balls.items():
      count = 0
      for x in drawn:
          if x == key:
              count += 1
      if value > count:
        broke = True
        break
    if not broke:
      good_outcome += 1
  return good_outcome/num_experiments