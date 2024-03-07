import tkinter as tk
from E3 import E1

class ventanaTuplas(tk.Tk):
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

        # Create buttons
        segundos_button = tk.Button(self, text="Pasar a segundos", command=self.calcSeg)
        hms_button = tk.Button(self, text="Pasar a horas, minutos y segundos", command=self.calcHMS)
        coste_button = tk.Button(self, text="Calcular coste", command=self.calcCoste)

        # Grid layout
        self.entry1.grid(row=0, column=1, sticky="nsew")
        self.entry2.grid(row=1, column=1, sticky="nsew")
        self.entry3.grid(row=2, column=1, sticky="nsew")
        self.entry4.grid(row=7, column=1, sticky="nsew")

        segundos_button.grid(row=4, column=0, columnspan=2, pady=10, sticky="nsew")
        hms_button.grid(row=5, column=0, columnspan=2, pady=10, sticky="nsew")
        coste_button.grid(row=6, column=0, columnspan=2, pady=10, sticky="nsew")

        # Labels
        tk.Label(self, text="Horas: ").grid(row=0, column=0, sticky="w")  # Align left
        tk.Label(self, text="Minutos: ").grid(row=1, column=0, sticky="w")  # Align left
        tk.Label(self, text="Segundos: ").grid(row=2, column=0, sticky="w")  # Align left
        tk.Label(self, text="Resultado: ").grid(row=7, column=0, sticky="w")

    def calcSeg(self):
        # Function to handle submitting data from text fields
        if self.entry1.get() == "":
            self.entry1.insert(tk.END, "0")
        if self.entry2.get() == "":
            self.entry2.insert(tk.END, "0")
        if self.entry3.get() == "":
            self.entry3.insert(tk.END, "0")

        data1 = int(self.entry1.get())
        data2 = int(self.entry2.get())
        data3 = int(self.entry3.get())
        result = E1.segundos(data1, data2, data3)
        self.entry4.delete(1.0, tk.END)
        self.entry4.insert(tk.END, result)

    def calcHMS(self):
        if self.entry3.get() == "":
            self.entry3.insert(tk.END, "0")
        data3 = int(self.entry3.get())
        result = E1.horas(data3)
        self.entry4.delete(1.0, tk.END)
        self.entry4.insert(tk.END, result)


    def calcCoste(self):
        if self.entry1.get() == "":
            self.entry1.insert(tk.END, "0")
        if self.entry2.get() == "":
            self.entry2.insert(tk.END, "0")
        if self.entry3.get() == "":
            self.entry3.insert(tk.END, "0")

        data1 = int(self.entry1.get())
        data2 = int(self.entry2.get())
        data3 = int(self.entry3.get())
        result = E1.segundos(data1, data2, data3)
        result = E1.importeLlamada(result)
        self.entry4.delete(1.0, tk.END)
        self.entry4.insert(tk.END, result)


# Create an instance of the ventanaTuplas class
app = ventanaTuplas()
# Run the application
app.mainloop()

