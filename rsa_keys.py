from random import randint


class RSAKeys:
	'''Class produce and represents keys for RSA algorithm.'''

	def __init__(self, bits=1024):
		self.e, self.d = self.generate(bits)

	def generate(self, bits):
		primes = RSAKeys.list_primes(2 ** bits - 1, 2 ** (bits - 1))
		

		p_idx = randint(0, len(primes))
		p = primes[p_idx]
		del primes
		
		q_idx = randint(0, len(primes))
		q = primes[q_idx]
		

		return (1, 2)

	@staticmethod
	def list_primes(lo, hi):
		return [1, 2, 3, 5, 7]


keys = RSAKeys()
print("p = {}\nq = {}".format(keys.e, keys.d))