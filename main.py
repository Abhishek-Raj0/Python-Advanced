from functools import wraps

def logged(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        # Print the log line and return result
        print(f"called {func.__name__}: {result}")
        return result
    return wrapper

@logged
def add(a, b):
    return a + b

a = int(input())
b = int(input())
add(a, b)