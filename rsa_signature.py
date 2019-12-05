from hashlib import sha256
from Crypto.PublicKey import RSA
from rsa_keys import RSAKeys

class RSASignature:
    '''Class produce and represents RSA digital signature.'''
    
    def __init__(self, **params):
       self.keys = params['rsa_keys'] 
       self.hash_fun = params['hash_fun']

    def encrypt(self, message):
        self.hash_fun.update(message.encode('UTF-8'))
        hash = int.from_bytes(self.hash_fun.digest(), byteorder='big')
        
        signature = pow(hash, self.keys.d, self.keys.n)
        return signature

    def decrypt(self, cryptogram):
        hash = pow(cryptogram, self.keys.e, self.keys.n)
        return hash


sign = RSASignature(rsa_keys=RSA.generate(1024), hash_fun=sha256())