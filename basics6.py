a = int(input())

factors = []
sqrt = int(a**0.5)
class basics6():
  def __init__(self,a):
    self.a = a
  def composite(self):
    for i in range(1,sqrt+1):
      if a%i==0:
        factors.append(i)
        if i != a //i:
          factors.append(a//i)
  def check(self):
    if len(factors) >2:
      print('yes')
    else:
      print('no')
obj = basics6(a)
obj.composite()
obj.check()
