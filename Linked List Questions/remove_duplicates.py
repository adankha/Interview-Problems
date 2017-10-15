from LinkedList import *


def remove_unsorted(head):

    if head is None:
        return

    prev_node = head
    curr_node = head
    all_nodes = {}

    while curr_node is not None and curr_node.next is not None:

        next_node = curr_node.next
        if curr_node.data not in all_nodes.keys():
            all_nodes[curr_node.data] = 1
            prev_node = curr_node
        elif curr_node.data in all_nodes.keys():
            prev_node.next = next_node
        curr_node = curr_node.next

    if curr_node.data not in all_nodes.keys():
        all_nodes[curr_node.data] = 1
    else:
        prev_node.next = None


def remove_sorted(head):
    pass


def random_list():
    my_list = LinkedList()
    my_list.add(31)
    my_list.add(31)
    my_list.add(31)
    my_list.add(92)
    my_list.add(26)
    my_list.add(26)
    my_list.add(26)
    my_list.add(31)
    my_list.add(31)
    my_list.add(31)
    return my_list


def main():

    my_list = random_list()

    print('Printing Linked List: ')
    my_list.print_list()

    remove_unsorted(my_list.head)
    my_list.print_list()


if __name__ == '__main__':
    main()
