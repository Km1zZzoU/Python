def reverse_dict(S_dict):
    reverse_dict = {}
    
    for key, value in S_dict.items():
        if value in reverse_dict:
            existing_value = reverse_dict[value]
            if isinstance(existing_value, tuple):
                reverse_dict[value] = existing_value + (key,)
            else:
                reverse_dict[value] = (existing_value, key)
        else:
            try:
                hash(value)
                reverse_dict[value] = key
            except TypeError:
                raise ValueError("value not hashable")
    
    return reverse_dict

# Пример использования:
S_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 3, 'e': 3}
print(reverse_dict(S_dict))
