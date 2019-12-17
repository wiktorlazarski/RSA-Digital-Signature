import random
from random import randint
from math import gcd

class RSAKeys:
	'''Class produces and represents keys for RSA algorithm.'''

	@staticmethod
	def generate(bits=5):
		'''Generates public and private key as well as n = p * q value used in cipher.

			Parameters:
			bits (int): Specifies the number of bits used to create e, d, n

			Returns:
			int: e - public key
			int: d - private key
			int: n - quotient of two prime numbers used to produce keys
		'''
		primes = RSAKeys.list_primes(2 ** (bits - 1) + 1, 2 ** bits)
		
		p, q = random.sample(primes, 2)
		n = p * q
		phi_n = (p - 1) * (q - 1)
		
		primes.remove(p)
		primes.remove(q)
		primes = [p for p in primes if gcd(p, phi_n) == 1]

		e = primes[randint(0, len(primes) - 1)]
		d = e
		while (e * d) % phi_n != 1: d = d + 1
		
		return RSAKeys(e, d, n)

	@staticmethod
	def list_primes(lo, hi):
		'''Returns a list of prime numbers in a given range [lo, hi).

			Parameters:
			lo (int): lower boundary of search space
			hi (int): higher boundary of search space

			Returns:
			[]: list of prime numbers between [lo, hi)
		'''	
		primes = []
		for num in range(lo, hi, 2):
			for i in range(2, num):
				if num % i == 0:
					break
			else:
				primes.append(num)

		return primes

	def __init__(self, e, d, n):
		self.e, self.d, self.n = e, d, n

	@property
	def e(self):
		return self.__e

	@e.setter
	def e(self, e):
		self.__e = e

	@property
	def d(self):
		return self.__d

	@d.setter
	def d(self, d):
		self.__d = d

	@property
	def n(self):
		return self.__n

	@n.setter
	def n(self, n):
		self.__n = n

if __name__ == "__main__":
	msg = 23
	keys = RSAKeys.generate(10)
	encryption = pow(msg, keys.e, keys.n)
	decryption = pow(encryption, keys.d, keys.n)
	if decryption != msg:
		print(f"TEST FAILED : {msg} \t=>\t {decryption}")
	else:	
		print(f"TEST PASSED : {msg} \t=>\t {decryption}")