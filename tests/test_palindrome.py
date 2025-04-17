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

    def test_non_palindromes(self):
        self.assertFalse(is_palindrome("hello"))
        self.assertFalse(is_palindrome("python"))
        self.assertFalse(is_palindrome("This is not a palindrome"))
        self.assertFalse(is_palindrome("computacion"))
        self.assertFalse(is_palindrome("milestone"))
        self.assertFalse(is_palindrome("issue"))
        self.assertFalse(is_palindrome("labels"))

    def test_edge_cases(self):
        self.assertTrue(is_palindrome("")) #cadena vacia
        self.assertTrue(is_palindrome("a")) #un solo caracter 
        self.assertTrue(is_palindrome("A")) #un solo caracter mayuscula
        self.assertTrue(is_palindrome(" "))  # espacio
        self.assertTrue(is_palindrome("   "))  # varios espacios
        self.assertTrue(is_palindrome("!!!"))  # solo símbolos
        self.assertTrue(is_palindrome("1"))  # número único
        self.assertTrue(is_palindrome("121"))  # número palíndromo
        self.assertFalse(is_palindrome("  a"))  # con espacios desbalanceados
        self.assertFalse(is_palindrome("a "))  # con espacios desbalanceados

    def is_palindrome(texto):
    limpio = ''.join(c.lower() for c in texto if c.isalnum())
    return limpio == limpio[::-1]

if __name__ == '__main__':
    unittest.main()