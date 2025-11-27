# atividade

# valor = float(input('Qual o valor da compra? '))

# if valor > 250.00 :
#     porcento = 0.16 * valor
#     total = valor - porcento
#     print(f'O valor com desconto é: {total} ')
# elif valor < 250.00:
#     print(f'O valor final é: {valor}')

disponivel = int(input("digite a quantidade disponivel: "))
solicitada = int(input('digite a quantidade solicitada: '))
peso = float(input('digite o peso do pedido: '))

if solicitada <= disponivel and peso <= 50:
    print('O pedido sera enviado em breve')
else:
    print('o pedido nao pode ser enviado')
