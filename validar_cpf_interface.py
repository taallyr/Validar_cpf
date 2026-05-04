import tkinter as tk
from tkinter import messagebox

def validar_cpf(cpf):
    cpf = cpf.replace(".", "").replace("-", "")
    
    if len(cpf) != 11 or cpf == cpf[0] * 11:
        return False

    soma = 0
    for i in range(9):
        soma += int(cpf[i]) * (10 - i)
    resto = (soma * 10) % 11
    if resto == 10:
        resto = 0
    if resto != int(cpf[9]):
        return False

    soma = 0
    for i in range(10):
        soma += int(cpf[i]) * (11 - i)
    resto = (soma * 10) % 11
    if resto == 10:
        resto = 0
    if resto != int(cpf[10]):
        return False

    return True

def verificar():
    cpf = entrada.get()
    if validar_cpf(cpf):
        messagebox.showinfo("Resultado", "CPF válido!")
    else:
        messagebox.showerror("Resultado", "CPF inválido!")

# Janela
janela = tk.Tk()
janela.title("Validador de CPF")
janela.geometry("300x150")

label = tk.Label(janela, text="Digite o CPF:")
label.pack(pady=10)

entrada = tk.Entry(janela)
entrada.pack()

botao = tk.Button(janela, text="Validar", command=verificar)
botao.pack(pady=10)

janela.mainloop()