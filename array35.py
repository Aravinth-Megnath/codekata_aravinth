class array35():
  def __init__(self,sentence,string):
    self.sentence = sentence
    self.string = string

  def check(self):
    sentence = self.sentence.split()
    count = 0
    for word in sentence:
      if word == self.string:
        count +=1
      else:
        continue
    if count == 0:
      print(-1)
    else:
      print(count)

obj = array35(input(),input())
obj.check()
