class LRUCache:

    def __init__(self, capacity: int):
        self.limit = capacity
        self.store = OrderedDict()

    def get(self, key: int) -> int:
        if(key in self.store):
            self.store.move_to_end(key)
            return self.store[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if(key in self.store):
            self.store.move_to_end(key)
        else:
            if(len(self.store.keys())+1 > self.limit):
                self.store.popitem(last=False)
        self.store[key]=value
