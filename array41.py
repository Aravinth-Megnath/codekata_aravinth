
class array41:
  def __init__(self,N,a):
    self.N = int(N)
    self.a = list(map(int,a.split()))
  def check(self):
    result =[]
    b = sorted(self.a,reverse = True)
    a_index_map = {val :[] for val in self.a}
    for index, val in enumerate(self.a):
      a_index_map[val].append(index)

    for j in b:
      result.append(a_index_map[j].pop(0))

    print(*result)
obj = array41(input(),input())
obj.check()
                                                 
