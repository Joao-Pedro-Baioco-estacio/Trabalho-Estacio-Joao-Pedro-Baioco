import tkinter as tk
from tkinter import filedialog

def escolher_pdf():
    caminho = filedialog.askopenfilename(filetypes=[("Arquivos PDF", "*.pdf")])
    if caminho:
        print(f"Arquivo selecionado: {caminho}")

# Interface principal
janela = tk.Tk()
janela.title("Verificador de Feriados")
janela.geometry("300x200")
janela.resizable(False, False)

titulo = tk.Label(janela, text="Escolha um arquivo PDF com datas", font=("Arial", 11))
titulo.pack(pady=20)

botao = tk.Button(janela, text="Selecionar PDF", command=escolher_pdf)
botao.pack(pady=10)

janela.mainloop()
