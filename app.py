import random
import string
from flask import Flask, render_template, request

app = Flask(__name__)

def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            is_upper = char.isupper()
            offset = ord('A') if is_upper else ord('a')
            result += chr((ord(char) - offset + shift) % 26 + offset)
        else:
            result += char
    return result

def polyalphabetic_cipher(text, keyword):
    result = ""
    for i, char in enumerate(text):
        if char.isalpha():
            is_upper = char.isupper()
            offset = ord('A') if is_upper else ord('a')
            key_char = keyword[i % len(keyword)]
            key_offset = ord(key_char)
            result += chr((ord(char) - offset + (key_offset - ord('A'))) % 26 + offset)
        else:
            result += char
    return result

def generate_random_keyword():
    length = random.randint(5, 10)
    return ''.join(random.choice(string.ascii_uppercase) for _ in range(length))

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        original_text = request.form['original_text']
        cipher_type = request.form['cipher_type']

        return render_template('cipher_page.html', original_text=original_text, cipher_type=cipher_type)

    return render_template('index.html')

@app.route('/cipher_page', methods=['POST'])
def cipher_page():
    original_text = request.form['original_text']
    cipher_type = request.form['cipher_type']
    encrypt_choice = request.form['encrypt']
    keyword = None

    if cipher_type == 'caesar':
        shift = 3  # Adjust the shift value as needed
        result_text = caesar_cipher(original_text, shift) if encrypt_choice == 'Encrypt' else original_text

    elif cipher_type == 'polyalphabetic':
        if encrypt_choice == 'Encrypt':
            keyword = generate_random_keyword()
            result_text = polyalphabetic_cipher(original_text, keyword)
        else:
            result_text = original_text

    return render_template('cipher_page.html', original_text=original_text, cipher_type=cipher_type, result_text=result_text, encrypt_choice=encrypt_choice, keyword=keyword if encrypt_choice == 'Encrypt' else None)


if __name__ == '__main__':
    app.run(debug=True)




 













