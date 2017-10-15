from LinkedList import *


def remove_unsorted(head):
    """
    Removes all duplicate elements in an unsorted linked list.
    Explanation:
        We have 3 pointers, a previous, current, and next.
        The variable names hold exactly what you think they hold.
        Essentially what we do is we have a library which holds numbers in which we've discovered.
        If we ever come across a number we've came across (and it's in our dictionary), we take the prev.next pointer
        and point it to the next node, skipping over the current.

        Note: Be careful with how you assign the previous. If we did not find a key, we set prev to current.
        If we found a key, we set previous to next node.

        Since our loop terminates without current ever being the last element, make sure you check if the element is at
        the end of the list.

    :param head: Head of list
    :return: Nada!
    """

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

    if curr_node.data in all_nodes.keys():
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
