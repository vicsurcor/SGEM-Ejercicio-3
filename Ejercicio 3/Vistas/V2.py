import tkinter as tk
from E3 import E5


class ventanaTuplas2(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Simple GUI")
        # Set initial size of the window
        self.geometry("600x400")

        # Create text fields as instance variables
        self.entry1 = tk.Entry(self, width=50)
        self.entry2 = tk.Entry(self)
        self.entry3 = tk.Entry(self)
        self.entry4 = tk.Text(self, height=10, width=50)
        self.entry5 = tk.Text(self, height=5, width=50)

        # Create buttons
        telegrama_button = tk.Button(self, text="Calcula el coste del telegrama", command=self.telegrama)

        # Grid layout
        self.entry1.grid(row=0, column=1, sticky="nsew")
        self.entry2.grid(row=1, column=1, sticky="nsew")
        self.entry3.grid(row=2, column=1, sticky="nsew")
        self.entry4.grid(row=7, column=1, sticky="nsew")
        self.entry5.grid(row=8, column=1, sticky="nsew")

        telegrama_button.grid(row=4, column=0, columnspan=2, pady=10, sticky="nsew")

        # Labels
        tk.Label(self, text="Texto: ").grid(row=0, column=0, sticky="w")  # Align left
        tk.Label(self, text="Coste palabra corta: ").grid(row=1, column=0, sticky="w")  # Align left
        tk.Label(self, text="Coste palabra larga: ").grid(row=2, column=0, sticky="w")  # Align left
        tk.Label(self, text="Resultado: ").grid(row=7, column=0, sticky="w")

    def telegrama(self):

        if self.entry1.get() == "":
            self.entry1.insert(tk.END, "")
        if self.entry2.get() == "":
            self.entry2.insert(tk.END, "0")
        if self.entry3.get() == "":
            self.entry3.insert(tk.END, "0")

        data1 = (self.entry1.get())
        data2 = float(self.entry2.get())
        data3 = float(self.entry3.get())
        result = E5.telegrama(data1, data2, data3)
        self.entry4.delete(1.0, tk.END)
        self.entry4.insert(tk.END, result[0])
        self.entry5.delete(1.0, tk.END)
        self.entry5.insert(tk.END, result[1])


# Create an instance of the ventanaTuplas class
app = ventanaTuplas2()
# Run the application
app.mainloop()
