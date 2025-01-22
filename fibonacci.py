

def fibonacci(n = None):
    if n is None:
        n = 100
    a = 0
    b = 1
    while a < n:
        print(a, end=' ')
        temp = a
        a = b
        b = temp + b
    print()

print(fibonacci(1000))
print(fibonacci()) # 100 is the default value
print(fibonacci(10))