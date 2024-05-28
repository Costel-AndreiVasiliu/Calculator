import tkinter as tk
from tkinter import messagebox


class Calculator:
    expression = " "

    # Constructor
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Calculator")
        self.root.geometry("300x520")
        self.root.configure(bg="#1051DC")
        self.root.resizable(False, False)
        self.root.propagate(False)

        self.frame = tk.Frame(self.root,
                              width="300",
                              height="175",
                              bg="#1051DC")
        self.frame.grid(row=0, column=0)

        self.str_var = tk.StringVar()
        self.text = tk.Entry(self.frame,
                             width=24,
                             bg="#7EA4F5",
                             font=("Arial", 16, "bold"),
                             fg="white",
                             justify=tk.RIGHT,
                             textvariable=self.str_var)
        self.text.grid(row=0, column=0, padx=4, pady=10, ipady=20, sticky=tk.W + tk.E,)

        self.clear = tk.Button(self.frame,
                               text="C",
                               font=("Arial", 16, "bold"),
                               bg="#8EAAE6",
                               activebackground="grey",
                               activeforeground="red",
                               command=self.clear_text)
        self.clear.grid(row=1, column=0, padx=4, pady=5, sticky=tk.W + tk.E)

        self.button_frame = tk.Frame(self.root,
                                     width=300,
                                     height=225,
                                     bg="#1051DC")
        self.button_frame.grid(row=1, column=0, padx=4, pady=3, sticky=tk.W + tk.E)

        self.numbers_grid()

        self.root.mainloop()

    # La apasarea butonului Clear (C) se sterge textul afisat
    def clear_text(self):
        Calculator.expression = " "
        self.str_var.set(Calculator.expression)

    # Afisarea valorii butonului apasat
    def btn_click(self, strng):
        if strng == "=":
            try:
                Calculator.expression = str(eval(Calculator.expression))
                self.str_var.set(Calculator.expression)
            except:
                messagebox.showwarning(title="Warning", message="Not a valid expression. Please use a valid one !")

        else:
            Calculator.expression += strng
            self.str_var.set(Calculator.expression)

    # Adaugarea butoanelor cu cifre si operatii
    def add_numbers(self, btn_number):
        btn = tk.Button(self.button_frame,
                        text=btn_number,
                        width=5,
                        height=3,
                        font=("Arial", 16),
                        bg="#8EAAE6",
                        fg="white",
                        command=lambda: self.btn_click(btn_number))
        return btn

    # Creaza zona de cifre + simboluri
    def numbers_grid(self):
        numbers = [
            ('7', '8', '9', '*'),
            ('4', '5', '6', '-'),
            ('1', '2', '3', '+'),
            ('/', '0', '%', '=')
        ]
        for i, item in enumerate(numbers):
            for j, char in enumerate(item):
                btn = self.add_numbers(char)
                btn.grid(row=i, column=j, padx=2, pady=2)


if __name__ == "__main__":
    Calculator()
