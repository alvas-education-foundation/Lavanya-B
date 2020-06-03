# Github repository- Lavanya-B

a = input()
sum = 0
for i in range(len(a)):
  n = int(a[i])**3
  sum +=n
if int(a)==sum:
  print ("Armstrong Number")
else :
  print ("Not Armstrong Number")