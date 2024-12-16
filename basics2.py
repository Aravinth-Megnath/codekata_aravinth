a = int(input())
b = list(map(int, (input().split())))
class basics2():
  def __init__(self,a,b):
    self.a = a
    self.b = b
  def between(self):

    if a>b[0] and a<b[1]:
      print('YES')
    else:
      print('NO')
obj = basics2(a,b)
obj.between()
