class MyHashSet:

    def __init__(self):
        # self.myHashSet=set()
        self.myHashSet=[False]*1000001
        
    def add(self, key: int) -> None:
        # self.myHashSet.add(key)
        self.myHashSet[key]=True

    def remove(self, key: int) -> None:
        # if key in self.myHashSet:
        #     self.myHashSet.remove(key)
        # else:
        #     return None
        self.myHashSet[key]=False

    def contains(self, key: int) -> bool:
        # if key in  self.myHashSet:
        #     return True
        # else:
        #     return False
        return self.myHashSet[key]
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)