from LinkedList import *


def find_middle(head):
    """
    Finds the middle element of a linked list in log(n) run-time.
    How? We traverse through with iter2 2 times as fast as we do with iter1.
    Since we are traversing x2 with iter2, then iter1 will hold the middle value
    :param head: Head of list
    :return:  Middle element
    """

    if head is None:
        return

    iter1 = head
    iter2 = head.next

    while iter2 and iter2.next:
        iter1 = iter1.next
        iter2 = iter2.next.next
    return iter1.data


def insert_num(the_list, num):

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

        if next_node is not None and cur_node.data < num <= next_node.data:
            cur_node.next = new_node
            new_node.next = next_node
            return
        elif next_node is None and cur_node.data <= num:
            cur_node.next = new_node
            return
        cur_node = cur_node.next
        next_node = next_node.next


def random_list():
    my_list = LinkedList()
    my_list.add(31)
    my_list.add(77)
    my_list.add(17)
    my_list.add(93)
    my_list.add(26)
    my_list.add(54)
    my_list.add(92)
    my_list.add(24)
    return my_list


def main():

    my_list = random_list()

    print('Printing Linked List: ')
    my_list.print_list()

    print('Finding middle element in O(log(n)) time.')
    print('Middle Element: ', find_middle(my_list.head), end="\n\n")

    sorted_list = LinkedList()
    for i in range(20, 0, -1):
        sorted_list.add(i)

    print('Sorted Linked List: ')
    sorted_list.print_list()
    insert_num(sorted_list, 15)
    insert_num(sorted_list, -1)
    insert_num(sorted_list, 22)
    insert_num(sorted_list, -10)
    print('Sorted Linked List After Insertions 15, -1, 22, -10: ')
    sorted_list.print_list()


if __name__ == '__main__':
    main()
