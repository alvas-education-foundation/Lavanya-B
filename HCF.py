#github repository- Lavanya-B

N1 = int(input("\nEnter first number: "))
N2 = int(input("\nEnter second number: "))

def HCF(x, y):

    if x > y:
        smaller = y
    else:
        smaller = x
    for i in range(1, smaller+1):
        if((x % i == 0) and (y % i == 0)):
            hcf = i
            
    return hcf

print("\nHCF of", N1,"&", N2,"=", HCF(N1, N2))