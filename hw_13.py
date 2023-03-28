_cache = []

def cache(max_size):
    def decorator(func):
        global _cache
        _cache = [None] * max_size

        def wrapper(*args, **kwargs):
            if _cache[args[0]] is None:
                _cache[args[0]] = func(*args, **kwargs)
            return _cache[args[0]]
        return wrapper
    return decorator

@cache(100)
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)

print(fib(20))
print(_cache)
