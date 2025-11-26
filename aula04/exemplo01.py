# informar se é maior de idade
# idade = int(input('informe sua idade: '))

# if idade >= 18:
#     print('voce é maior de idade')
# else:
#     print('voce é menor de idade')

# testando com mais condiçoes
# teste de pontos

# pontos = int(input('Quantos pontos? '))
# if pontos >= 100:
#     print('Pontuação Maxima!')
# elif pontos >= 50:
#     print('Pontuação Boa!')
# elif pontos >= 25:
#     print('Pontuação Ruim.')
# else:
#     print('Pontuação Baixa.')

# verificação de login
# usuario = input('Informe o usuario: ').lower()
# senha = input('Digite a senha: ')
# print(usuario)

# if usuario == 'admin' and senha == '1234':
#     print('Login efetuado com sucesso!')
# else:
#     print('Usuario ou/e senha incorretos')

# Condição para brinde

# compra = float(input('Qual o valor da compra?: '))
# cliente_frequente = input('Cliente frequente? [S/N]: ').lower()

# if compra >= 1000 or cliente_frequente == 's':
#     print('Tem brinde!')
# else:
#     print('Sem brinde.')

# Aprovação por nota ou frequência

nota = float(input('Informe a sua nota: '))
frequencia = float(input('Informe a sua frequencia: '))

if nota >= 7:
    if frequencia >= 75:
        print('APROVADO')
    else:
        print('REPROVADO POR FALTA')
else:
    print('REPROVADO POR NOTA')
