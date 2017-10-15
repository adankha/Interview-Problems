from LinkedList import *


def insert_num(the_list, num):
    """
    Insert an element in a linked-list that is already sorted.
    Edge cases:
    1) List is empty
    2) num is less than head of list [front of list case]
    3) current node <= num <= next node [in between case]
    4) current
    :param the_list:
    :param num:
    :return: Nothing
    """

    head = the_list.head

    if head is None:
        the_list.add(num)
        return
    if num <= head.data:
        the_list.add(num)
        return

    cur_node = head
    next_node = head.next
    new_node = Node(num)

    while cur_node is not None:

        if next_node is not None and cur_node.data <= num <= next_node.data:
            cur_node.next = new_node
            new_node.next = next_node
            return
        elif next_node is None and cur_node.data <= num:
            cur_node.next = new_node
            return
        cur_node = cur_node.next
        next_node = next_node.next


def main():

    sorted_list = LinkedList()
    for i in range(20, 0, -1):
        sorted_list.add(i)

    print('Sorted Linked List: ')
    sorted_list.print_list()
    insert_num(sorted_list, -112)
    insert_num(sorted_list, 66)
    insert_num(sorted_list, -5)
    insert_num(sorted_list, -10)
    print('Sorted Linked List After Insertions 15, -1, 22, -10: ')
    sorted_list.print_list()


if __name__ == '__main__':
    main()
