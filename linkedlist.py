#!python


class Node(object):

    def __init__(self, data):
        """Initialize this node with the given data."""
        self.data = data
        self.next = None

    def __repr__(self):
        """Return a string representation of this node."""
        return 'Node({!r})'.format(self.data)


class LinkedList(object):

    def __init__(self, items=None):
        """Initialize this linked list and append the given items, if any."""
        self.head = None  # First node
        self.tail = None  # Last node
        # Append given items
        if items is not None:
            for item in items:
                self.append(item)

    def __str__(self):
        """Return a formatted string representation of this linked list."""
        items = ['({!r})'.format(item) for item in self.items()]
        return '[{}]'.format(' -> '.join(items))

    def __repr__(self):
        """Return a string representation of this linked list."""
        return 'LinkedList({!r})'.format(self.items())

    def items(self):
        """Return a list (dynamic array) of all items in this linked list.
        Best and worst case running time: O(n) for n items in the list (length)
        because we always need to loop through all n nodes to get each item."""
        items = []  # O(1) time to create empty list
        # Start at head node
        node = self.head  # O(1) time to assign new variable
        # Loop until node is None, which is one node too far past tail
        while node is not None:  # Always n iterations because no early return
            items.append(node.data)  # O(1) time (on average) to append to list
            # Skip to next node to advance forward in linked list
            node = node.next  # O(1) time to reassign variable
        # Now list contains items from all nodes
        return items  # O(1) time to return list

    def is_empty(self):
        """Return a boolean indicating whether this linked list is empty."""
        return self.head is None

    def length(self):
        """Return the length of this linked list by traversing its nodes.
        TODO: Running time: O(n) Why and under what conditions?
we have to loop through all the nodes and increment the count one by one
        """
        # TODO: Loop through all nodes and count one for each
        length_counter = 0
        current = self.head

        while current is not None:
            current = current.next
            length_counter += 1
        return length_counter

    def append(self, item):
        """Insert the given item at the tail of this linked list.
        TODO: Running time: O(1) Why and under what conditions?

        it's constant because we know exactly where the tail is and can append exactly where we want.

        """
        # TODO: Create new node to hold given item
        # TODO: Append node after tail, if it exists
        # tail_node = self.tail
        # head_node = self.head
        new_node = Node(item)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

        return

    def prepend(self, item):
        """Insert the given item at the head of this linked list.
        TODO: Running time: O(1) Why and under what conditions?
        we know exactly where the head is
        """
        # TODO: Create new node to hold given item
        # TODO: Prepend node before head, if it exists
        new_node = Node(item)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            #new node that is created needs to point to the current head first
            new_node.next = self.head
            # head now points to the new node
            self.head = new_node

        return




    def find(self, quality):
        """Return an item from this linked list satisfying the given quality.
        TODO: Best case running time: O(???) Why and under what conditions?
        Best case running time is 0(1) if data is found in the first node.

        TODO: Worst case running time: O(???) Why and under what conditions?
        worst case is 0(n) if data is not found in the listself.
        Where n is the number of items stored in the linked list.
        """

        # TODO: Loop through all nodes to find item where quality(item) is True
        # TODO: Check if node's data satisfies given quality function

        current_node = self.head #0(1)
        # Loop until the node is None, which is one node too far past the tail

        while current_node is not None: # from 1 to n iterations
            #Check is this node's data satifies the given quality function
            if quality(current_node.data) is True: # 0(1)
                # Return this node's data that satifies the quality function
                return current_node.data #0(1)
            else:
                current_node = current_node.next # 0(1) to reassign variable

        # returning none because it was never found
        return None # 0(1)

    def delete(self, item):
        found = False
        node = Node(item)

        previous_node = None
        current_node = self.head

        # Make sure linked list is not empty
        while current_node is not None:
            #Search for matching parameters
            if current_node.data == node.data:
                found = True
                current_node.prev = previous_node
                #check to make sure previous node is not empty
                if previous_node is not None:
                    # If previous node isn't None, then set the pointer for the previous_node to be equal to current_nodes pointer
                    previous_node.next = current_node.next
                else:
                    #If previous node is equal to None, set the head equal to our current_node's pointer
                    self.head = current_node.next
                    # if our current_node is pointing to None, set the tail equal to our previous_node
                if current_node.next == None:
                    self.tail = previous_node
            previous_node = current_node
            current_node = current_node.next
        if not found:
            raise ValueError('Item not found: {}'.format(item))



"""Delete the given item from this linked list, or raise ValueError.
TODO: Best case running time: O(1) Why and under what conditions?
It would have to be the first node and then we don't have to go through the rest of the nodes in the linked list
TODO: Worst case running time: O(N) Why and under what conditions?
This is if the item we are looking for is at the end and we have to go through all the nodes
"""

def test_linked_list():
    ll = LinkedList()
    print('list: {}'.format(ll))

    print('\nTesting append:')
    for item in ['A', 'B', 'C']:
        print('append({!r})'.format(item))
        ll.append(item)
        print('list: {}'.format(ll))

    print('head: {}'.format(ll.head))
    print('tail: {}'.format(ll.tail))
    print('length: {}'.format(ll.length()))

    # Enable this after implementing delete method
    delete_implemented = False
    if delete_implemented:
        print('\nTesting delete:')
        for item in ['B', 'C', 'A']:
            print('delete({!r})'.format(item))
            ll.delete(item)
            print('list: {}'.format(ll))

        print('head: {}'.format(ll.head))
        print('tail: {}'.format(ll.tail))
        print('length: {}'.format(ll.length()))


if __name__ == '__main__':
    test_linked_list()
