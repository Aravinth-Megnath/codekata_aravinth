a = list(map(int, (input().split())))
class basics3():
  def __init__(self,a):
    self.a = a
  def square(self):
    product = a[0] * a[1]
    square = product ** 0.5
    if product == int(square * square):
      print('yes')
    else:
      print('no')

obj = basics3(a)
obj.square()
