def encrypt(self, message):
        if not isinstance(message, int) or message < 0:
            raise ValueError("Message must be a positive integer.")

        p, g, h = self.public_key

        # Generate a random key for encryption
        k = random.randint(1, p - 2)

        # Compute c1 and c2 for the ciphertext
        c1 = pow(g, k, p)
        s = pow(h, k, p)  # Shared secret
        c2 = (message * s) % p

        return (c1, c2)  # Return ciphertext
