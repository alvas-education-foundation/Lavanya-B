#github repository- Lavanya-B

arr = [7,4,2,8,7,6,1]
odd = lambda x: x % 2
even = lambda x: not(x % 2)
odd = list(filter(odd, arr))
even = list(filter(even, arr))
odd.sort()
even.sort()
print(odd)
print(even)