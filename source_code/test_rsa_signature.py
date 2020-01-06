import unittest
from hashlib import sha256
from rsa_signature import RSASignature
from rsa_keys import RSAKeys
from Crypto.PublicKey import RSA

class TestRSASignature(unittest.TestCase):

    messages = ['ECRYP', 'lorem ipsum', 'wiktor', 'cryptography']
    hashes = [2 ** 5, 2 ** 6, 2 ** 10, 2 ** 14]

    def test_encrypt_msg(self):
        # Test hashes equals after ecryption-decryption process
        signature = RSASignature(rsa_keys=RSA.generate(1024), hash_fun=sha256())
        
        for msg in self.messages:
            hash_fun = sha256()
            signature.hash_fun = hash_fun.copy()
            
            hash_fun.update(msg.encode())
            before = int.from_bytes(hash_fun.digest(), byteorder='big')
            
            after = signature.decrypt(signature.encrypt_message(msg))

            self.assertEqual(before, after)

        # Test if encrypt_message method raise exception when hash >= n
        signature = RSASignature(rsa_keys=RSAKeys.generate(bits=8), hash_fun=sha256()) 
        self.assertRaises(ValueError, signature.encrypt_message, self.messages[0])

    def test_encrypt_hash(self):
        # Test hashes equals after ecryption-decryption process
        signature = RSASignature(rsa_keys=RSAKeys.generate(bits=8), hash_fun=sha256())

        for hash in self.hashes:
            after = signature.decrypt(signature.encrypt_hash(hash))

            self.assertEqual(hash, after)

        # Test if encrypt_message method raise exception when hash >= n
        signature = RSASignature(rsa_keys=RSAKeys.generate(bits=8), hash_fun=sha256()) 
        self.assertRaises(ValueError, signature.encrypt_hash, 2 ** 20)
