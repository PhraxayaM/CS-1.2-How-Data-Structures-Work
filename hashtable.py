#!python

from linkedlist import LinkedList


class HashTable(object):

    def __init__(self, init_size=8):
        """Initialize this hash table with the given initial size."""
        # Create a new list (used as fixed-size array) of empty linked lists
        self.buckets = [LinkedList() for _ in range(init_size)]

    def __str__(self):
        """Return a formatted string representation of this hash table."""
        items = ['{!r}: {!r}'.format(key, val) for key, val in self.items()]
        return '{' + ', '.join(items) + '}'

    def __repr__(self):
        """Return a string representation of this hash table."""
        return 'HashTable({!r})'.format(self.items())

    def _bucket_index(self, key):
        """Return the bucket index where the given key would be stored."""
        # Calculate the given key's hash code and transform into bucket index
        return hash(key) % len(self.buckets)

    def keys(self):
        """Return a list of all keys in this hash table.
        TODO: Running time: O(N) Why and under what conditions?
        We have to go through all the buckets and then go through all the linked list.
        """

        # Collect all keys in each bucket
        all_keys = []
        for bucket in self.buckets:
            for key, value in bucket.items():
                all_keys.append(key)
        return all_keys

    def values(self):
        """Return a list of all values in this hash table.
        TODO: Running time: O(N) Why and under what conditions?
        We have to go through all the buckets and then go through all the linked list.
        """
        all_values = []
        # TODO: Loop through all buckets
        for bucket in self.buckets:
        # TODO: Collect all values in each bucket
            for key, value in bucket.items():
                all_values.append(value)
        return all_values

    def items(self):
        """Return a list of all items (key-value pairs) in this hash table.
        TODO: Running time: O(N) Why and under what conditions?
        We have to go through all the buckets and then go through all the linked list.
        """
        # Collect all pairs of key-value entries in each bucket
        all_items = []
        for bucket in self.buckets: # b iterations => 0(b*l) = 0(n) overall
            all_items.extend(bucket.items()) # 0(l) because l is list's test_length

            # extend is appending. It is doing the same thing as the code commented below.
            # for item in self.items: # l iterations where l = length of items => 0(l) overall
            #     all_items.append(item) #0(1)
        return all_items #0(n)

    def length(self):
        """Return the number of key-value entries by traversing its buckets.
        TODO: Running time: O(b*n) where b is # buckets, and n is number of entries Why and under what conditions?"""
        """Running time: 0(n) where b is # buckets, and n is number of entries"""
        count = 0 #0(1)
        # TODO: Loop through all buckets
        for bucket in self.buckets: # b iterations => 0(b*l) = 0(b*n/b) = 0(n)
        # TODO: Count number of key-value entries in each bucket
            #count number of key -value entries in each buckets
            count += bucket.length() # 0(l) for length method where l is n divided by b
            #count = count + bucket.length() #0(l) where l = list's length
        return count # 0(1)

    def contains(self, key):
        """Return True if this hash table contains the given key, or False.
        TODO: Running time: O(L) Why and under what conditions? We already know the specific bucket but we still have to go through the linked list"""
        # TODO: Find bucket where given key belongs

        #1) call bucket_index() in order to find the correct buckets
        #2)  create another for loop. for key value in bucket.items ,
        #3) check if current key is equal to key
        #4) if true, return True
        #5) if false, check next node
        bucket_index = self._bucket_index(key) #0(l), l = length
        bucket = self.buckets[bucket_index] # bucket is a linked list
        item = bucket.find(lambda value: value[0] == key)

        #item = (key, value) tuple
        if item is not None:
            return True
        else:
            return False

    def get(self, key):
        """Return the value associated with the given key, or raise KeyError.
        TODO: Running time: O(L) Why and under what conditions? We know which specific bucket to go to but we still have to traverse through all the linked list"""
        # TODO: Find bucket where given key belongs

        ## bucket_index is created so that we know where our index is
        bucket_index = self._bucket_index(key)
        ## bucket is created so we can retrieve the value of the current index we are in by passing in bucket_index.
        ## Having bucket = self.buckets means that bucket is now the whole hash table, and we can retrieve a specific value from that hash table by using [] to pull the value of the current index we are on.

        bucket = self.buckets[bucket_index]
        for current_key, current_value in bucket.items():
        # TODO: Check if key-value entry exists in bucket
            if current_key == key:
        # TODO: If found, return value associated with given key
                return current_value
        # TODO: Otherwise, raise error to tell user get failed
        raise KeyError('Key not found: {}'.format(key))
        # Hint: raise KeyError('Key not found: {}'.format(key))

    def set(self, key, value):
        """Insert or update the given key with its associated value.
        TODO: Running time: O(l) Why and under what conditions? Our item variable uses the lambda method to
        find the specific bucket but we still need to traverse through the linked list_to_append
        """



        bucket_index = self._bucket_index(key) # 0(1)
        bucket = self.buckets[bucket_index] # 0(1)
        item = bucket.find(lambda value: value[0] == key)

        if item is not None: # Update an old key with new value
            bucket.delete(item)
            bucket.append((key, value))
        else:
            bucket.append((key, value))

        # TODO: Find bucket where given key belongs
        # for current_key, current_value in bucket.items():
        # # TODO: Check if key-value entry exists in bucket
        #     if current_key == key:
        # # TODO: If found, update value associated with given key
        #         bucket.delete(current_value)
        # # TODO: Otherwise, insert given key-value entry into bucket
        # bucket.append((key, value))

    def delete(self, key):
        """Delete the given key from this hash table, or raise KeyError.
        TODO: Running time: O(l) because ? We know the specific bucket but we still have to go through each linked list to Find
        the matching key"""
        bucket_index = self._bucket_index(key) #
        bucket = self.buckets[bucket_index]
        item = bucket.find(lambda key_value: key_value[0] == key)

        if item is not None:
            bucket.delete(item)
        else:
            raise KeyError('Key not found: {}'.format(key))
        # TODO: Find bucket where given key belongs
        # for current_key, current_value in bucket.items():
        # # TODO: Check if key-value entry exists in bucket
        #     if current_key == key:
        #         print(current_key)
        # # TODO: If found, delete entry associated with given key
        #         bucket.delete(current_value)
        #         return
        # # TODO: Otherwise, raise error to tell user delete failed
        # raise KeyError('Key not found: {}'.format(key))
        # Hint: raise KeyError('Key not found: {}'.format(key))



def test_hash_table():
    ht = HashTable()
    print('hash table: {}'.format(ht))

    print('\nTesting set:')
    for key, value in [('I', 1), ('V', 5), ('X', 10)]:
        print('set({!r}, {!r})'.format(key, value))
        ht.set(key, value)
        print('hash table: {}'.format(ht))

    print('\nTesting get:')
    for key in ['I', 'V', 'X']:
        value = ht.get(key)
        print('get({!r}): {!r}'.format(key, value))

    print('contains({!r}): {}'.format('X', ht.contains('X')))
    print('length: {}'.format(ht.length()))

    # Enable this after implementing delete method
    delete_implemented = False
    if delete_implemented:
        print('\nTesting delete:')
        for key in ['I', 'V', 'X']:
            print('delete({!r})'.format(key))
            ht.delete(key)
            print('hash table: {}'.format(ht))

        print('contains(X): {}'.format(ht.contains('X')))
        print('length: {}'.format(ht.length()))


if __name__ == '__main__':
    test_hash_table()
