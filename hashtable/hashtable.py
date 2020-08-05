class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

    # def __str__(self):
    #     return f'{self.value}'

# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity):
        # Your code here
        self.capacity = capacity
        self.storage = [None] * capacity
        self.count = 0


    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        # Your code here
        return len(self.storage)


    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        # Your code here
        return self.count / self.capacity
        


    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit
        Implement this, and/or DJB2.
        """
        # Your code here
        FNV_offset_basis = 14695981039346656037
        FNV_prime = 1099511628211

        hashed = FNV_offset_basis

        string_bytes = key.encode()
        for b in string_bytes:
            hashed = hashed * FNV_prime
            hashed = hashed ^ b
        return hashed


    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        # Your code here

        # my original implementation
        # needs ord()
        # hash_value = 5381
        # for el in key:
        #     hash_value = (hash_value * 33) + ord(el)
        # return hash_value

        # guided code (day 2)
        # does not need ord() 
        hash_var = 5381
        string_bytes = key.encode()
        for b in string_bytes:
            # << is called a left shift, adds x amount of 0's to the end a number
            hash_var =((hash_var << 5) + hash_var) + b
        return hash_var
        
    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        #return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        # Your code here
        self.count += 1
        # check if load factor is to low or too high

        load = self.get_load_factor()
        if load > 0.7:
            self.resize(self.capacity * 2)
        index = self.hash_index(key)

        # self.storage[index] = value
        current = self.storage[index]
        while current is not None:
            if current.key == key:
                current.value = value
                return
            current = current.next
        entry = HashTableEntry(key, value)
        entry.next = self.storage[index]
        self.storage[index] = entry
        # print(self.storage[index].value, "==",entry.value)
        
    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        # Your code here
        self.count -= 1
        # check if load factor is too low 
        # if it is, call resize
        
        index = self.hash_index(key)
        if self.storage[index]is not None:
            current = self.storage[index]
            if current.key == key:
                if current.next is not None:
                    current = current.next
                    self.storage[index] = current
                else:
                    self.storage[index] = None
                return current
            previous = current
            current = current.next
            while current is not None:
                if current.key == key:
                    previous.next = current.next
                    current.next = None
                    return current
                else:
                    previous = current
                    current = current.next
            return None
        else:
        # if deleted:
        #     self.storage[target] = None
        # else:
            print("Warning: key not found")
            return None

    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        # Your code here
        index = self.hash_index(key)
        if self.storage[index]:
            current = self.storage[index]
            while current is not None:
                if current.key == key:
                    return current.value
                current = current.next
        else:
            return None


    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # Your code here
        new_storage = [None] * new_capacity
        index = 0
        for entry in self.storage:
            new_storage[index] = entry
            index +=1
        self.storage = new_storage





if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    # old_capacity = ht.get_num_slots()
    # ht.resize(ht.capacity * 2)
    # new_capacity = ht.get_num_slots()

    # print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")
