import unittest
from palindrome import baseN, isPalindrome

class TestAll(unittest.TestCase):

    def setUp(self):
        pass

    def test_palindrome_true(self):
        self.assertTrue(isPalindrome(['a','b','c','b','a']))

    def test_palindrome_false(self):
        self.assertFalse(isPalindrome(['a','b','c','d','e']))

    def test_base_4_2(self):
        self.assertEqual(baseN(4,2), [1,0,0])

    def test_base_4_2_wrong(self):
        self.assertNotEqual(baseN(4,2), [1,0,2])

    def test_base_6_3(self):
        self.assertEqual(baseN(6,3), [2,0])

if __name__ == '__main__':
    unittest.main()
