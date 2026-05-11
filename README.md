# 🆔 Validar CPF

Um projeto em Python para validar números de CPF (Cadastro de Pessoa Física) de acordo com as regras oficiais da Receita Federal do Brasil.

## 📋 Descrição

Este repositório contém uma solução para validar CPF com verificação completa de dígitos verificadores e detecção de CPFs inválidos ou sequências conhecidas. Ideal para integração em sistemas que precisam validar dados de contribuintes brasileiros.

## 🎯 Objetivo

- Validar CPF de forma correta e segura
- Verificar dígitos verificadores
- Detectar CPFs inválidos e sequências
- Fornecer feedback claro sobre validação
- Facilitar integração em aplicações Python

## 🛠️ Tecnologias

- **Linguagem**: Python 3.x
- **Tipo**: Validação de Dados
- **Propósito**: Educacional e Prático

## 📁 Estrutura do Repositório

```
Validar_cpf/
├── README.md
├── validar_cpf.py
└── teste_cpf.py
```

## 🚀 Como Usar

1. Clone o repositório:
```bash
git clone https://github.com/taallyr/Validar_cpf.git
cd Validar_cpf
```

2. Execute o validador:
```bash
python validar_cpf.py
```

3. Ou importe em seu projeto:
```python
from validar_cpf import validar_cpf

resultado = validar_cpf("12345678909")
print(resultado)  # True ou False
```

## 💡 Funcionalidades

- ✅ Validação de dígitos verificadores
- ✅ Detecção de sequências inválidas (ex: 111.111.111-11)
- ✅ Suporte para CPF com ou sem formatação
- ✅ Mensagens de erro descritivas
- ✅ Tratamento de entrada inválida

## 📊 Como Funciona

A validação de CPF segue o algoritmo oficial:

1. **Primeiro dígito verificador**: Multiplica-se os primeiros 9 dígitos por 10, 9, 8, ..., 2 e soma-se os resultados
2. **Segundo dígito verificador**: Multiplica-se os 10 primeiros dígitos (incluindo o primeiro verificador) por 11, 10, 9, ..., 2 e soma-se
3. **Validação final**: Ambos os dígitos devem corresponder aos últimos 2 dígitos do CPF

### Exemplo:
```
CPF: 123.456.789-09
Primeiros 9 dígitos: 1 2 3 4 5 6 7 8 9
Multiplicadores:    10 9 8 7 6 5 4 3 2
Soma: (1×10) + (2×9) + (3×8) + ... = resultado
```

## 📝 Formato Esperado

O projeto aceita CPF nos seguintes formatos:
- Com formatação: `123.456.789-09`
- Sem formatação: `12345678909`

## 🧪 Testes

Execute os testes inclusos:
```bash
python teste_cpf.py
```

Exemplos de CPF:
- ❌ Inválidos: `111.111.111-11`, `000.000.000-00`, `123.456.789-00`
- ✅ Válidos: (gere com CPF válidos reais para testes)

## 🤝 Contribuições

Sugestões de melhorias e correções são bem-vindas! Sinta-se à vontade para:
- Abrir issues reportando bugs
- Fazer pull requests com melhorias
- Sugerir novas funcionalidades

## 📝 Licença

Este projeto está disponível sob a licença MIT.

## ⚠️ Aviso Legal

Este projeto é apenas para fins educacionais e de validação de formato. Para transações financeiras ou dados sensíveis, utilize bibliotecas certificadas e validações de segurança adicional.

---

**Autor**: [taallyr](https://github.com/taallyr)  
**Criado em**: 2026  
**Último atualizado**: Maio de 2026
