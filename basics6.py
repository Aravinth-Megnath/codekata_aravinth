a = int(input())


class basics6():
  def __init__(self,a):
    self.a = a
    self.factors = []
    self.sqrt = int(a**0.5)
  def composite(self):
    for i in range(1,self.sqrt+1):
      if a%i==0:
        self.factors.append(i)
        if i != a //i:
          self.factors.append(a//i)
  def check(self):
    if len(self.factors) >2:
      print('yes')
    else:
      print('no')
obj = basics6(a)
obj.composite()
obj.check()
