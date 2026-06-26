import os
import sys

print(os.getcwd())
print(os.listdir())

print(sys.version)
print(sys.argv)
# print(sys.exit())

from datetime import datetime
now = datetime.now()
print(now)
print(now.date())
print(now.time())

import math
print(math.sqrt(36))
print(math.factorial(5))
print(math.pi)

import random
print(random.randint(1, 10))
colors = ["Red", "Blue", "Green"]
print(random.choice(colors))

from itertools import count, permutations, combinations
counter = count(1)
for _ in range(5):
    print(next(counter))

print(list(permutations([1,2,3], 2)))
print(list(combinations([1,2,3], 2)))