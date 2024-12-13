import random

class ElGamal:
    def __init__(self):
        # Generate a large prime number to be used for the encryption process.
        self.large_prime = self.create_large_prime()
        # Find a primitive root modulo for the large prime number.
        self.generator = self.get_primitive_root(self.large_prime)
        # Create a private key (the number needs to be less than the prime number)
        self.private = self.create_private_key(self.large_prime)
        # Calculate the public key using the generator, private key, and the large prime number.
        self.public = self.calculate_public_key(self.generator, self.private, self.large_prime)
        # Store the public key components large prime number, generator and the value of public .
        self.public_key = (self.large_prime, self.generator, self.public)

    #check if n is prime number 
    def is_prime(self, n):
        if n <= 1:
            raise ValueError("invalid number")
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    #generate a number between the range of 10^6-10^7 until a number is found
    def create_large_prime(self):
        while True:
            p = random.randint(10**6, 10**7)
            if self.is_prime(p):
                return p
    #find the primitive root
    def get_primitive_root(self, p):
        for g in range(2, p): #test starting from 2
            if all(pow(g, (p - 1) // q, p) != 1 for q in range(2, p) if (p - 1) % q == 0):
                return g #only return if primitive root is found
        raise ValueError("primitive root is not found for the prime number.")

    #generate a private key that must be between 1 and p-2
    def create_private_key(self, p):
        return random.randint(1, p - 2)
    #calculate the public key using the g^x mod p equation
    def calculate_public_key(self, g, x, p):
        return pow(g, x, p)
    #calculating the mod inverse of modulo m using euclidean algorithm
    def mod_inverse(self, a, m):
        m0, x0, x1 = m, 0, 1
        if m == 1:
            return 0 #returns 0 as modular inverse can't exist if m is 1
        while a > 1:
            q = a // m
            m, a = a % m, m
            x0, x1 = x1 - q * x0, x0
        if x1 < 0:
            x1 += m0 #make sure the answer is positive
        return x1

    #encrypting message using public key
    def encrypt(self, message):
        if not isinstance(message, int) or message<0:
            raise ValueError("please enter a positive integer: ")
        
            
        
        p, g, h = self.public_key

        # Generate a random temporary key k for encryption.
        k = random.randint(1, p - 2)

        # Calculate c1
        c1 = pow(g, k, p)
        # The secret value needed for encryption and decryption process
        s = pow(h, k, p)
        # Get c2
        c2 = (message * s) % p

        # Return ciphertext
        return (c1, c2)

    def decrypt(self, ciphertext):
        if not isinstance(ciphertext, tuple) or len(ciphertext) != 2:
            raise ValueError("Ciphertext must be a tuple of two integers (c1, c2).")
        
        c1, c2 = ciphertext

        # Get the shared secret
        s = pow(c1, self.private, self.large_prime)

        # Calculate the modular inverse of s
        s_inv = self.mod_inverse(s, self.large_prime)

        # Recover the original message
        m = (c2 * s_inv) % self.large_prime

        # Return the decrypted message
        return m

# Example
if __name__ == "__main__":
    try:
        elgamal = ElGamal()
        print("Public Key (p, g, h):", elgamal.public_key)
        print("Private Key (x):", elgamal.private)

        # Encrypt a message
        message =int(input("please input message: "))
        ciphertext = elgamal.encrypt(message)
        print("Ciphertext (c1, c2):", ciphertext)

        # Decrypt the message
        decrypted_message = elgamal.decrypt(ciphertext)
        print("Decrypted Message:", decrypted_message)

    except ValueError as e:
        print("Error:", e)
    except Exception as e:
        print("An unexpected error occurred:", e)