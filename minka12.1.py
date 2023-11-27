def cycle(iterable):
    while True:
        for item in iterable:
            yield item

def take(iterable, n):
    result = []
    for _ in range(n):
        result.append(next(iterable))
    return result

print(take(cycle(['a', 2, ('tuple', 'Tuple')]), 17))