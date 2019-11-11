from functools import wraps, lru_cache


def my_lru_cache(maxsize=None):
    def my_decorator(func):

        @wraps(func)
        def wrapped(*args, **kwargs):

            key = args + tuple(sorted(kwargs.items()))
            if key in wrapped.cache:  # Нашлось в кэше, возвращаем
                wrapped.hits += 1
                wrapped.list_keys.append(wrapped.list_keys.pop(wrapped.list_keys.index(key)))
            else:
                wrapped.misses += 1
                wrapped.list_keys.append(key)
                wrapped.cache[key] = func(*args, **kwargs)
                if maxsize is not None and len(wrapped.cache) > maxsize:
                    wrapped.cache.pop(wrapped.list_keys.pop(0))

            return wrapped.cache[key]

        def cache_info():
            print("CacheInfo(hits={hits}, misses={misses}, maxsize={maxsize}, curr_size={curr_size})". \
                  format(hits=wrapped.hits, misses=wrapped.misses,
                         maxsize=maxsize, curr_size=len(wrapped.cache)))

        def cache_clear():
            wrapped.cache = {}
            wrapped.list_keys = []
            wrapped.hits = wrapped.misses = 0

        wrapped.cache_info = cache_info
        wrapped.cache_clear = cache_clear
        wrapped.maxsize = maxsize
        wrapped.cache = {}
        wrapped.list_keys = []
        wrapped.hits = wrapped.misses = 0

        return wrapped

    return my_decorator


@my_lru_cache(3)
def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)


print([fib(n) for n in range(16)])
fib.cache_info()

print("*******************************************************************")


@lru_cache(3)
def fib2(n):
    if n < 2:
        return n
    return fib2(n - 1) + fib2(n - 2)


print([fib2(n) for n in range(16)])
print(fib2.cache_info())

print("************************clear cache**************************************")
fib.cache_clear()
fib.cache_info()
