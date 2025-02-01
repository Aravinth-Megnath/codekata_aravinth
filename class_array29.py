import sys
class array29():
  
  def __init__(self,a,b):
    self.a = a
    self.b = b

  def check(self):
    try:
      self.a = int(self.a)
    except ValueError:
      print('Please enter Integer')
      sys.exit()
      
    try:
      self.b = list(map(int,self.b.split()))
    except ValueError:
      print('Please enter Integer')
      sys.exit()

  def rearranging(self):
    final = []
    for i in self.b:
     # c = self.b[i]
      final.append(self.b[i])
    print(*final)
  
obj = array29(input(),input())
obj.check()
obj.rearranging()
