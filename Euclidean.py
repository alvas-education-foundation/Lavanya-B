# github repository- Lavanya-B

a = int(input())
b = int(input())

def equal(a,b):
    if a==b:
        print(a)
    
while a!=b:
    if a>b:
        a = a - b
        equal(a,b)
    else:
        b = b - a
        equal(a,b)