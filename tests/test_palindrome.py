import unittest
from src.palindrome import is_palindrome

class TestPalindrome(unittest.TestCase):
    def test_simple_palindromes(self):
        self.assertTrue(is_palindrome("madam"))
        self.assertTrue(is_palindrome("racecar"))
        self.assertTrue(is_palindrome("level"))

    def test_phrase_palindromes(self):
        self.assertTrue(is_palindrome("A man, a plan, a canal: Panama"))
        self.assertTrue(is_palindrome("Was it a car or a cat I saw?"))
        self.assertTrue(is_palindrome("No lemon, no melon"))
        self.assertTrue(is_palindrome("Madam, in Eden, I'm Adam"))
        self.assertTrue(is_palindrome("Eva, can I see bees in a cave?"))
        self.assertTrue(is_palindrome("Never odd or even"))
        self.assertTrue(is_palindrome("Able was I, I saw Elba"))
        self.assertTrue(is_palindrome("Do geese see God?"))
        self.assertTrue(is_palindrome("Murder for a jar of red rum"))
        self.assertTrue(is_palindrome("Step on no pets"))
        self.assertTrue(is_palindrome("Was it a rat I saw?"))
        self.assertTrue(is_palindrome("Yo, Banana Boy!"))
        self.assertTrue(is_palindrome("Rats live on no evil star"))

    def is_palindrome(texto):
    limpio = ''.join(c.lower() for c in texto if c.isalnum())
    return limpio == limpio[::-1]

if __name__ == '__main__':
    unittest.main()