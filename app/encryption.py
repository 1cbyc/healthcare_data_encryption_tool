# first i want to implement the aes and rsa encryption for this project
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend

# first the AES Encryption
def encrypt_aes(data, key):
    cipher = Cipher(algorithms.AES(key), modes.ECB(), backend=default_backend())
    encryptor = cipher.encryptor()
    padded_data = data.ljust(16, b'\x00')  # padding now to ensure data is a multiple of 16 bytes
    return encryptor.update(padded_data) + encryptor.finalize()

# now the RSA Encryption
def generate_rsa_keypair():
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
        backend=default_backend()
    )
    public_key = private_key.public_key()
    return private_key, public_key

def encrypt_rsa(data, public_key):
    return public_key.encrypt(
        data,
        padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()), algorithm=hashes.SHA256())
    )

def load_public_key(pem_data):
    return serialization.load_pem_public_key(
        pem_data,
        backend=default_backend()
    )
