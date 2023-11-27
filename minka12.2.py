def chain(*iterables):
    for iterable in iterables:
        yield from iterable

my_list = [21, 23, 34, 24]
result = list(chain([1, 2, 3, 4, 5], ['a', 'python', 'b'], my_list))
print(result)