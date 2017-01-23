class Do:
  def __init__(self, function):
    self.function = function

  def times(self, num):
    for _ in range(num):
      self.function()
