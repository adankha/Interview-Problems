"""
    A simple file that has two classes: Node and LinkedList.
    Used to help with interview problems / questions dealing with linked lists.
"""


class Node:
    def __init__(self,initdata):
        self.data = initdata
        self.next = None

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def set_data(self,newdata):
        self.data = newdata

    def set_next(self,newnext):
        self.next = newnext


class LinkedList:

    def __init__(self):
        self.head = None

    def add(self, item):
        temp = Node(item)
        temp.set_next(self.head)
        self.head = temp

    def print_list(self):
        tmp = self.head
        s = ''

        if tmp is None:
            print('Empty List')
            return 'Empty List'

        while tmp.next is not None:
            print(tmp.data, '-> ', end="")
            s += str(tmp.data) + ' -> '
            tmp = tmp.next
        print(tmp.data)
        s += str(tmp.data)
        return s
