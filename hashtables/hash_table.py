class HashTable:
    def __init__(self, size):
        # check for size >= 0
        if size < 0:
            raise Exception("Invalid Size")
        self.data = [[] for _ in range(0, size)]
        self.length = 0
        self.capacity = size

    def __str__(self):
        return str(self.__dict__)

    def __hash(self, key):
        # check invalid key ie key should not be empty
        if len(key) < 1:
            raise Exception("Invalid Key")
        hashedKey = 0  # Mistake : None should be used  Any doesn't work
        # None gives error as few line below we add None to int tye - This give unsupported operation exception, should be 0
        for indexChar in range(0, len(key)):
            hashedKey = hashedKey + int(indexChar)
        hashedKey = hashedKey % self.capacity
        return hashedKey

    def set(self, key, value):  # Mistake - missed adding self as first parameter
        # check for key should not be empty
        if len(key) < 1:
            raise Exception("invalid index")
        # get hashed key for index
        hKey = self.__hash(key)  # Mistake : missed using self object to call member function
        print(f"hash of  {key}   - {hKey}")
        # check for existing bucket
        bucket = self.data[hKey]
        print(bucket)
        self.data[hKey].append([key, value])

    def get(self, key):
        # check for valid ie key is not empty
        # hash the key, get index of bucket
        # get the bucket and loop over for the matching key if length of the bucket is more than one.

        if len(key) == 0:
            raise Exception("Invalid key")
        value = None
        h_key = self.__hash(key)
        bucket = self.data[h_key]
        if bucket is not None and len(bucket) > 1:
            for elem in bucket:
                if elem[0] is key:
                    value = elem[1]
        elif len(bucket) == 1:
            value = bucket[0][1]
        return value
