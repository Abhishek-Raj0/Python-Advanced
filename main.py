n = int(input())
# total = sum(...)  # use a generator expression
# print(total)
total = sum(x*x for x in range(1, n+1))
print(total)