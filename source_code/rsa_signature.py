from hashlib import sha256
from Crypto.PublicKey import RSA
from rsa_keys import RSAKeys

class RSASignature:
    '''Class produce and represents RSA digital signature.'''
    
    def __init__(self, **params):
       self.keys = params['rsa_keys'] 
       self.hash_fun = params['hash_fun']

    def encrypt_message(self, message):
        '''Produces signature from a given message.

			Parameters:
			message (str): plain text message that will be converted into signature.

			Returns:
			int: encrypted hash / RSA digital signature
		'''	
        self.hash_fun.update(message.encode())
        hash = int.from_bytes(self.hash_fun.digest(), byteorder='big')

        if hash >= self.keys.n:
            raise ValueError("RSASignature.encrypt_message : hash greater or equal N")

        signature = pow(hash, self.keys.d, self.keys.n)
        return signature

    def encrypt_hash(self, hash):
        '''Produces signature from a given hash.

			Parameters:
			hash (int): already hashed plain text message that will be converted into signature.

			Returns:
			int: encrypted hash / RSA digital signature
		'''	
        if hash >= self.keys.n:
            raise ValueError("RSASignature.encrypt_hash : hash greater or equal N")

        signature = pow(hash, self.keys.d, self.keys.n)
        return signature

    def decrypt(self, cryptogram):
        '''Performes decryption of a cryptogram(RSA digital signature).

			Parameters:
			cryptogram (str): cryptogram / RSA digital signature that will be converted into hash.

			Returns:
			int: decrypted hash
		'''	
        hash = pow(cryptogram, self.keys.e, self.keys.n)
        return hash

    @property
    def hash_fun(self):
        return self.__hash_fun
    
    @hash_fun.setter
    def hash_fun(self, hash_fun):
        self.__hash_fun = hash_fun