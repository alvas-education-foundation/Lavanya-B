# github repository- Lavanya-B

n =int(input())
base = int(input())
s=""
while n>0:
  s= str(n%base) + s
  n=n//base
print(s)