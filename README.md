# fernet-enigma-tkinter# Security Window Application

This is a Python GUI application that allows you to encrypt and decrypt text using a 32-character secret key and a 6-digit PIN. The application is built using the `tkinter` library for the graphical user interface, the `cryptography` library for encryption and decryption, and the `pyperclip` library for copying the decrypted text to the clipboard.

## Installation

To run the application, you need to have Python 3 and the following libraries installed:

- tkinter
- cryptography
- pyperclip

You can install the libraries using `pip`:


## Usage

To use the application, run the `security_window.py` file. The application will open a window with the following fields:

- **Secret Text:** Enter the text you want to encrypt or decrypt.
- **6-digit PIN:** Enter a 6-digit PIN to use for encryption and decryption.
- **32-character Secret Key:** Enter a 32-character secret key to use for encryption and decryption.
- **Encrypt:** Click this button to encrypt the text.
- **Decrypt:** Click this button to decrypt the text.
- **Generate Secret Key:** Click this button to generate a random 32-character secret key.

When you click the **Encrypt** button, the application will encrypt the text using the secret key and PIN you entered. When you click the **Decrypt** button, the application will decrypt the text using the secret key and PIN you entered. The decrypted text will be displayed in a message box and copied to the clipboard.

## Contributing

Contributions to this project are welcome. If you find a bug or have a feature request, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
