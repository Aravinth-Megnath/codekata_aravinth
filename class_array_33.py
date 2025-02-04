class array33():
  def __init__(self,N,a):
    self.N = N
    self.a = a

  def check(self):
    try:
      self.N = int(self.N)
    except:
      print('Please enter Integer')
      return
    try:
      self.a = list(map(int,self.a.split()))
    except:
      print('Please enter Integer')
      return
      
  def find_lowest(self):
    lowest = self.a[0]
    for i in range(self.N):
      if self.a[i]<lowest:
        lowest = self.a[i]
      else:
        continue
    print(lowest)

obj = array33(input(),input())
obj.check()
obj.find_lowest()
  
