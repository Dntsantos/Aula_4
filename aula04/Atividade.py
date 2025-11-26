# atividade

valor = float(input('Qual o valor da compra? '))

if valor > 250.00 :
    porcento = 0.16 * valor
    total = valor - porcento
    print(f'O valor com desconto é: {total} ')
elif valor < 250.00:
    print(f'O valor final é: {valor}')