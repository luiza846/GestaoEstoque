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

# O restante do seu código permanece inalterado
