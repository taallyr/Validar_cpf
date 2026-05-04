def validar_cpf(cpf):
    
    # Criar um contador para saber quantos caracteres o CPF tem
    contador = 0
    
    # Percorrer cada caractere do CPF
    for c in cpf:
        contador += 1  # soma 1 a cada caractere encontrado

    # Verificar se tem exatamente 11 caracteres
    if contador != 11:
        return False  # se não tiver, CPF é inválido

    # Verificar se todos os números são iguais (ex: 11111111111)
    igual = True  # começa assumindo que todos são iguais

    # Comparar cada número com o primeiro
    for i in range(1, 11):
        if cpf[i] != cpf[0]:
            igual = False  # encontrou um diferente

    # Se todos forem iguais, CPF inválido
    if igual:
        return False

    # =========================
    # CÁLCULO DO 1º DÍGITO
    # =========================

    soma = 0   # variável para guardar a soma
    peso = 10  # peso começa em 10

    # Percorre os 9 primeiros números do CPF
    for i in range(9):
        # Converte o caractere para número e multiplica pelo peso
        soma += int(cpf[i]) * peso
        peso -= 1  # diminui o peso (10, 9, 8...)

    # Calcula o resto da divisão
    resto = (soma * 10) % 11

    # Se o resto for 10, vira 0 (regra do CPF)
    if resto == 10:
        resto = 0

    # Verifica se o resultado é igual ao 10º dígito do CPF
    if resto != int(cpf[9]):
        return False  # se não for igual, CPF inválido

    # =========================
    # CÁLCULO DO 2º DÍGITO
    # =========================

    soma = 0   # zera a soma
    peso = 11  # peso começa em 11

    # Percorre os 10 primeiros números do CPF
    for i in range(10):
        soma += int(cpf[i]) * peso
        peso -= 1  # diminui o peso

    # Calcula o resto novamente
    resto = (soma * 10) % 11

    # Ajuste se for 10
    if resto == 10:
        resto = 0

    # Verifica com o último dígito do CPF
    if resto != int(cpf[10]):
        return False  # se não bater, inválido

    # Se passou por todas as verificações
    return True


# =========================
# PROGRAMA PRINCIPAL
# =========================

# Pedir o CPF para o usuário (somente números)
cpf = input("Digite o CPF (somente números): ")

# Chamar a função para validar o CPF
if validar_cpf(cpf):
    print("CPF válido!")  # mensagem se for válido
else:
    print("CPF inválido!")  # mensagem se for inválido