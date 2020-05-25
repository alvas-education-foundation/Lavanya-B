
#A number is said to be pronic if it is the product of two consecutive numbers.
import math
n=int(input ())
num=int(math.sqrt(n))
if(n==num*(num+1)):
    print (n,":True")
        
else:
    print (n,":False")