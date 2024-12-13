import random

class ElGamal:
    def __init__(self):
        # Key generation: Initialize parameters and generate keys
        self.large_prime = self.create_large_prime()
        self.generator = self.get_primitive_root(self.large_prime)
        self.private = self.create_private_key(self.large_prime)
        self.public = self.calculate_public_key(self.generator, self.private, self.large_prime)
        self.public_key = (self.large_prime, self.generator, self.public)

    def is_prime(self, n):
        if n <= 1:
            raise ValueError("Invalid number. Must be greater than 1.")
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    def create_large_prime(self):
        while True:
            p = random.randint(10**6, 10**7)
            if self.is_prime(p):
                return p

    def get_primitive_root(self, p):
        for g in range(2, p):
            if all(pow(g, (p - 1) // q, p) != 1 for q in range(2, p) if (p - 1) % q == 0):
                return g
        raise ValueError("Primitive root not found.")

    def create_private_key(self, p):
        return random.randint(1, p - 2)

    def calculate_public_key(self, g, x, p):
        return pow(g, x, p)
