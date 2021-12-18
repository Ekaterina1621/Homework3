import unittest
from math import prod
from minmax import min_num, max_num, sum_num, prod_num, lst_num


class TestListMethods(unittest.TestCase):

    def test_min(self):
        self.assertEqual(min_num(lst_num), min(lst_num))

    def test_max(self):
        self.assertEqual(max_num(lst_num), max(lst_num))

    def test_sum(self):
        self.assertEqual(sum_num(lst_num), sum(lst_num))

    def test_prod(self):
        self.assertEqual(prod_num(lst_num), prod(lst_num))

    def test_speed(self):
        pass

    def test_len1(self):
        self.assertFalse(len(lst_num) == 1)  # проверка на то, что длина списка больше 1


