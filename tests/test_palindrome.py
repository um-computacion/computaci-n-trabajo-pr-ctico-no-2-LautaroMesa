import unittest
from src.palindrome import is_palindrome

class TestPalindrome(unittest.TestCase):
    def test_simple_palindromes(self):
        self.assertTrue(is_palindrome("madam"))
        self.assertTrue(is_palindrome("racecar"))
        self.assertTrue(is_palindrome("level"))
        
    def test_phrase_palindromes(self):
        self.assertTrue(is_palindrome("Dábale arroz a la zorra el abad"))
        self.assertTrue(is_palindrome("A mamá Roma le aviva el amor a mamá"))
        self.assertTrue(is_palindrome("Anita lava la tina"))

if __name__ == '__main__':
    unittest.main()