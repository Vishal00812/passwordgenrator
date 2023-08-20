import string
import tkinter as tk
from tkinter import ttk
import random
from tkinter.constants import DISABLED, E, END, NORMAL, NW, VERTICAL


class GUI(tk.Frame):

    def __init__(self, master):
        super().__init__(master)
        self.pack()
        self.widget_vars()
        self.create_widgets()
        self.style()

    def generate_password(self):
        passw = Password(self.length.get(), self.lower.get(), self.upper.get(),
                         self.digits.get(), self.punct.get())
        # You can only insert to Text if the state is NORMAL
        self.password_text.config(state=NORMAL)
        self.password_text.delete("1.0", END)   # Clears out password_text
        self.password_text.insert(END, passw.password)
        self.password_text.config(state=DISABLED)

    def widget_vars(self):
        self.length = tk.IntVar(self, value=16)
        self.lower = tk.BooleanVar(self, value=True)
        self.upper = tk.BooleanVar(self, value=True)
        self.digits = tk.BooleanVar(self, value=True)
        self.punct = tk.BooleanVar(self, value=True)

    def create_widgets(self):
        # Define widgets
        self.lower_checkbtn = ttk.Checkbutton(self, variable=self.lower)
        self.lower_label = ttk.Label(self, text="string.ascii_lower")
        self.upper_checkbtn = ttk.Checkbutton(self, variable=self.upper)
        self.upper_label = ttk.Label(self, text="string.ascii_upper")
        self.digits_checkbtn = ttk.Checkbutton(self, variable=self.digits)
        self.digits_label = ttk.Label(self, text="string.digits")
        self.punct_checkbtn = ttk.Checkbutton(self, variable=self.punct)
        self.punct_label = ttk.Label(self, text="string.punctuation")
        self.length_spinbox = ttk.Spinbox(self, from_=1, to=128, width=3,
                                          textvariable=self.length)
        self.length_label = ttk.Label(self, text="Password length")
        self.separator = ttk.Separator(self, orient=VERTICAL)
        self.generate_btn = ttk.Button(self, text="Generate password",
                                       command=self.generate_password)
        self.password_text = tk.Text(self, height=4, width=32, state=DISABLED)

        # Place widgets on the screen
        self.length_label.grid(column=0, row=0, rowspan=4, sticky=E)
        self.length_spinbox.grid(column=1, row=0, rowspan=4, padx=4, pady=2)
        self.lower_label.grid(column=3, row=0, sticky=E, padx=4)
        self.lower_checkbtn.grid(column=4, row=0, padx=4, pady=2)
        self.upper_label.grid(column=3, row=1, sticky=E, padx=4)
        self.upper_checkbtn.grid(column=4, row=1, padx=4, pady=2)
        self.digits_label.grid(column=3, row=2, sticky=E, padx=4)
        self.digits_checkbtn.grid(column=4, row=2, padx=4, pady=2)
        self.punct_label.grid(column=3, row=3, sticky=E, padx=4)
        self.punct_checkbtn.grid(column=4, row=3, padx=4, pady=2)
        self.separator.grid(column=2, row=0, rowspan=4, ipady=45)
        self.generate_btn.grid(columnspan=5, row=4, padx=4, pady=2)
        self.password_text.grid(columnspan=5, row=6, padx=4, pady=2)

        self.grid(padx=10, pady=10)

    def style(self):
        self.style = ttk.Style(self)
        self.style.theme_use("clam")


class Password:

    def __init__(self, length: int,
                 allow_lowercase: bool,
                 allow_uppercase: bool,
                 allow_digits: bool,
                 allow_punctuation: bool) -> None:
        self.length = length
        self.allow_lowercase = allow_lowercase
        self.allow_uppercase = allow_uppercase
        self.allow_digits = allow_digits
        self.allow_punctuation = allow_punctuation
        self.allowed_chars = self.gen_allowed_chars()
        self.password = self.gen_password()

    def gen_allowed_chars(self) -> str:
        chars = ''
        if self.allow_lowercase:
            chars += string.ascii_lowercase
        if self.allow_uppercase:
            chars += string.ascii_uppercase
        if self.allow_digits:
            chars += string.digits
        if self.allow_punctuation:
            chars += string.punctuation
        return chars

    def gen_password(self) -> str:
        password = ''
        for _ in range(self.length):
            password += random.choice(self.allowed_chars)
        return password


if __name__ == '__main__':
    root = tk.Tk()
    root.title("Password Generator")
    app = GUI(root)
    app.mainloop()
