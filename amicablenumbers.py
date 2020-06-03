# Github repository- Lavanya-B


A=int(input("A="))
B=int(input("B="))
c=0
d=0
for k in range(1,A):
    if(A%k==0):
      c+=k
for i in range(1,B):
    if(B%i==0):
      d+=i
if(B==c and A==d):
  print(A,"and",B,"are amicable")
else:
  print(A,"and",B,"are not amicable")