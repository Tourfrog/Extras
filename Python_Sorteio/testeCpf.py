checarCPF = []
       
podeContinuar = True
while True:
    cpf = str(input(f'Digite o cpf do cliente: '))
    for numeral in cpf:
        if numeral.isalpha():
            podeContinuar = False
        if numeral.isdigit():
            checarCPF.append(numeral)
        print(checarCPF)
        print(len(checarCPF))
        print(podeContinuar)