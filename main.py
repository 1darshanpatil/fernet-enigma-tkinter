from uiux import SecurityWindow
from ciphering import Cipher
from enigma import Encryptor

if __name__ == "__main__":
    ciphering = Cipher()
    enigma = Encryptor()
    window = SecurityWindow(ciphering, enigma)
