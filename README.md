# RSA-project
RSA Encryption and Decryption
This Python script demonstrates RSA encryption and decryption functionality. It generates RSA keys from integer input, encrypts the input message, and decrypts the ciphertext back to the original message.

Prerequisites
Python 3.x installed on your system.
How to Run
Clone or download this repository to your local machine.

Navigate to the directory containing the Python script (rsa_encrypt_decrypt.py).

Open a terminal or command prompt.

Run the script by executing the following command:

Copy code
python rsa_encrypt_decrypt.py
Follow the on-screen prompts to input an integer message.

The script will then generate RSA keys, encrypt the input message, and finally decrypt the ciphertext back to the original message. The public and private keys, as well as the ciphertext and decrypted message, will be displayed in the terminal.

Customization
You can modify the keysize parameter in the generate_rsa_keys_from_int function to adjust the key size (in bits) for RSA key generation. By default, it's set to 1024.

The value of the public exponent e is set to 65537 by default. You can change this value if desired.

Contributing
If you find any issues with the code or have suggestions for improvements, please feel free to open an issue or submit a pull request.
