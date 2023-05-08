from rotors import Rotor_lst

class Encryptor:
    def __init__(self):
        self.rotor_lst = Rotor_lst
        self.package_e = None # self._encrypt_package(self.pin, self.rotor_lst)


    def get_pin(self, pin):
        self.package_e = self._encrypt_package([int(x) for x in pin], self.rotor_lst)

    def _rotate_single_dict_using_single_int(self, x, dc):
        dc_rotated = {}
        keys, values = zip(*dc.items())
        for cnt in range(len(dc)):
            dc_rotated[keys[cnt]] = values[(cnt - x) % len(dc)]
        return dc_rotated

    def _encrypt_package(self, PIN, rotor_lst):
        package_e = []
        for x in range(6):
            pn = PIN[x]
            package_e.append(self._rotate_single_dict_using_single_int(pn, rotor_lst[x]))
        return package_e

    def _pass(self, ch):
        for x in range(6):
            ch = self.package_e[x][ch]
        return ch

    def _gkf_vod(self, dc, val):
        return list(dc.keys())[list(dc.values()).index(val)]

    def _unpass(self, ch):
        for x in range(1, 7):
            ch = self._gkf_vod(self.package_e[-x], ch)
        return ch

    def _update(self):
        # if e_or_d == 1:
        self.package_e = self._encrypt_package([1 for _ in range(6)], self.package_e)
        # else:
        #    self.package_e = self._encrypt_package([-1 for _ in range(6)], self.package_e)

    def encrypt_password(self, password):
        password_e = ''
        for str_ in password:
            password_e += self._pass(str_)
            self._update()
        return password_e

    def decrypt_password(self, password_e):
        password = ''
        for str_ in password_e:
            password += self._unpass(str_)
            self._update()
        return password





if __name__ == '__main__':
    pin = input("Enter your 6-digit PIN to encrypt/decrypt the password: ")
    if len(pin) == 6 and pin.isnumeric():
        encryptor = Encryptor()
        encryptor.get_pin(pin)
        e_or_d = input("Enter 'e' to encrypt the password or 'd' to decrypt the password: ")
        if e_or_d == 'e':
            password = input("Enter the password to encrypt: ")
            password_e = encryptor.encrypt_password(password)
            print("Encrypted password is: ", password_e)
        elif e_or_d.lower() == 'd':
            password_e = input("Enter the password to decrypt: ")
            password = encryptor.decrypt_password(password_e)
            print("Decrypted password is: ", password)
        else:
            print("Invalid input")
            print("Exiting...")
    else:
        if not pin.isnumeric():
            print("The above is not PIN, Please only enter numbers")
        else:
            if len(pin) == 1:
                print(f"The above PIN is of 1-digit only, Please enter 6-digit PIN")
            elif len(pin) < 6:
                print(f'The above PIN is of only {len(pin)}-digits')
            else:
                print(f"The above PIN is of {len(pin)}-digits, Please enter 6-digit PIN")
        print("Program Exiting")
