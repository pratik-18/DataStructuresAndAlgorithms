class HashTable:
    def __init__(self):
        self.Max = 100
        self.arr = [ None for i in range(self.Max) ]

    def get_hash(self, key):
        h = 0;
        for char in key:
            h += ord(char)

        return h % self.Max

    def __setitem__(self, key, value):
        self.arr[self.get_hash(key)] = value

    def __getitem__(self, key):
        return self.arr[self.get_hash(key)]

    def __delitem__(self, key):
        self.arr[self.get_hash(key)] = None

    def print(self):
        print(self.arr);


if __name__ == "__main__":

    ht = HashTable();

    ht["a"] = 1
    ht["b"] = 2
    ht["c"] = 3
    ht["d"] = 4
    ht["e"] = 5

    del ht["c"];

    print(ht["e"])
    print(ht["d"])
    print(ht["c"])
    print(ht["b"])
    print(ht["a"])
