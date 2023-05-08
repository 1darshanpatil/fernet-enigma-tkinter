modu = ['tkinter', 'cryptography', 'pyperclip']

import tkinter as tk
import cryptography
import pyperclip
from tkinter import messagebox


class SecurityWindow:
    def __init__(self, cipher_machine: object, Encryptor: object) -> object:
        self.Encryptor = Encryptor
        self.cipher_machine = cipher_machine
        self.root = tk.Tk()
        self.root.title("Security Window")
        self.root.configure(background="#f2f2f2")
        self.xyz = tk.StringVar()
        # Set window dimensions
        window_width = self.root.winfo_screenwidth() * 0.53
        window_height = self.root.winfo_screenheight() * 0.5
        self.root.geometry(f"{int(window_width)}x{int(window_height)}")

        # Create window header
        self.header_frame = tk.Frame(self.root, bg="#2962FF")
        self.header_frame.pack(fill=tk.X)

        self.header_label = tk.Label(self.header_frame, text="Security Window", fg="#fff", bg="#2962FF",
                                     font=("Arial", 20, "bold"))
        self.header_label.pack(padx=20, pady=10)

        # Create window content
        self.content_frame = tk.Frame(self.root, bg="#f2f2f2")
        self.content_frame.pack(padx=20, pady=20, fill=tk.BOTH, expand=True)

        self.entry_frame = tk.Frame(self.content_frame, bg="#f2f2f2")
        self.entry_frame.pack(pady=20)

        self.password_label = tk.Label(self.entry_frame, text="Enter your secret text", font=("Arial", 16),
                                       bg="#f2f2f2")
        self.password_label.pack(pady=10)

        font = ("DejaVu Sans Mono", 14)
        self.password_entry = tk.Entry(self.entry_frame, width=70, bd=1, bg="white", fg="black", font=font,
                                       highlightthickness=1)
        self.password_entry.pack(fill=tk.X, padx=10)

        self.label_frame = tk.Frame(self.content_frame, bg="#f2f2f2")
        self.label_frame.pack(pady=10)

        self.pin_label = tk.Label(self.label_frame, text="Enter your 6-digit PIN:", font=("Arial", 16), bg="#f2f2f2")
        self.pin_label.pack(pady=10)

        self.pin_entry = tk.Entry(self.label_frame, show='*', width=70, bd=1, bg="white", fg="black", font=font,
                                  textvariable=self.xyz,
                                  highlightthickness=1)
        self.pin_entry.pack(fill=tk.X, padx=10)

        self.secret_key_label = tk.Label(self.label_frame, text="Enter your 64-character secret key:",
                                         font=("Arial", 16), bg="#f2f2f2")
        self.secret_key_label.pack(pady=10)

        self.secret_key_entry = tk.Entry(self.label_frame, show='*', width=70, bd=1, bg="white", fg="black", font=font,
                                         highlightthickness=1)
        self.secret_key_entry.pack(fill=tk.X, padx=10)

        self.button_frame = tk.Frame(self.content_frame, bg="#f2f2f2")
        self.button_frame.pack(pady=20)

        self.encrypt_button = tk.Button(self.button_frame, text="Encrypt", bg="#4CAF50", fg="#fff", font=("Arial", 16),
                                        command=self.passE)

        self.encrypt_button.pack(side=tk.LEFT, padx=10)

        self.decrypt_button = tk.Button(self.button_frame, text="Decrypt", bg="#F44336", fg="#fff", font=("Arial", 16),
                                        command=self.passD)

        self.decrypt_button.pack(side=tk.LEFT, padx=10)

        self.generate_button = tk.Button(self.button_frame, text="Generate Secret key", bg="#FFC107", fg="#fff",
                                         font=("Arial", 16), command=self.passG)

        self.generate_button.pack(side=tk.LEFT, padx=10)

        self.root.mainloop()

    def pass_pin(self):
        if len(self.xyz.get()) != 6 or self.xyz.get().isdigit() == False:
            messagebox.showerror(title="Error", message="Please enter a 6-digit PIN that contains only numbers")
            self.xyz.set("")
        if len(self.xyz.get()) == 6 and self.xyz.get().isdigit() == True:
            self.Encryptor.get_pin(self.xyz.get())
            return "PIN-OKAY"

    def passD(self):
        if self.pass_pin() == "PIN-OKAY":
            if self.password_entry.get() != "":
                try:
                    egg1 = self.cipher_machine.decrypt_text(self.secret_key_entry.get(), self.password_entry.get())
                    passwordD = self.Encryptor.decrypt_password(egg1)
                    messagebox.showinfo(title="Decrypted Text", message=f"Your decrypted text is: \n{passwordD} \n")

                    if messagebox.askyesno(title="Copying", message="Do you want to copy the decrypted text to your "):
                        pyperclip.copy(passwordD)
                except cryptography.fernet.InvalidToken:
                    messagebox.showerror(title="Error", message="Please enter a valid secret key")
                    self.password_entry.delete(0, tk.END)
            else:
                messagebox.showerror(title="Error", message="Please enter a secret text")
                self.password_entry.delete(0, tk.END)

    def passE(self):
        if self.pass_pin() == "PIN-OKAY":
            if self.password_entry.get() != "":
                try:
                    passwordE = self.Encryptor.encrypt_password(self.password_entry.get())
                    syfr = self.cipher_machine.encrypt_text(self.secret_key_entry.get(), passwordE)
                    messagebox.showinfo(title="Encryption Result", message=f"Your cipher text is: \n{syfr.decode()} \n")

                    if messagebox.askyesno(title="Copying", message="Do you want to copy the cipher text to your "
                                                                    "clipboard?"):
                        pyperclip.copy(syfr.decode())
                except ValueError:
                    messagebox.showerror(title="Error", message="Please check your secret key")
                    self.secret_key_entry.delete(0, tk.END)
            else:
                messagebox.showerror(title="Error", message="Please enter a secret text")
                self.password_entry.delete(0, tk.END)

    def passG(self):
        if self.secret_key_entry.get() != "":
            ask_for_new = messagebox.askyesno(title="Secret Key", message="You have already entered a secret key.\n"
                                                                          "Are you sure you want to generate a new "
                                                                          "secret key?")
            if ask_for_new:
                genK = self.cipher_machine.get_key()
                ask_conformation = messagebox.askyesno(title="Secret Key",
                                                       message=f"Your secret key is: {genK.decode()}\nDo "
                                                               f"you want to copy the secret key?")
                if ask_conformation:
                    messagebox.showinfo(title="Secret Key", message="Your secret key has been copied to your "
                                                                    "clipboard and "
                                                                    "also entered into the secret key entry box.\n"
                                                                    "Please make sure to save this secret key before "
                                                                    "you start using it.")
                    self.secret_key_entry.delete(0, tk.END)
                    self.secret_key_entry.insert(0, genK.decode())
                    pyperclip.copy(genK.decode())
        else:
            genK = self.cipher_machine.get_key()
            ask_conformation = messagebox.askyesno(title="Secret Key",
                                                   message=f"Your secret key is: {genK.decode()}\nDo "
                                                           f"you want to copy the secret key?")
            if ask_conformation:
                messagebox.showinfo(title="Secret Key", message="Your secret key has been copied to your "
                                                                "clipboard and "
                                                                "also entered into the secret key entry box.\n"
                                                                "Please make sure to save this secret key before you "
                                                                "start using it.")
                self.secret_key_entry.delete(0, tk.END)
                self.secret_key_entry.insert(0, genK.decode())
                pyperclip.copy(genK.decode())
