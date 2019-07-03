a1 = int(input())
b2 = list(map(int,input().split()))
d3 = []
for i in b2:
  c4 = bin(i)
  d3.append(c4)
e5 = sorted(d3)
e5.reverse()
for i in e5:
  print(int(i,2))
