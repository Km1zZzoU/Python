class LRUCache:
    def __init__(self, capacity=4):
        self.capacity = capacity
        self.cache = {}
        self.order = []
        pass

    def put(self, key, value):
        if len(self.cache) == self.capacity:
            del self.cache[self.order[0]]
        self.cache[key] = value
        print(self.cache)

    def get(self, key):
        if key in self.cache:
            if len(self.order)<self.capacity: 
                self.order.append(key)
            else:
                self.order.remove(key)
                self.order.append(key)
            return self.cache[key]
        else:
            return None
Cache = LRUCache()
Cache.put('a', 1)
Cache.put('b', 2)
Cache.put('c', 3)
Cache.put('d', 4)
print(Cache.get('b'))
Cache.put('d', 5)