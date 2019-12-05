from random import randint
from math import gcd

class RSAKeys:
	'''Class produces and represents keys for RSA algorithm.'''

	@staticmethod
	def list_primes(lo, hi):	
		primes = []
		for num in range(lo, hi, 2):
			for i in range(2, num):
				if num % i == 0:
					break
			else:
				primes.append(num)

		return primes

	@staticmethod
	def generate_prime_pair(lo, hi):
		primes = RSAKeys.list_primes(lo, hi)

		f_idx = randint(0, len(primes) - 1)
		first = primes.pop(f_idx)
		
		s_idx = randint(0, len(primes) - 1)
		second = primes[s_idx]

		return (first, second)

	def __init__(self, bits=1024):
		self.e, self.d = self.generate(bits)

	def generate(self, bits):
		p, q = RSAKeys.generate_prime_pair(2 ** (bits - 1) + 1, 2 ** bits)
		
		self.n = p * q
		phi_n = (p - 1) * (q - 1)

		return self.generate_keys(phi_n)

	def generate_keys(self, phi_n):
		primes = RSAKeys.list_primes(1, phi_n)
		primes = [p for p in primes if gcd(p, phi_n) == 1]

		e = primes[randint(0, len(primes) - 1)]
	
		d = 1
		while (e * d) % phi_n != 1: d = d + 1

		return e, d
