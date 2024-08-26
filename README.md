# healthcare_data_encryption_tool

building this data encryption tool that encrypts healthcare data to protect patient information.

i intend to implement AES or RSA encryption
And I would get a way, maybe a working user interface for users to input data and also receive encrypted output by the way.

in otherwords, this tool encrypts healthcare data to protect patient information using AES or RSA encryption algorithms.

### Since it is open source, let me show you how to get it running:

1. **Just install the dependencies i added**: `pip install -r requirements.txt`
2. **then, run the py app**: `python3 run.py`
3. **you can view the web ui** at `http://localhost:5666` i usually reallocate ports for specific projects tho, yours might be `5000`

### Speaking of Encryption Algorithms

- **AES**: symmetric encryption. it requires a key for both encryption and decryption. more like one way thang!
- **RSA**: asymmetric encryption. just uses a pair of keys (like public and private key) for encryption and decryption. so, it is a two way thang!

### Now Let's use it
- enter healthcare data and an encryption key in the web form i designed.
- then, select the encryption method and click "Encrypt" button to get the encrypted output. haha!

## In the future, I will...

- add a decryption functionality.
- implement an additional encryption algorithm (or more).