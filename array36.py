class array34():
  def __init__(self,N,year,parties):
    self.N = int(N)
    self.year = list(map(int,(year).split()))
    self.parties = (parties).split()

  def check(self):
    change_in_win = []
    sorted_year = dict(sorted(zip(self.year,self.parties)))
    keys = list(sorted_year.keys())
    for i in range(len(keys)-1):
      if sorted_year[keys[i]] != sorted_year[keys[i+1]]:
        change_in_win.append(keys[i+1])
      else:
        continue
    for i in change_in_win:
      print(i)

obj = array34(input(),input(),input())
obj.check()
