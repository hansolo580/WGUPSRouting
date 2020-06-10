class LoadHashTable:

    def __init__(self, key, item):
        self.key = key
        self.item = item


class HashTable:

    # This constructs the table. Complexity is O(1)
    def __init__(self, initialize=10):
        # initializes a hash table with empty buckets.
        self.map = []
        for i in range(initialize):
            self.map.append([])

    # getter to generate hash key. Complexity is O(1)
    def get_hash_key(self, key):
        hash_key = int(key) % len(self.map)
        return hash_key

    # setter to insert new value to HashTable. Complexity is O(N)
    def add_package(self, key, value):
        package_key = self.get_hash_key(key)
        package_value = [key, value]

        if self.map[package_key] is None:
            self.map[package_key] = list([package_value])
            return True
        else:
            for i in self.map[package_key]:
                if i[0] == key:
                    i[1] = package_value
                    return True
            self.map[package_key].append(package_value)
            return True

    # setter to update existing package. Complexity is O(N)
    def update_package(self, key, value):
        package_key = self.get_hash_key(key)
        if self.map[package_key] is not None:
            for i in self.map[package_key]:
                if i[0] == key:
                    i[1] = value
                    print(i[1])
                    return True
        else:
            print('Error updating package at key: ' + key)

    # getter to read data from HashTable. Complexity is O(N)
    def get(self, key):
        package_key = self.get_hash_key(key)
        if self.map[package_key] is not None:
            for i in self.map[package_key]:
                if i[0] == key:
                    return i[1]
        return None

    # deletes data from HashTable. Complexity is O(N)
    def delete(self, key):
        package_key = self.get_hash_key(key)

        if self.map[package_key] is None:
            return False
        for i in range(0, len(self.map[package_key])):
            if self.map[package_key][i][0] == key:
                self.map[package_key].pop(i)
                return True
        return False
