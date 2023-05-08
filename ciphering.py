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


if __name__ == "__main__":
    cipher = Cipher()
    choice = input("Do you want to encrypt or decrypt? [E/D]: ")
    if choice.lower() == "e":
        if input("Do you have key[Y/N]? ").lower() == 'y':
            key = input("Please enter your secret key: ")
            # cipher.pass_key(key)
        else:
            key = cipher.get_key()
            print(f"Your secret key\n{key.decode()} is copied to clipboard.")
            pyperclip.copy(key.decode())
        print("Please enter your text to be encrypted.")
        message_s = input()
        try:
            encry = cipher.encrypt_text(key, message_s)
            print(f"Encrypted text\n{encry.decode()}")
        except ValueError as VE:
            print(f"Seems you entered wrong key as {VE}")

    elif choice.lower() == "d":
        try:
            key = input("Please enter your secret key: ")
            cipher.pass_key(key)
            print("Please enter your cipher text to be decrypted: ")
            message_cfr = input()
            plen = cipher.decrypt_text(key, message_cfr)
            print(f"Your decrypted cipher is\n{plen}")
        except cryptography.fernet.InvalidToken:
            print("Uh-ho! Something went wrong.")
    else:
        print("Invalid input")
