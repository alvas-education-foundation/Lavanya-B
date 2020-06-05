# github repository- Lavanya-B

import time 

def fib(num): 
    if num == 0: return 0
    elif num < 2: return 1
    else:
        return fib(num - 1) + fib(num - 2) 

start_time = time.time() 
n = int(input())

for i in range(n):
    print(fib(i), end = ", ")

print()    
print("lead time", round((time.time() - start_time), 5))