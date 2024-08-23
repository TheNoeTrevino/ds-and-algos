class Node:
    # elements in a linked list are linked via the node having the address to the next node. AKA: 'next'
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:

    def __init__(self, head=None):
        self.head = head

    def insert_at_beginning(self, data):

        # make a new node with the new data, and the current head as the pointer
        new_node = Node(data, self.head)
        # set the new node as the current head
        self.head = new_node

    def print(self):
        if self.head is None:
            print('Linked List is empty')

        itr = self.head
        llstr = ''

        while itr:
            llstr += str(itr.data) + '-->'
            itr = itr.next

        print(llstr)

ll = LinkedList()
ll.insert_at_beginning(5)
ll.insert_at_beginning(18)
ll.insert_at_beginning(9)
ll.print()
