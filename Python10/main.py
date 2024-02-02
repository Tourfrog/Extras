from tkinter import *
janela = Tk()
janela.title('Cadastro de Email')
janela.geometry('300x300')

bancoDeDados = [
    'joao@email.com',
    'maria@email.com',
    'jose@email.com',
    'ana@email.com',
    'pedro@email.com',
    'abel@email.com',
    'patricia@email.com',
    'amanda@email.com'
]

novoEmail = 'teste'
novaSenha = 'teste1'
novaRepetirSenha = 'teste2'

tituloLabel = Label(text='Cadastro de email', height = 2, font= ('Arial',12, 'bold') ,bg = 'red')
tituloLabel.pack()

email_Label = Label(text='Email' )
email_Label.pack()
email_Input = Entry()
email_Input.pack()

checarEmail = Label(text='')
checarEmail.pack()

def emailOK():
    global novoEmail
    verEmail = str(email_Input.get())
    podeContinuar = True

    if verEmail == '':
        checarEmail.configure(text='Escreva o email.')
    else:
        for email in bancoDeDados:
            if verEmail == email:
                checarEmail.configure(text='Esse email já está cadastrado')
                podeContinuar = False
        
        if podeContinuar == True:
            checarEmail.configure(text='Email aceito para cadastro')
            
            novoEmail = verEmail
            
    

senha_Label = Label(text='Senha')
senha_Label.pack()
senha_Input = Entry(show='*')
senha_Input.pack()

checarSenhaForte = Label(text='')
checarSenhaForte.pack()

def senhaForte():
    global novaSenha
    verSenhaForte = str(senha_Input.get())
    podeContinuar = True

    checarUpper = False
    checarLower = False
    checarNumber = False
    checarSpecialLetter = False
    

    if verSenhaForte == '':
        checarSenhaForte.configure(text='Escreva a senha')
    else:
        contarSenhaForte = 0
        for caracter in verSenhaForte:
            if caracter.isdigit():
                contarSenhaForte += 1
                checarNumber = True
            elif caracter.isupper():
                contarSenhaForte += 1
                checarUpper = True
            elif caracter.islower():
                contarSenhaForte += 1
                checarLower = True
            elif caracter in '!@#$%&?':
                contarSenhaForte += 1
                checarSpecialLetter = True

        if len(verSenhaForte) >= 8:
            contarSenhaForte += 1
            checarTamanho = True
            
        if contarSenhaForte < 8:
            podeContinuar = False
            checarSenhaForte.configure(text='''A senha não é forte o suficiente,
    tem que ter 8 digito no minimo!''')
        else:
            if checarUpper == False:
                checarSenhaForte.configure(text='Tem que ter uma letra Maiuscula!')
            else:
                if checarLower == False:
                    checarSenhaForte.configure(text='Tem que ter uma letra minuscula!')
                else:
                    if checarNumber == False:
                        checarSenhaForte.configure(text='Tem que ter número!')
                    else:
                        if checarSpecialLetter == False:
                            checarSenhaForte.configure(text='Tem que ter letra especial, ex: !@##%')
                        else:
                            podeContinuar = True
                            checarSenhaForte.configure(text='A senha é muito forte!')
                            novaSenha = verSenhaForte
            


confirmarSenha_Label = Label(text='Repetir senha para confirmar')
confirmarSenha_Label.pack()
confirmSenha_Input = Entry(show='*')
confirmSenha_Input.pack()

checarSenhaIgual_Label = Label(text='')
checarSenhaIgual_Label.pack()

def senhaIgual():
    global novaRepetirSenha
    sameSenha = str(confirmSenha_Input.get())
    senhaOriginal = str(senha_Input.get())
    podeContinuar = True

    if sameSenha == '':
        checarSenhaIgual_Label.configure(text='Escreva o capmo de Repetir senha')
    else:
        if sameSenha != senhaOriginal:
            podeContinuar = False
            checarSenhaIgual_Label.configure(text='Você errou em repetir a senha!')
        else:
            checarSenhaIgual_Label.configure(text='Repetir senha, OK!')
            podeContinuar = True
            novaRepetirSenha = sameSenha
            

def cadastrarEmail():
    # Condição para aceitar o cadastro
    contadorCadastro = 0
    

    emailOK()
    senhaForte()
    senhaIgual()

    print(novoEmail)
    print(novaSenha)
    print(novaRepetirSenha)

    if novoEmail in bancoDeDados:
        print('Email já cadastrado')
    else:
        if novoEmail != 'teste':
            contadorCadastro += 1
        if novaSenha != 'teste1':
            contadorCadastro += 1
        if novaRepetirSenha != 'teste2':
            contadorCadastro += 1

        if contadorCadastro == 3:
            bancoDeDados.append(novoEmail)
            print(bancoDeDados)
            resultado_Label.configure(text='Email Cadastrado com sucesso!')

    

botao = Button(janela, text='Cadastrar', command=cadastrarEmail)
botao.pack()

resultado_Label = Label(text='')
resultado_Label.pack()

janela.mainloop()