import tkinter as tk
from PIL import Image, ImageTk
import math
import random
import random as rd

"""                         CALCULOS                           """

# calcular a funcao objetivo
def FuncaoObjetivo(media_demanda, estoque_diario, demanda_total, soma_deman_atendido):

    a = 0.7
    b = 0.3

    # calcular o criterio economico
    criterio_economico = math.exp((math.log((10 ** -3) / (10 * media_demanda)) * estoque_diario))

    # calcular o nivel de atendimento
    nivel_atendimento = soma_deman_atendido/demanda_total

    # calcular funcao objetivo
    funcao_objetivo = (nivel_atendimento * a) + (criterio_economico * b)

    return funcao_objetivo


"""                        INTERFACE                           """

def confirmar():

    # Obter os valores digitados pelo usuário
    media_demanda = float(media_demanda_entry.get())
    estoque_medio = float(estoque_medio_entry.get())
    demanda_total = float(demanda_total_entry.get())
    soma_demanda_atendido = float(soma_demanda_atendido_entry.get())

    # Criar uma nova janela com as informações digitadas
    nova_janela = tk.Toplevel(root)
    nova_janela.title("Informações Digitadas")

    # Definir as dimensões da nova janela
    largura_nova_janela = 800
    altura_nova_janela = 600

    # Definir a geometria da nova janela com a posição centralizada
    nova_janela.geometry(f"{largura_nova_janela}x{altura_nova_janela}")

    # Obter as dimensões da tela
    largura_tela = nova_janela.winfo_screenwidth()
    altura_tela = nova_janela.winfo_screenheight()

    # Calcular a posição para centralizar a nova janela
    pos_x = (largura_tela - largura_nova_janela) // 2
    pos_y = (altura_tela - altura_nova_janela) // 2

    # Centralizar a nova janela
    nova_janela.geometry(f"{largura_nova_janela}x{altura_nova_janela}+{pos_x}+{pos_y}")

    # Adicionar rótulos com as informações digitadas
    tk.Label(nova_janela, text="Média de Demanda: " + str(media_demanda)).pack()
    tk.Label(nova_janela, text="Estoque Médio: " + str(estoque_medio)).pack()
    tk.Label(nova_janela, text="Demanda Total: " + str(demanda_total)).pack()
    tk.Label(nova_janela, text="Soma de Demanda Atendido: " + str(soma_demanda_atendido)).pack()
    funcao_objetivo = FuncaoObjetivo(media_demanda, estoque_medio, demanda_total, soma_demanda_atendido)
    tk.Label(nova_janela, text="Função Objetivo: " + str(funcao_objetivo)).pack()

# Criar a janela principal
root = tk.Tk()
root.title("Cadastro de Informações")

# Definir o tamanho da janela principal
largura_janela = 800
altura_janela = 600

# Obter as dimensões da tela
largura_tela = root.winfo_screenwidth()
altura_tela = root.winfo_screenheight()

# Calcular a posição para centralizar a janela principal
pos_x = (largura_tela - largura_janela) // 2
pos_y = (altura_tela - altura_janela) // 2

# Definir a geometria da janela principal com a posição centralizada
root.geometry(f"{largura_janela}x{altura_janela}+{pos_x}+{pos_y}")

# Carregar a imagem de fundo
imagem_fundo = Image.open("C:/Users/analu/OneDrive - Fatec Centro Paula Souza/5º PERÍODO/Programação Linear/GestaoEstoque/gestaoEstoque_python/interfaceI.png")

largura, altura = imagem_fundo.size

# Criar um frame para conter os elementos da interface
frame = tk.Frame(root, width=largura, height=altura)
frame.pack()

# Carregar a imagem de fundo no frame
imagem_fundo = ImageTk.PhotoImage(imagem_fundo)
background_label = tk.Label(frame, image=imagem_fundo)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Posição x para os elementos à direita
pos_x = largura * 0.8

# Criar os rótulos e campos de entrada dentro do frame
tk.Label(frame, text="Média de Demanda Diária:").place(relx=pos_x / largura, rely=0.3, anchor='e')
media_demanda_entry = tk.Entry(frame, width=28)
media_demanda_entry.place(relx=pos_x / largura, rely=0.35, anchor='e')

tk.Label(frame, text="Estoque Médio Diário:").place(relx=pos_x / largura, rely=0.4, anchor='e')
estoque_medio_entry = tk.Entry(frame, width=28)
estoque_medio_entry.place(relx=pos_x / largura, rely=0.45, anchor='e')

tk.Label(frame, text="Demanda Total:").place(relx=pos_x / largura, rely=0.5, anchor='e')
demanda_total_entry = tk.Entry(frame, width=28)
demanda_total_entry.place(relx=pos_x / largura, rely=0.55, anchor='e')

tk.Label(frame, text="Soma de Demanda Atendido:").place(relx=pos_x / largura, rely=0.6, anchor='e')
soma_demanda_atendido_entry = tk.Entry(frame, width=28)
soma_demanda_atendido_entry.place(relx=pos_x / largura, rely=0.65, anchor='e')

# Criar o botão de confirmar dentro do frame
confirmar_button = tk.Button(frame, text="Confirmar", command=confirmar, width=23, bg="#758094", fg="white")
confirmar_button.place(relx=pos_x / largura, rely=0.75, anchor='e')

root.mainloop()



