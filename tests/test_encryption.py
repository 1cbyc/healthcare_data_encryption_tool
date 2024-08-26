# to test the encryption module i designed
import unittest
from app.encryption import encrypt_aes, encrypt_rsa, generate_rsa_keypair

class TestEncryption(unittest.TestCase):

    def setUp(self):
        self.private_key, self.public_key = generate_rsa_keypair()

    def test_encrypt_aes(self):
        key = b'\x00' * 16
        data = b'Test data'
        encrypted = encrypt_aes(data, key)
        self.assertIsInstance(encrypted, bytes)

    def test_encrypt_rsa(self):
        data = b'Test data'
        encrypted = encrypt_rsa(data, self.public_key)
        self.assertIsInstance(encrypted, bytes)

if __name__ == '__main__':
    unittest.main()
