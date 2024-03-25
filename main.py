import random
from math import gcd


def miller_rabin_test(n, k=5):
    if n <= 1:
        return False
    if n <= 3:
        return True


    d = n - 1
    s = 0
    while d % 2 == 0:
        d //= 2
        s += 1

    # Repeat k times
    for _ in range(k):
        a = random.randint(2, n - 1)
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(s - 1):
            x = pow(x, 2, n)
            if x == 1:
                return False
            if x == n - 1:
                break
        else:
            return False
    return True


def generate_prime_candidate(length):
    # Generate an odd number
    p = random.getrandbits(length)
    p |= (1 << length - 1) | 1
    return p


def generate_prime(length=1024, k=5):
    while True:
        p = generate_prime_candidate(length)
        if miller_rabin_test(p, k):
            return p


def extended_gcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = extended_gcd(b % a, a)
        return (g, x - (b // a) * y, y)


def modinv(a, m):
    g, x, y = extended_gcd(a, m)
    if g != 1:
        raise Exception('Modular inverse does not exist')
    else:
        return x % m


def generate_rsa_keys_from_int(message, keysize=1024):
    # Generate two distinct prime numbers based on the specified key size
    p = generate_prime(keysize // 2)
    q = generate_prime(keysize // 2)

    n = p * q
    phi = (p - 1) * (q - 1)


    e = 65537

    # Verify that e is relatively prime to phi(n)
    if gcd(e, phi) != 1:
        # Start over if e is not relatively prime to phi(n)
        return generate_rsa_keys_from_int(message, keysize)

    d = modinv(e, phi)

    return (e, n), (d, n)


def rsa_encrypt(message, public_key):
    e, n = public_key
    return pow(message, e, n)


def rsa_decrypt(ciphertext, private_key):
    d, n = private_key
    return pow(ciphertext, d, n)



message = int(input("Enter an integer message to generate RSA keys and encrypt: "))


public_key, private_key = generate_rsa_keys_from_int(message)
print("Public Key:", public_key)
print("Private Key:", private_key)


ciphertext = rsa_encrypt(message, public_key)
print("Ciphertext:", ciphertext)


decrypted_message = rsa_decrypt(ciphertext, private_key)
print("Decrypted Message:", decrypted_message)
