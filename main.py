def fibonacci(limit):
    # Yield Fibonacci numbers a where a < limit
    a,b = 0, 1
    while a < limit:
        yield a
        a,b = b, a+b
    pass

n = int(input())
result = list(fibonacci(n))
print(" ".join(str(x) for x in result))
