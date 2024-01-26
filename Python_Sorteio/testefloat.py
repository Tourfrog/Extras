valorCompras = float(input(f'Digite o valor da compra do cliente: '))

if valorCompras == round(valorCompras, 2):
    print(valorCompras, 'deu certo')
else: 
    print('deu errado')