# Github repository- Lavanya-B

from itertools import cycle

count = 0
for letter in cycle('Hello'):
    if count > 20:
        break
    print(letter)
    count += 1