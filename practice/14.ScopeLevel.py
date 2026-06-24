# Local level variable scope 

def test():
    x = 10
    print(x)

test()

# Global level variable scope

x = 100

def show():
    print(x)

show()


# Modifiying Global level variable
count = 0

def increment():
    global count
    count += 1

increment()

print(count)