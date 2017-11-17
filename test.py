import unittest
from palindrome import baseN, isPalindrome

class TestAll(unittest.TestCase):

    def setUp(self):
        pass

    def test_palindrome_true(self):
        self.assertTrue(isPalindrome(['a','b','c','b','a']))

    def test_palindrome_false(self):
        self.assertFalse(isPalindrome(['a','b','c','d','e']))

    def test_invalid_palendrome_arg(self):
        with self.assertRaises(Exception) as context:
            isPalindrome('abc')
        self.assertTrue('Invalid argument' in context.exception)

    def test_invalid_int(self):
        with self.assertRaises(Exception) as context:
            baseN('abc',2)
        self.assertTrue('Invalid integer' in context.exception)

    def test_invalid_base(self):
        with self.assertRaises(Exception) as context:
            baseN(43,1)
        self.assertTrue('Invalid base' in context.exception)

    def test_base_4_2(self):
        self.assertEqual(baseN(4,2), [1,0,0])

    def test_base_4_2_wrong(self):
        self.assertNotEqual(baseN(4,2), [1,0,2])

    def test_base_6_3(self):
        self.assertEqual(baseN(6,3), [2,0])

if __name__ == '__main__':
    unittest.main()
