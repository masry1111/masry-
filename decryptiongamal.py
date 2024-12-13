def mod_inverse(self, a, m):
        m0, x0, x1 = m, 0, 1
        while a > 1:
            q = a // m
            m, a = a % m, m
            x0, x1 = x1 - q * x0, x0
        return x1 + m0 if x1 < 0 else x1

def decrypt(self, ciphertext):
        if not isinstance(ciphertext, tuple) or len(ciphertext) != 2:
            raise ValueError("Ciphertext must be a tuple of two integers (c1, c2).")

        c1, c2 = ciphertext

        # Compute the shared secret
        s = pow(c1, self.private, self.large_prime)

        # Find the modular inverse of the shared secret
        s_inv = self.mod_inverse(s, self.large_prime)

        # Recover the original message
        message = (c2 * s_inv) % self.large_prime

        return message  # Return decrypted message
