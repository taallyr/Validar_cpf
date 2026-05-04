# Importando o Tkinter pra criar a telinha do programa
import tkinter as tk
# Importando as caixinhas de aviso (pop-up)
from tkinter import messagebox

# Essa função é a responsável por verificar se o CPF é válido ou não
def validar_cpf(cpf):
    # Aqui a gente limpa o CPF (tira pontos e traços)
    cpf = cpf.replace(".", "").replace("-", "")
    
    # Primeiro teste:
    # Se não tiver 11 números OU se for tudo igual (tipo 11111111111), já é inválido
    if len(cpf) != 11 or cpf == cpf[0] * 11:
        return False

    # =========================
    # Verificando o 1º dígito
    # =========================
    soma = 0
    
    # Aqui fazemos uma conta com os 9 primeiros números
    # Cada número é multiplicado por um peso (de 10 até 2)
    for i in range(9):
        soma += int(cpf[i]) * (10 - i)
    
    # Agora fazemos o cálculo final
    resto = (soma * 10) % 11
    
    # Regra: se der 10, vira 0
    if resto == 10:
        resto = 0
    
    # Se o resultado não for igual ao dígito do CPF, já é inválido
    if resto != int(cpf[9]):
        return False

    # =========================
    # Verificando o 2º dígito
    # =========================
    soma = 0
    
    # Mesma lógica, mas agora usamos 10 números e pesos de 11 até 2
    for i in range(10):
        soma += int(cpf[i]) * (11 - i)
    
    resto = (soma * 10) % 11
    
    if resto == 10:
        resto = 0
    
    # Compara com o último número do CPF
    if resto != int(cpf[10]):
        return False

    # Se passou por tudo, então o CPF é válido
    return True


# Essa função roda quando o usuário clica no botão
def verificar():
    # Pega o que a pessoa digitou na caixinha
    cpf = entrada.get()
    
    # Chama a função que valida
    if validar_cpf(cpf):
        # Mostra uma mensagem de sucesso
        messagebox.showinfo("Resultado", "CPF válido!")
    else:
        # Mostra uma mensagem de erro
        messagebox.showerror("Resultado", "CPF inválido!")


# =========================
# Agora começa a parte da telinha (interface)
# =========================

# Criando a janela principal
janela = tk.Tk()

# Nome que aparece lá em cima da janela
janela.title("Validador de CPF")

# Tamanho da janela (largura x altura)
janela.geometry("300x150")

# Texto que aparece na tela
label = tk.Label(janela, text="Digite o CPF:")
label.pack(pady=10)  # Esse pady é só um espacinho

# Campo onde o usuário vai digitar o CPF
entrada = tk.Entry(janela)
entrada.pack()

# Botão que o usuário vai clicar pra validar
botao = tk.Button(janela, text="Validar", command=verificar)
botao.pack(pady=10)

# Isso aqui mantém a janela aberta rodando
janela.mainloop()