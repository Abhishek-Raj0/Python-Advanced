import re
n = int(input())
for _ in range(n):
    email = input().strip()
    # Validate and print result
    if re.match(r"^[^@]+@[^@]+\.[^@]+$", email):
        print("valid")
    else:
        print("invalid")