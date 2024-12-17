a = list(map(int,(input().split())))
prime_no = []
class basics5():
  def __init__(self,a):
    self.a = a
  def prime (n):
    if n<=0:
      return False
    for i in range(2,n):
      if n%i==0:
        return False
    return True
  for i in range(a[0],a[1]+1):
    if prime(i):
      prime_no.append(i)

    else:
      continue

obj = basics5(a)
print(len(prime_no))
    
