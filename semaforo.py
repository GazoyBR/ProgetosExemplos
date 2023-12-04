import tkinter as tk
import time

class Semaforo:
    def __init__(self, root):
        self.root = root
        self.root.title("Semaforo Simples")

        self.luz_vermelha = tk.Canvas(root, width=50, height=50, bg="white")
        self.luz_vermelha.create_oval(5, 5, 45, 45, fill="gray")
        self.luz_vermelha.grid(row=0, column=0, padx=10)

        self.luz_amarela = tk.Canvas(root, width=50, height=50, bg="white")
        self.luz_amarela.create_oval(5, 5, 45, 45, fill="gray")
        self.luz_amarela.grid(row=0, column=1, padx=10)

        self.luz_verde = tk.Canvas(root, width=50, height=50, bg="white")
        self.luz_verde.create_oval(5, 5, 45, 45, fill="gray")
        self.luz_verde.grid(row=0, column=2, padx=10)

        self.botao_iniciar = tk.Button(root, text="Iniciar", command=self.iniciar_semaforo)
        self.botao_iniciar.grid(row=1, column=0, columnspan=3, pady=10)

    def iniciar_semaforo(self):
        for _ in range(3):
            self.luz_vermelha.itemconfig(1, fill="red")
            self.root.update()
            time.sleep(2)

            self.luz_vermelha.itemconfig(1, fill="gray")
            self.luz_amarela.itemconfig(1, fill="yellow")
            self.root.update()
            time.sleep(1)

            self.luz_amarela.itemconfig(1, fill="gray")
            self.luz_verde.itemconfig(1, fill="green")
            self.root.update()
            time.sleep(2)

            self.luz_verde.itemconfig(1, fill="gray")

# Criar a janela principal
root = tk.Tk()
semaforo = Semaforo(root)

# Iniciar o loop de eventos
root.mainloop()
