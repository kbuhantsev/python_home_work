from functools import wraps


def my_lru_cache(maxsize=None):
    def my_decorator(func):

        @wraps(func)
        def wrapped(*args, **kwargs):

            key = args + tuple(sorted(kwargs.items()))
            if key in wrapped.cache:  # Нашлось в кэше, возвращаем
                wrapped.hits += 1
                return wrapped.cache.get(key)
            else:
                wrapped.misses += 1
                if (maxsize is None) or (len(wrapped.cache) < maxsize):  # Место в кэшэ есть, добавляем
                    wrapped.cache[key] = func(*args, **kwargs)
                    return wrapped.cache[key]
                else:  # Места в кэшэ нет, очищаем
                    sorted(wrapped.cache.items(), key=lambda item: item[1])
                    wrapped.cache[0] = func(*args, **kwargs)
                    return wrapped.cache[0]

        wrapped.maxsize = maxsize
        wrapped.cache = {}
        wrapped.hits = wrapped.misses = 0

        return wrapped

    return my_decorator


@my_lru_cache(None)
def fib(n):

    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)


print([fib(n) for n in range(16)])
print("CacheInfo(hits={hits}, misses={misses}, maxsize={maxsize}, curr_size={curr_size})".\
      format(hits=fib.hits, misses=fib.misses,
             maxsize=fib.maxsize, curr_size=len(fib.cache)))


