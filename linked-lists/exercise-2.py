class Node:
    def __init__(self, data=None, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next


class DoublyLinkedList:
    def __init__(self, head=None):
        self.head = head

    def push(self, data):
        new_node = Node(data, None, self.head)
        self.head = new_node

    def append(self, data):
        if self.head is None:
            self.head = Node(data, None, None)
            return

        itr = self.head
        while itr.next:
            itr = itr.next

        itr.next = Node(data, itr)

    def append_values(self, data_list):
        for data in data_list:
            self.append(data)

    def print(self):
        llstr = ""
        itr = self.head
        if itr is None:
            print("Linked List is empty")
            return

        while itr:
            llstr += str(itr.data)

            if itr.next is not None:
                llstr += "-->"

            itr = itr.next

        print(llstr)

    def insert_after_value(self, data):
        if self.head is None:
            self.head = Node(data)


ll = DoublyLinkedList()
ll.append(1)
ll.append(2)
ll.push(0)
ll.append_values([0, 2, 1, 4, 32, 9])
ll.print()
