import unittest

from insert_in_sorted import *
from middle_element import find_middle


class LinkedListTests(unittest.TestCase):

    def test_insert(self):
        my_list = LinkedList()
        my_list.add(4)
        my_list.add(2)
        my_list.add(1)
        my_list.print_list()
        self.assertEqual(insert_num(my_list, 0), True)
        self.assertEqual(insert_num(my_list, -2), True)
        self.assertEqual(insert_num(my_list, 10), True)
        self.assertEqual(insert_num(my_list, 3), True)
        self.assertEqual(my_list.print_list(), "-2 -> 0 -> 1 -> 2 -> 3 -> 4 -> 10")

    def test_middle(self):
        my_list = LinkedList()
        my_list.add(1)
        my_list.add(2)
        my_list.add(4)
        self.assertEqual(find_middle(my_list.head), 2)

    def test_middle_empty(self):
        my_list2 = LinkedList()
        self.assertEqual(find_middle(my_list2.head), None)


if __name__ == '__main__':
    unittest.main()
