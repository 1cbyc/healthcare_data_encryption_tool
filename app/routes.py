# next i want to create the flask routes i will use for this project
from flask import Flask, request, render_template
from .encryption import encrypt_aes, encrypt_rsa, generate_rsa_keypair
import base64

app = Flask(__name__)
private_key, public_key = generate_rsa_keypair()  # to generate the RSA key pair for demo


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        data = request.form['data']
        method = request.form.get('method')
        key = request.form.get('key', '').encode()

        if method == 'aes':
            encrypted_data = encrypt_aes(data.encode(), key)
        elif method == 'rsa':
            encrypted_data = encrypt_rsa(data.encode(), public_key)
        else:
            encrypted_data = b'Invalid method'

        return render_template('result.html', encrypted_data=base64.b64encode(encrypted_data).decode())
    return render_template('index.html')
