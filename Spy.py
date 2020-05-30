# github repository- Lavanya-B

def spy(x):
    sum,prod=0,1
    for i in str(x):
        sum+=int(i)
        prod*=int(i)
    return prod==sum
y=input("Enter a number:\n")
if spy(y):
    print(y,"is a spy number.")
else:
    print(y,"is not a spy number.")