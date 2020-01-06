import unittest
from rsa_keys import RSAKeys

class TestRSAKeys(unittest.TestCase):

    characters = ['W', 'i', 'K', 't', 'O', 'r']

    def test_keys_generation(self):
        # Test generate method by performing simple RSA encryption/decryption process
        keys = RSAKeys.generate(bits=8)

        for char in self.characters:
            char = ord(char)
            c = pow(char, keys.e, keys.n)
            m = pow(c, keys.d, keys.n)
            
            self.assertEqual(char, m)