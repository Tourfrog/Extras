from tkinter import ttk
from tkinter import *

# Função para adicionar dados à TreeView
def adicionar_dados():
    nome = entry_nome.get()
    idade = entry_idade.get()
    modalidade = entry_modalidade.get()

    tree.insert('', 'end', values=(nome, idade, modalidade))

# Configuração da janela
janela = Tk()
janela.title('Exemplo TreeView')
janela.geometry('400x300')

# Entradas para obter dados
Label(janela, text='Nome:').grid(row=0, column=0, padx=5, pady=5)
Label(janela, text='Idade:').grid(row=1, column=0, padx=5, pady=5)
Label(janela, text='Modalidade:').grid(row=2, column=0, padx=5, pady=5)

entry_nome = Entry(janela)
entry_nome.grid(row=0, column=1, padx=5, pady=5)

entry_idade = Entry(janela)
entry_idade.grid(row=1, column=1, padx=5, pady=5)

entry_modalidade = Entry(janela)
entry_modalidade.grid(row=2, column=1, padx=5, pady=5)

# Botão para adicionar dados à TreeView
btn_adicionar = Button(janela, text='Adicionar', command=adicionar_dados)
btn_adicionar.grid(row=3, column=0, columnspan=2, pady=10)

# TreeView
tree = ttk.Treeview(janela, columns=('Nome', 'Idade', 'Modalidade'), show='headings')
tree.heading('Nome', text='Nome')
tree.heading('Idade', text='Idade')
tree.heading('Modalidade', text='Modalidade')

tree.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

# Exemplo inicial
tree.insert('', 'end', values=('João', 25, 'Natação'))
tree.insert('', 'end', values=('Maria', 30, 'Musculação'))

# Execução da aplicação
janela.mainloop()
