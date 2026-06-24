numbers = [10, 20, 30, 40]
# start
print(numbers[0])
# end
print(numbers[-1])
# start:end:step
print(numbers[0:-1])
# reverse
print(numbers[::-1])

# append()
numbers.append(50)
print(numbers)

# insert() take position,value
numbers.insert(5,60)
print(numbers)

# remove() 
numbers.remove(60)
print(numbers)

# pop()
numbers.pop()
print(numbers)

# extend()
a = [1, 2]
b = [3, 4]
a.extend(b)
print(a)

# sort()
numbers.sort()
print(numbers)

# reverse()
numbers.reverse()
print(numbers)

# List Comprehensions
squares = []

for i in range(5):
    squares.append(i * i)
print(squares)

squares = [i * i for i in range(5)]
print(squares)

evens = [x for x in range(10) if x % 2 == 0]
print(evens)