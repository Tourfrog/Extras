
import random


listaDeCliente = []

def adicionarCompras():
    podeContinuar = True
    # Inserindo Nome do Cliente
    while True:
        nome = str(input('Digite o nome do cliente: '))

        for letra in nome:
            if letra.isdigit():
                podeContinuar = False

        if podeContinuar == True:
            print('Nome OK!')
            break
        else: 
            print(f'Não aceitamos números no nome. Nós desculpem por favor, vossa Majestade {nome}.')
            podeContinuar = True

    # Inserindo CPF do Cliente
    checarCPF = []
    while True:
  
            cpf = str(input(f'Digite o cpf do cliente {nome}: '))
            for numeral in cpf:
                if numeral.isalpha():
                    podeContinuar = False
                    break
                elif numeral.isdigit():
                    checarCPF.append(numeral)

                # print(checarCPF)
                # print(len(checarCPF))
                # print(podeContinuar)
            if podeContinuar == True:
                if len(checarCPF) == 11:
                    print('CPF OK!')
                    break
                else:
                    print(f'O CPF tem 11 números, você colocou {len(checarCPF)}.')
                    checarCPF.clear()
            else:
                print('Não existe letra no CPF.')
                checarCPF.clear()
                podeContinuar = True    

    # Inserindo o ValorCompras do Cliente
    while True:
            try:
                valorCompras = float(input(f'Digite o valor da compra do cliente {nome}: '))

                cliente = {
                    'nome' : nome,
                    'cpf' : cpf,
                    'valorCompras': valorCompras
                }

                listaDeCliente.append(cliente)
                print('Cliente e compras adicionado com sucesso!')
                    
                break
            except:
                print('Ninguem paga compras com letra.')

    # print('Certificando se funcionou tudo.')
                        

def sortearVencedor():
    clienteSorteado = random.randrange(0, len(listaDeCliente))

    nomeVencedor = listaDeCliente[clienteSorteado]['nome']
    cpfVencedor = listaDeCliente[clienteSorteado]['cpf']
    valorComprasVencedor = listaDeCliente[clienteSorteado]['valorCompras']

    print(f'''
        Parabéns, {nomeVencedor}, cpf: {cpfVencedor},
        com sua compra no valor de {valorComprasVencedor},
        você foi o sorteado de hoje, venham recolher o seu premio.''')
    
    maiorCompra = 0
    nomeDoMaiorCliente = 'teste'
    for maiorCliente in listaDeCliente:
        if maiorCliente['valorCompras'] > maiorCompra:
            maiorCompra = maiorCliente['valorCompras']
            nomeDoMaiorCliente = maiorCliente['nome']

    print(f'Parabéns ao {nomeDoMaiorCliente}, por ter feito a maior compra de hoje.')
    
    

while True:
    try:
        menu = int(input('''
                    Menu
        1 - Adicionar compras
        2 - Ver lista de clientes                
        3 - Encerar compras e Sortear cliente
        Digite aqui a opção desejada -> '''))

        match menu:
            case 1:
                adicionarCompras()

            case 2:
                for cliente in listaDeCliente:
                    print(f'Nome: {cliente["nome"]} / CPF: {cliente["cpf"]} / Compras no valor R${cliente["valorCompras"]}.')

            case 3:
                if len(listaDeCliente) < 1:
                    print('Adicione clientes antes de sortear.')
                else:
                    encerrar = str(input('''
                                        Digite (s) se realmente deseja encerrar a venda e começar o sorteio,
                                        se ainda não terminou digite (n) para voltar a adicionar outras compras: '''))
                    match encerrar:
                        case 's':
                            sortearVencedor()
                            break
                        case 'n':
                            continue
                        case _:
                            print('Opção Invalida!')

            case _:
                print('Opção Invalida.')

    except ValueError:
        print('Digite apenas o numeral sugerido no Menu, (1 ou 2)!')

