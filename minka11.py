def singleton(cls):
    list = {}

    def get_list():
        if cls not in list:
            list[cls] = cls()
        return list[cls]

    return get_list

@singleton
class MyClass:
    def __init__(self):
        print("Created new class")

instance1 = MyClass()
instance2 = MyClass()

print(instance1 is instance2)