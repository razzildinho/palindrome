import unittest
from palindrome import baseN, isPalindrome

class TestAll(unittest.TestCase):

    def setUp(self):
        pass

    def test_palindrome_true(self):
        self.assertTrue(isPalindrome('abcba'))

    def test_palindrome_false(self):
        self.assertFalse(isPalindrome('abcde'))

    def test_palindrome_invalid(self):
        self.assertFalse(isPalindrome(101))

    def test_base_4_2(self):
        self.assertEqual(baseN(4,2), '100')

    def test_base_4_2_wrong(self):
        self.assertNotEqual(baseN(4,2), '102')

    def test_base_6_3(self):
        self.assertEqual(baseN(6,3), '20')

    def test_base_gt_36(self):
        self.assertEqual(baseN(1004, 37), 'Invalid Base')

if __name__ == '__main__':
    unittest.main()
