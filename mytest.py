import unittest
from mycode import *

class MyFirstTests(unittest.TestCase):

    def test_hello(self):
        """ Check if function return: hello world """
        self.assertEqual(greet_the_world(), 'hello world', 'Function not returning desired value')

    def test_custom_num_list_my(self):
        """ Check if function return identical number list """
        self.assertEqual(my_create_num_list(4), [0, 1, 2, 3])

        """ Check if function return same length of list """
        self.assertEqual(len(my_create_num_list(10)), 10)

    def test_custom_num_list(self):
        self.assertEqual(len(create_num_list(10)), 10)

    def test_three_multiplication(self):
    # check multiply of 3 number
        self.assertEqual(three_multiplication(2,3,6),36, 'Multiply result not matched.')

    def test_power_two_num(self):
        self.assertEqual(power_two_num(3,3),27, 'Result not matched.')

if __name__ == '__main__':
    unittest.main()