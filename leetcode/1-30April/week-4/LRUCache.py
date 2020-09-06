class CacheItem:
    def __init__(self, key: int, value: int):
        self.key = key
        self.val = value
        self.left = None
        self.right = None

class LRUCache:
    def __init__(self, capacity: int):
        self.cache = {}
        self.start = None
        self.end = None
        self.sz = capacity

    def display(self):
        print("start display")
        initial = self.start
        while self.start:
            print(self.start.key, self.start.val, end=";")
            self.start = self.start.right
        self.start = initial
        print()
        print(self.end.key)

    def get(self, key: int) -> int:
        item = self.cache.get(key)
        if item == None:
            return -1

        self.moveToEnd(item)
        self.display()
        return item.val

    def put(self, key: int, value: int) -> None:
        item = None
        if self.cache.get(key) != None:
            item = self.cache.get(key)
            item.val = value
        else:
            #create new item
            item = CacheItem(key, value)

            #check whether the size is okay
            if len(self.cache) + 1 > self.sz:
                self.deleteItem()

        if len(self.cache) == 0:
            self.start = item
            self.end = item

        self.moveToEnd(item)
        self.cache[key] = item
        self.display()

    def deleteItem(self):
        #always delete the start / the LRU
        k = self.start.key
        self.detachItem(self.cache.get(k))
        self.cache.pop(k)

    def detachItem(self, item: CacheItem):
        if len(self.cache) == 0 or len(self.cache) == 1:
            #we can skip this process
            return

        left = item.left
        right = item.right
        if left != None:
            left.right = right
        else: #meaning this is the first
            self.start = self.start.right

        if right != None:
            right.left = left
        else: #meaning this is the last
            print("go a")
            self.end = self.end.left

    def moveToEnd(self, item: CacheItem):
        self.detachItem(item)

        self.end.right = item
        item.left = self.end
        item.right = None
        self.end = item


obj = LRUCache(2)
obj.put(2, 1)
obj.put(3, 2)
obj.get(3)
obj.get(2)
obj.put(4, 3)
obj.get(2)
obj.get(3)
obj.get(4)

print('-----')
test = LRUCache(2)
test.put(1, 1)
test.put(2, 2)
test.get(1)
test.put(3, 3)
test.get(2)
test.put(4, 4)
test.get(1)
test.get(3)
test.get(4)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
