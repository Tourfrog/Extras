

listasDeTarefas = []

# listasDeTarefas=[{
#     'nome' = 'Emy',
#     'descrição' = 'apagar o fogo com alcool',
#     'prioridade' = 'alta',
#     'categoria' = 'domestica',
#     'concluida' = False,
# }]

def tarefaFeita():
    quemFez = str(input('Digite o nome de quem terminou a tarefa: '))
    qualTarefa = str(input('Qual foi a tarefa concluida: '))

    for tarefa in listasDeTarefas:
        if tarefa['nome'] == quemFez:
            if tarefa['descrição'] == qualTarefa:
                tarefa['concluida'] = True
        
    # for tarefa in listasDeTarefas:
    #     for nome in tarefa:
    #         if nome['nome'] == quemFez:
    #             if nome['descrição'] == qualTarefa:
    #                 nome['concluida'] = True
    #         else:
    #             print('Esta pessoa não está na lista')
            
        


def mostrarPorCategoria():
    for tipoDeCategoria in listasDeTarefas:
        print(tipoDeCategoria['categoria'])
            
    mostrarPorCategorias = str(input('Digite a categoria, para ver as tarefas dessa categoria: '))

    
    for tarefaCategoria in listasDeTarefas:
        if tarefaCategoria['categoria'] == mostrarPorCategorias:
            print(tarefaCategoria)
        else:
            print('Não existe tarefa nesta categoria')


def mostrarPorPrioridade():
    tipoDePrioridade = str(input('Temos de tarefas de (alta) e (baixa) prioridade, qual quer ver: ')).lower()

    for tarefaPrioridade in listasDeTarefas:
        if tarefaPrioridade['prioridade'] == tipoDePrioridade:
            print(tarefaPrioridade)


def mostrarTarefasConcluida():
        for tarefaConcluida in listasDeTarefas:
            if tarefaConcluida['concluida'] == True:
                print(tarefaConcluida)

while True:
    action = int(input('''
        Menu, digite o numero para fazer a ação que tu deseja:

        1 - Adicionar tarefas
        2 - Mostrar todas as tarefas
        3 - Marcar tarefas que foram concluidas
        4 - Exibir as tarefas por categorias
        5 - Exibir tarefas por prioridade
        6 - Mostrar tarefas concluidas
        0 - Desligar
        digite aqui => '''))
    

    tarefa = []
    match action:
        case 1:
            nome = str(input('Digite o nome de quem vai fazer a tarefa: '))
            descricao = str(input('Digite qual é a tarefa a ser feita: '))
            categoria = str(input('Qual é a categoria da tarefa: ')).lower()
            while True:
                prioridade = str(input('Qual é a prioridade da tarefa, digite se é alta ou baixa: ')).lower()
                if prioridade == 'alta':
                    break
                elif prioridade == 'baixa':
                    break
                else:
                    print('Escreva apenas (alta) ou (baixa) para descrever a prioridade das tarefas.')

            
            tarefa = {
                'nome': nome,
                'descrição' : descricao,
                'categoria' : categoria,
                'prioridade' : prioridade,
                'concluida' : False
            }

            listasDeTarefas.append(tarefa)
            
        case 2: 
            if len(listasDeTarefas) < 1:
                print('Não tem tarefas na lista, coloque as tarefas na lista usando a opção 1.')
            else:
                for tarefa in listasDeTarefas:
                   print(tarefa)
        
        case 3:
            if len(listasDeTarefas) < 1:
                print('Não tem tarefas na lista, coloque as tarefas na lista usando a opção 1.')
            else:
                tarefaFeita()

        case 4:
            if len(listasDeTarefas) < 1:
                print('Não tem tarefas na lista, coloque as tarefas na lista usando a opção 1.')
            else:
                mostrarPorCategoria()

        case 5:
            if len(listasDeTarefas) < 1:
                print('Não tem tarefas na lista, coloque as tarefas na lista usando a opção 1.')
            else:
                mostrarPorPrioridade()
                    
        case 6:
            if len(listasDeTarefas) < 1:
                print('Não tem tarefas na lista, coloque as tarefas na lista usando a opção 1.')
            else:
                mostrarTarefasConcluida()

        case 0:
            print('Programa Encerrado.')
            break

        case _:
            print('Escolha apenas os numeros mostrados no Menu.')
            

                
                

    


            
