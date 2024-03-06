

from tkinter import ttk
from tkinter.ttk import *
from tkinter import *

janela = Tk()

janela.title('Academia de Esportes')
janela.geometry('500x500')

titulo = Label(janela, text='Registro de Aluno', font='Arial' 'bold')
titulo.pack()

class Aluno:
    def __init__(self,id:int, nome:str, idade:int, modalidade:str) -> None:
        self.alunoID = id
        self.alunoNome = nome
        self.alunoIdade = idade
        self.alunoModalidade = modalidade

# Lista para guardar alunos
listaDeAlunos = []

contadorParaID = 1
# Funções
def siteMainFrame (): 
    global mainFrame
    mainFrame = Frame(janela)
    mainFrame.pack(padx=5, pady=5)

    btoSiteCadastroDeAluno = Button(mainFrame, text='Para Cadastrar Aluno', command=siteCadastroDeAluno)
    btoSiteCadastroDeAluno.pack()

    btoSiteAtualizarAluno = Button(mainFrame, text='Para atualização de Aluno', command=siteAtualizarAluno)
    btoSiteAtualizarAluno.pack()

    btoVerListaDeAluno = Button(mainFrame, text='Ver Lista de Aluno', command=siteVerListaDeAluno)
    btoVerListaDeAluno.pack()

    btoSiteExcluirAluno = Button(mainFrame, text='Para excluir aluno', command=siteExcluirAluno)
    btoSiteExcluirAluno.pack()

    btoDestroy = Button(mainFrame, text='Sair', command=janela.destroy)
    btoDestroy.pack(side='bottom')

def siteCadastroDeAluno():
    global mainFrame
    if mainFrame:
        mainFrame.destroy()

    siteCadastrarFrame = Frame(janela)
    siteCadastrarFrame.pack()

    titulo_Nome = Label(siteCadastrarFrame, text='Nome')
    titulo_Nome.pack()
    input_Nome = Entry(siteCadastrarFrame)
    input_Nome.pack()
    
    titulo_Idade = Label(siteCadastrarFrame, text='Idade')
    titulo_Idade.pack()
    input_Idade = Entry(siteCadastrarFrame)
    input_Idade.pack()

    modalidadeFrame = Frame(siteCadastrarFrame)
    modalidadeFrame.pack()

    modRadioButtonValue = IntVar()

    mod_Natacao = Radiobutton(modalidadeFrame, text='Natação', variable=modRadioButtonValue, value=0, pady=10, padx=10)
    mod_Natacao.grid(column=0, row=0)
    mod_Musculacao = Radiobutton(modalidadeFrame, text='Musculação', variable=modRadioButtonValue, value=1, pady=10, padx=10)
    mod_Musculacao.grid(column=0, row=1)
    mod_Pilates = Radiobutton(modalidadeFrame, text='Pilates', variable=modRadioButtonValue, value=2, pady=10, padx=10)
    mod_Pilates.grid(column=0, row=2)
    mod_Capoeira = Radiobutton(modalidadeFrame, text='Capoeira', variable=modRadioButtonValue, value=3, pady=10, padx=10)
    mod_Capoeira.grid(column=1, row=0)
    mod_Boxe = Radiobutton(modalidadeFrame, text='Boxe', variable=modRadioButtonValue, value=4, pady=10, padx=10)
    mod_Boxe.grid(column=1, row=1)
    mod_Volei = Radiobutton(modalidadeFrame, text='Vôlei', variable=modRadioButtonValue, value=5, pady=10, padx=10)
    mod_Volei.grid(column=1, row=2)

    def cadastrarAluno():
        
        nomeAluno = str(input_Nome.get())
        idadeAluno = str(input_Idade.get())
        valorModalidade = modRadioButtonValue.get()

        podeContinuar = True
        for aluno in listaDeAlunos:
            if nomeAluno == aluno.alunoNome:
                label_ConfirmaçãoDeCadastro.configure(text='Esta pessoa já está cadastrada aqui.')
                podeContinuar = False
               
        if podeContinuar == True: 
            if nomeAluno == '':
                label_ConfirmaçãoDeCadastro.configure(text='Digite o nome')
                podeContinuar = False
            else:       
                for letra in nomeAluno:
                    if letra.isdigit():
                        input_Nome.delete(0,END)
                        label_ConfirmaçãoDeCadastro.configure(text='Não pode colocar número no Nome.')
                        input_Nome.delete(0, END)
                        input_Idade.delete(0, END)
                        input_Nome.focus()
                        podeContinuar = False
                              
            if idadeAluno == '':
                label_ConfirmaçãoDeCadastro.configure(text='Digite a idade')
                podeContinuar = False
            else:
                for caracteres in idadeAluno:
                    if caracteres.isalpha():
                        input_Idade.delete(0,END)
                        label_ConfirmaçãoDeCadastro.configure(text='Não pode colocar letra na Idade.')
                        input_Idade.delete(0, END) 
                        input_Idade.focus()
                        podeContinuar = False
                                              
            match valorModalidade:
                case 0:
                    modalidadeAluno = 'Natação'
                case 1:
                    modalidadeAluno = 'Musculação'
                case 2:
                    modalidadeAluno = 'Pilates'
                case 3:
                    modalidadeAluno = 'Capoeira'
                case 4:
                    modalidadeAluno = 'Boxe'
                case 5:
                    modalidadeAluno = 'Vôlei'
            
                
            if podeContinuar == True:
                global contadorParaID
                aluno = Aluno(id=contadorParaID, nome=nomeAluno, idade=idadeAluno, modalidade=modalidadeAluno)
                listaDeAlunos.append(aluno)
                label_ConfirmaçãoDeCadastro.configure(text=f'{nomeAluno} cadastrado com sucesso!')
                contadorParaID += 1
                                                
                input_Nome.delete(0, END)
                input_Idade.delete(0, END) 
                input_Nome.focus()
                                    
    btoCadastrarAluno = Button(siteCadastrarFrame, text='Cadastar', command=cadastrarAluno)
    btoCadastrarAluno.pack()

    label_ConfirmaçãoDeCadastro = Label(siteCadastrarFrame, text='')
    label_ConfirmaçãoDeCadastro.pack()

    # Função para voltar ao Frame do começo
    def forgetSiteCadastro():
        siteCadastrarFrame.destroy()
        siteMainFrame()

    btoVoltarAoMainFrame = Button(siteCadastrarFrame, text='Voltar ao Começo', command=forgetSiteCadastro )
    btoVoltarAoMainFrame.pack()



def siteAtualizarAluno():
    global mainFrame
    if mainFrame:
        mainFrame.destroy()

    def selecionarIDparaMUDAR():
        
            idEscolhido = int(input_EscolhaDoId.get())
            numeroMaxListaDeAlunos = len(listaDeAlunos)
            for aluno in listaDeAlunos:
                if idEscolhido == aluno.alunoID:
                    
                    label_IdEscolhido.configure(text=f'Você selecionou {aluno.alunoNome}, idade: {aluno.alunoIdade}, modalidade: {aluno.alunoModalidade}')

                    # Colocar uma função aqui, para abrir a escolha do que quer mudar
                    radioButtonFrame = Frame(siteAtualizarAlunoFrame)
                    radioButtonFrame.pack()

                    label_EscolherOdadoAserMudado = Label(radioButtonFrame, text='Escolhar o que quer mudar')
                    label_EscolherOdadoAserMudado.pack()

                    valor = IntVar()

                    def pegarMudar():
                        mudar = valor.get()

                        def mudarNomeFunction():
                            atualizarNome = str(input_MudarNome.get())
                            aluno.alunoNome = atualizarNome
                            label_IdEscolhido.configure(text='O nome foi atualizado com sucesso')
                            radioButtonFrame.destroy()

                        def mudarIdadeFunction():
                            atualizarIdade = str(input_MudarIdade.get())
                            aluno.alunoIdade = atualizarIdade
                            label_IdEscolhido.configure(text='A idade foi atualizado com sucesso')
                            radioButtonFrame.destroy()

                        def mudarModalidadeFunction():
                            atualizarModalidade = mudarModalidadeButtonValue.get()

                            match atualizarModalidade:
                                case 0:
                                    aluno.alunoModalidade = 'Natação'
                                    label_IdEscolhido.configure(text='A modalidade foi atualizado com sucesso')
                                    radioButtonFrame.destroy()
                                case 1:
                                    aluno.alunoModalidade = 'Musculação'
                                    label_IdEscolhido.configure(text='A modalidade foi atualizado com sucesso')
                                    radioButtonFrame.destroy()
                                case 2:
                                    aluno.alunoModalidade = 'Pilates'
                                    label_IdEscolhido.configure(text='A modalidade foi atualizado com sucesso')
                                    radioButtonFrame.destroy()
                                case 3:
                                    aluno.alunoModalidade = 'Capoeira'
                                    label_IdEscolhido.configure(text='A modalidade foi atualizado com sucesso')
                                    radioButtonFrame.destroy()
                                case 4:
                                    aluno.alunoModalidade = 'Boxe'
                                    label_IdEscolhido.configure(text='A modalidade foi atualizado com sucesso')
                                    radioButtonFrame.destroy()
                                case 5:
                                    aluno.alunoModalidade = 'Vôlei'
                                    label_IdEscolhido.configure(text='A modalidade foi atualizado com sucesso')
                                    radioButtonFrame.destroy()

                        if mudar == 0:
                            label_MudarNome = Label(radioButtonFrame, text='Mudar Nome')
                            label_MudarNome.pack()
                            input_MudarNome = Entry(radioButtonFrame)
                            input_MudarNome.pack()
                            btoMudarNome = Button(radioButtonFrame, text='Atualizar', command=mudarNomeFunction)
                            btoMudarNome.pack()
                            

                        elif mudar == 1:
                            label_MudarIdade = Label(radioButtonFrame, text='Mudar Idade')
                            label_MudarIdade.pack()
                            input_MudarIdade = Entry(radioButtonFrame)
                            input_MudarIdade.pack()
                            btoMudarIdade = Button(radioButtonFrame, text='Atualizar', command=mudarIdadeFunction)
                            btoMudarIdade.pack()
                            

                        elif mudar == 2:
                            label_MudarModalidade = Label(radioButtonFrame, text='Mudar Modalidade')
                            label_MudarModalidade.pack()

                            mudarModalidadeFrame = Frame(radioButtonFrame)
                            mudarModalidadeFrame.pack()

                            mudarModalidadeButtonValue = IntVar()

                            mod_Natacao = Radiobutton(mudarModalidadeFrame, text='Natação', variable=mudarModalidadeButtonValue, value=0, pady=10, padx=10)
                            mod_Natacao.grid(column=0, row=0)
                            mod_Musculacao = Radiobutton(mudarModalidadeFrame, text='Musculação', variable=mudarModalidadeButtonValue, value=1, pady=10, padx=10)
                            mod_Musculacao.grid(column=0, row=1)
                            mod_Pilates = Radiobutton(mudarModalidadeFrame, text='Pilates', variable=mudarModalidadeButtonValue, value=2, pady=10, padx=10)
                            mod_Pilates.grid(column=0, row=2)
                            mod_Capoeira = Radiobutton(mudarModalidadeFrame, text='Capoeira', variable=mudarModalidadeButtonValue, value=3, pady=10, padx=10)
                            mod_Capoeira.grid(column=2, row=0)
                            mod_Boxe = Radiobutton(mudarModalidadeFrame, text='Boxe', variable=mudarModalidadeButtonValue, value=4, pady=10, padx=10)
                            mod_Boxe.grid(column=2, row=1)
                            mod_Volei = Radiobutton(mudarModalidadeFrame, text='Vôlei', variable=mudarModalidadeButtonValue, value=5, pady=10, padx=10)
                            mod_Volei.grid(column=2, row=2)

                            btoMudarModalidade = Button(mudarModalidadeFrame, text='Atualizar', command=mudarModalidadeFunction)
                            btoMudarModalidade.grid(column=1, row=3)
                            

                    selectRadioButtonFrame = Frame(radioButtonFrame)
                    selectRadioButtonFrame.pack()

                    mudarNome = Radiobutton(selectRadioButtonFrame, text='Nome', variable=valor, value=0, pady=10)
                    mudarNome.grid(column=0, row=0)
                    mudarIdade = Radiobutton(selectRadioButtonFrame, text='Idade', variable=valor, value=1, pady=10)
                    mudarIdade.grid(column=1, row=0)
                    mudarModalidade = Radiobutton(selectRadioButtonFrame, text='Modalidade', variable=valor, value=2, pady=10)
                    mudarModalidade.grid(column=2, row=0)
                    btoSelectChange = Button(selectRadioButtonFrame, text='Selecionar', command=pegarMudar)
                    btoSelectChange.grid(column=1, row=2)

                    break
            
                else:
                    label_IdEscolhido.configure(text=f'Selecione apenas o id que se encontrar na lista. De 1 até {numeroMaxListaDeAlunos -1}')

    #Fim da def selecionarIDparaMUDAR()

    siteAtualizarAlunoFrame = Frame(janela)
    siteAtualizarAlunoFrame.pack()

    label_AtualizacaoDeDado = Label(siteAtualizarAlunoFrame, text='Atualização de Dados')
    label_AtualizacaoDeDado.pack()
        
    label_EscolhaDoId = Label(siteAtualizarAlunoFrame, text='Escreva o id da pessoa pra atualizar')
    label_EscolhaDoId.pack()
    input_EscolhaDoId = Entry(siteAtualizarAlunoFrame)
    input_EscolhaDoId.pack()
    label_IdEscolhido = Label(siteAtualizarAlunoFrame, text='')
    label_IdEscolhido.pack()
    btoID_Escolhido = Button(siteAtualizarAlunoFrame, text='Selecionar Id', command=selecionarIDparaMUDAR)
    btoID_Escolhido.pack()

    def voltarAoPincipal():
        siteAtualizarAlunoFrame.destroy()
        siteMainFrame()
    btoVoltarAoPrincipal = Button(siteAtualizarAlunoFrame, text='Voltar', command=voltarAoPincipal)
    btoVoltarAoPrincipal.pack()


def siteVerListaDeAluno():
    global mainFrame
    if mainFrame:
        mainFrame.destroy()

    siteVerListaDeAlunoFrame = Frame(janela)
    siteVerListaDeAlunoFrame.pack()

    areaDeLista = Frame(siteVerListaDeAlunoFrame)
    areaDeLista.pack()

    tree = ttk.Treeview(areaDeLista, columns=['nome', 'idade', 'modalidade'])  
    tree.column('#0',width=50)
    tree.column('nome',width=100)
    tree.column('idade',width=50)
    tree.column('modalidade',width=100)
    tree.heading('#0', text='ID')
    tree.heading('nome', text="Nome")
    tree.heading('idade', text="Idade")
    tree.heading('modalidade', text="Modalidade")
    

    lateral_ScrollBar = Scrollbar(areaDeLista, orient='vertical', command=tree.yview)
    lateral_ScrollBar.pack(side='right', fill='y')
    tree.configure(yscrollcommand=lateral_ScrollBar.set)
    tree.pack()

    for aluno in listaDeAlunos:
        idAluno = aluno.alunoID
        nomeAluno = aluno.alunoNome
        idadeAluno = aluno.alunoIdade
        modalidadeAluno = aluno.alunoModalidade

        # print(f"""
        # id:{idAluno}
        # Nome:{nomeAluno}
        # Idade:{idadeAluno}
        # Modalidade:{modalidadeAluno}
        # """)

        tree.insert('', 'end', text=idAluno, values=[nomeAluno, idadeAluno, modalidadeAluno])



    label_Localizar = Label(siteVerListaDeAlunoFrame, text='Localizar aluno pelo nome')
    label_Localizar.pack()
    input_Localizar = Entry(siteVerListaDeAlunoFrame)
    input_Localizar.pack()
    
    label_AlunoLocalizado = Label(siteVerListaDeAlunoFrame, text='')
    label_AlunoLocalizado.pack()

    def localizarAlunoNaLista():
        label_AlunoLocalizado.configure(text='')
        nomeParaLocalizar = str(input_Localizar.get())
        input_Localizar.delete(0,END)
        for localizarAluno in listaDeAlunos:
            # print(nomeParaLocalizar)
            # print(localizarAluno.alunoNome)
            if nomeParaLocalizar == localizarAluno.alunoNome:
                
                label_AlunoLocalizado.configure(text=f'{localizarAluno.alunoNome} (id:{localizarAluno.alunoID}) se encontra matriculado aqui, fazendo: {localizarAluno.alunoModalidade}.')
            else:
                label_AlunoLocalizado.configure(text='Este nome não foi localizado, possivelmente não se encontra matriculado aqui.')

    btoLocalizarAluno = Button(siteVerListaDeAlunoFrame, text='Buscar aluno', command=localizarAlunoNaLista)
    btoLocalizarAluno.pack()

    def forgetSiteVerLista():
        siteVerListaDeAlunoFrame.destroy()
        siteMainFrame()
    btoVoltarAoMainFrame = Button(siteVerListaDeAlunoFrame, text='Voltar ao Começo', command=forgetSiteVerLista )
    btoVoltarAoMainFrame.pack()



def siteExcluirAluno():
    global mainFrame
    if mainFrame:
        mainFrame.destroy()

    siteExcluirAlunoFrame = Frame(janela)
    siteExcluirAlunoFrame.pack()

    label_TituloExcluir = Label(siteExcluirAlunoFrame, text='Remoção de Aluno')
    label_TituloExcluir.pack()

    def selecionarPorID():
        selecionadoPorID = int(input_SelecionarPorID.get())
        label_AlunoSelecionado.configure(text='')

        contadorDeID = 0
        
        for aluno in listaDeAlunos:
            if selecionadoPorID == aluno.alunoID:

                def eliminarAluno():
                    label_AlunoSelecionado.configure(text=f'{aluno.alunoNome} foi removido do sistema.')
                    listaDeAlunos.remove(aluno)
                    btoEliminar.destroy()
                    btoNaoEliminar.destroy()
                    input_SelecionarPorID.delete(0,END)
                    input_SelecionarPorID.focus()


                def naoEliminar():
                    input_SelecionarPorID.delete(0,END)
                    input_SelecionarPorID.focus()
                    label_AlunoSelecionado.destroy()
                    btoEliminar.destroy()
                    btoNaoEliminar.destroy()

                label_AlunoSelecionado.configure(text=f'''Você selecionou o {aluno.alunoNome} da {aluno.alunoModalidade}.
    Tem certeza que quer eliminar ele(a)?''')
                
                btoEliminar = Button(pequenaJanelaExcluirFrame, text='Sim, remover aluno', command=eliminarAluno)
                btoEliminar.pack()
                btoNaoEliminar = Button(pequenaJanelaExcluirFrame, text='Não. //  Preservar aluno', command=naoEliminar)
                btoNaoEliminar.pack()

                break
            else:
                contadorDeID +=1
                if contadorDeID == len(listaDeAlunos):
                    label_AlunoSelecionado.configure(text='Esse ID não existe.')

    label_SelecionarPorID = Label(siteExcluirAlunoFrame, text='Escreva o ID do aluno para remover')
    label_SelecionarPorID.pack()
    input_SelecionarPorID = Entry(siteExcluirAlunoFrame)
    input_SelecionarPorID.pack()
    btoSelecionarPorID = Button(siteExcluirAlunoFrame, text='Selecionar', command=selecionarPorID)
    btoSelecionarPorID.pack()

    label_AlunoSelecionado = Label(siteExcluirAlunoFrame, text='')
    label_AlunoSelecionado.pack()

    pequenaJanelaExcluirFrame = Frame(siteExcluirAlunoFrame)
    pequenaJanelaExcluirFrame.pack()

    def forgetSiteExcluirAluno():
        siteExcluirAlunoFrame.destroy()
        siteMainFrame()
    btoVoltarAoMainFrame = Button(siteExcluirAlunoFrame, text='Voltar ao começo', command=forgetSiteExcluirAluno)
    btoVoltarAoMainFrame.pack()


mainFrame = Frame(janela)
mainFrame.pack(padx=5, pady=5)

btoSiteCadastroDeAluno = Button(mainFrame, text='Para Cadastrar Aluno', command=siteCadastroDeAluno)
btoSiteCadastroDeAluno.pack()

btoSiteAtualizarAluno = Button(mainFrame, text='Para atualização de Aluno', command=siteAtualizarAluno)
btoSiteAtualizarAluno.pack()

btoVerListaDeAluno = Button(mainFrame, text='Ver Lista de Aluno', command=siteVerListaDeAluno)
btoVerListaDeAluno.pack()

btoSiteExcluirAluno = Button(mainFrame, text='Para excluir aluno', command=siteExcluirAluno)
btoSiteExcluirAluno.pack()

btoDestroy = Button(mainFrame, text='Sair', command=janela.destroy)
btoDestroy.pack(side='bottom')

janela.mainloop()
