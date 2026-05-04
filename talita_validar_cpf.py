def validar_cpf(cpf):

    # Verifica se tem 11 caracteres
    contador = 0
    for c in cpf:
        contador += 1

    if contador != 11:
        return False

    # Verifica se todos os números são iguais
    igual = True
    for i in range(1, 11):
        if cpf[i] != cpf[0]:
            igual = False

    if igual:
        return False

    # 1º dígito
    soma = 0
    peso = 10

    for i in range(9):
        soma += int(cpf[i]) * peso
        peso -= 1

    resto = (soma * 10) % 11
    if resto == 10:
        resto = 0

    if resto != int(cpf[9]):
        return False

    # 2º dígito
    soma = 0
    peso = 11

    for i in range(10):
        soma += int(cpf[i]) * peso
        peso -= 1

    resto = (soma * 10) % 11
    if resto == 10:
        resto = 0

    if resto != int(cpf[10]):
        return False

    return True


cpf = input("Digite o CPF (somente números): ")

if validar_cpf(cpf):
    print("CPF válido!")
else:
    print("CPF inválido!")
