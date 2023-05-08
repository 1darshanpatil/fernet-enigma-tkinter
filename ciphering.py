from cryptography.fernet import Fernet


class Cipher:
    def __init__(self):
        self.key = None
        self.cipher_suite = None


    def pass_key(self, key):
        self.key = key
        self.cipher_suite = Fernet(self.key)

    def get_key(self):
        self.key = Fernet.generate_key()
        self.pass_key(self.key)
        return self.key

    def encrypt_text(self, key, plaintext):
        #print(key, plaintext)
        self.pass_key(key)
        en_text = plaintext
        encoded_text = en_text.encode()
        encrypted_txt = self.cipher_suite.encrypt(encoded_text)
        # encode_encrypted_txt = encrypted_txt.encode()
        # print(encrypted_txt.decode())
        return encrypted_txt

    def decrypt_text(self, key, cfr):
        #print(key, cfr)
        self.pass_key(key)
        encrypted_txt = cfr
        decrypted_txt = self.cipher_suite.decrypt(encrypted_txt)
        txt = decrypted_txt.decode()
        # print(txt)
        return txt

'''
if __name__ == "__main__":
    cipher = Cipher()
    print("Do you want to encrypt or decrypt? [E/D]")
    choice = input()
    if choice.lower() == "e":
        cipher.encrypt_text()
    elif choice.lower() == "d":
        cipher.decrypt_text()
    else:
        print("Invalid input")
    cipher.encrypt_text()
'''