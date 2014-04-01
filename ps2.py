#!/usr/bin/env python
'''Problem set 2.'''
#Problem1
nA = 6
nB = 9
nC = 20
m = {}

def d_equation(num_nug):
  assert num_nug >= 6
  for c in range (0, num_nug):
    for b in range (0, num_nug):
      for a in range (0, num_nug):
        if nA*a + nB*b + nC*c == num_nug:
          m[num_nug] = (a, b, c)
          return True 
  #print ("no answer")
  return False 

def findLgst():
  ctr = 0
  num = nA
  lgstNum = 0
  while ctr < nA:
    if d_equation(num):
      ctr += 1
    else:
      ctr = 0
      lgstNum = num
    num += 1

  return lgstNum

num_ngts = input("enter a #: ")
ans = d_equation(num_ngts)
#ans = findLgst()
print (ans)
keys = m.keys()
values = m.values()
for i in range(len(keys)):
  print("%d*6+%d*9+%d*20=%d"%(values[i][0],values[i][1],values[i][2],keys[i]))
