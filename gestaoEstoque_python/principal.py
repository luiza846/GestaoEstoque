import tkinter as tk
from PIL import Image, ImageTk
import math
import random
import random as rd


""" CALCULOS """

tamanho_cromossomo = 22
tamanho_torneio = 5
taxa_mutacao = 0.01
tamanho_populacao = 100
geracoes = 100

class Cromossomo:
    def __init__(crom):
        crom.genes = [0] * tamanho_cromossomo

# gerar um cromossomo de 22 genes
def GerarProblema(n, media_demanda):

    tamanho_lote = []
    ponto_reposicao = []

    
    
    # gerar problema p/ tamanho lote
    for i in range(n):
        tamanho_lote.append(rd.randint(0, 1))
        binario_string_tl = ''.join(map(str, tamanho_lote))
        decimal_tl = int(binario_string_tl, 2)
    print("Cromossomo Tamanho Lote: ",tamanho_lote)
    # gerar problema p/ ponto de reposicao
    for i in range(n):
        ponto_reposicao.append(rd.randint(0, 1))
        binario_string_pr = ''.join(map(str, ponto_reposicao))
        decimal_pr = int(binario_string_pr, 2)
    print("Cromossomo Ponto de Reposicao: ",ponto_reposicao)
    if decimal_pr< 2 * media_demanda or decimal_pr > 10 * media_demanda or \
            decimal_tl < 2 * media_demanda or decimal_tl > 10 * media_demanda:
                return -9999


    return tamanho_lote, ponto_reposicao

# gerar cromossomo de 22 genes
def InicializarCromossomo(cromossomo):

    for x in range(tamanho_cromossomo):
        # gerar numeros aleatorios de 1 e 0
        cromossomo.genes[x] = random.randint(0 , 1)

    # pegar 11 primeiros genes para tamanho lote
    tamanho_lote = cromossomo.genes[:tamanho_cromossomo // 2]

    # pegar o restante de genes para ponto de reposicao
    ponto_reposicao = cromossomo.genes[tamanho_cromossomo //2:]

    print("Cromossomo: ",cromossomo.genes)
    print("Cromossomo do Tamanho Lote: ",tamanho_lote)
    print("Crmossomo de Ponto de Reposicao: ", ponto_reposicao)
    

""" INTERFACE GERADO PELO CHATGPT """


class GestaoEstoqueApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestão de Estoque")
        self.root.geometry("800x600")

        # Carregar a imagem de fundo
        imagem_fundo = Image.open("C:/Users/anacl/OneDrive/Área de Trabalho/Ana/5°Semestre/Programação Linear/GestaoEstoque/gestaoEstoque_python/interfaceI.png")
        imagem_fundo = imagem_fundo.resize((800, 600))
        imagem_fundo_tk = ImageTk.PhotoImage(imagem_fundo)

        # Exibir a imagem de fundo em um widget de lona
        self.canvas = tk.Canvas(root, width=800, height=600)
        self.canvas.pack(fill="both", expand=True)
        self.canvas.create_image(0, 0, anchor="nw", image=imagem_fundo_tk)
        self.canvas.imagem_fundo_tk = imagem_fundo_tk

        # Frame para os campos com cor de fundo transparente
        self.frame_campos = tk.Frame(self.canvas, bd=0, highlightthickness=0)
        self.frame_campos.place(relx=0.88, rely=0.5, anchor="e")

        # Campos
        

        self.label_media_demanda = tk.Label(self.frame_campos, text="Média de Demanda Diária:")
        self.label_media_demanda.grid(row=0, column=0, padx=(0, 3), pady=5, sticky="e")
        self.entry_media_demanda = tk.Entry(self.frame_campos)
        self.entry_media_demanda.grid(row=0, column=1, padx=(3, 0), pady=5, sticky="w")

        self.label_estoque_medio = tk.Label(self.frame_campos, text="Estoque Médio Diário:")
        self.label_estoque_medio.grid(row=1, column=0, padx=(0, 3), pady=5, sticky="e")
        self.entry_estoque_medio = tk.Entry(self.frame_campos)
        self.entry_estoque_medio.grid(row=1, column=1, padx=(3, 0), pady=5, sticky="w")

        self.label_demanda_total = tk.Label(self.frame_campos, text="Demanda Total:")
        self.label_demanda_total.grid(row=2, column=0, padx=(0, 3), pady=5, sticky="e")
        self.entry_demanda_total = tk.Entry(self.frame_campos)
        self.entry_demanda_total.grid(row=2, column=1, padx=(3, 0), pady=5, sticky="w")

        self.label_soma_atendido = tk.Label(self.frame_campos, text="Soma de Demanda Atendido:")
        self.label_soma_atendido.grid(row=3, column=0, padx=(0, 3), pady=5, sticky="e")
        self.entry_soma_atendido = tk.Entry(self.frame_campos)
        self.entry_soma_atendido.grid(row=3, column=1, padx=(3, 0), pady=5, sticky="w")

        self.label_tamanho_problema = tk.Label(self.frame_campos, text="Tamanho do Problema:")
        self.label_tamanho_problema.grid(row=4, column=0, padx=(0, 3), pady=5, sticky="e")
        self.entry_tamanho_problema = tk.Entry(self.frame_campos)
        self.entry_tamanho_problema.grid(row=4, column=1, padx=(3, 0), pady=5, sticky="w")

        self.label_prioridade = tk.Label(self.frame_campos, text="Prioridade:")
        self.label_prioridade.grid(row=5, column=0, padx=(0, 3), pady=5, sticky="e")
        self.entry_prioridade = tk.Entry(self.frame_campos)
        self.entry_prioridade.grid(row=5, column=1, padx=(3, 0), pady=5, sticky="w")
        

        # Frame para os botões
        self.frame_botoes = tk.Frame(self.canvas, bd=0, highlightthickness=0)
        self.frame_botoes.place(relx=0.88, rely=0.8, anchor="e")

        # Botões

        self.botao_avalia = tk.Button(self.frame_botoes, text="Avalia", command=self.criar_janela_avalia)
        self.botao_avalia.pack(side=tk.RIGHT, padx=3)

        self.botao_solucao_inicial = tk.Button(self.frame_botoes, text="Solução Inicial", command=self.criar_janela_solucao_inicial)
        self.botao_solucao_inicial.pack(side=tk.RIGHT, padx=3)

        self.botao_gerar_problema = tk.Button(self.frame_botoes, text="Gerar Problema", command=self.criar_janela_gerar_problema)
        self.botao_gerar_problema.pack(side=tk.RIGHT, padx=3)

    """   NA JANELA GERAR PROBLEMA   """

    def criar_janela_gerar_problema(self):
        janela_gerar_problema = tk.Toplevel(self.root)
        janela_gerar_problema.title("Gerar Problema")
        janela_gerar_problema.geometry("800x600")
        # Implemente a lógica para gerar o problema aqui

        # pegar o valor digitado pelo usuario
        n = int(self.entry_tamanho_problema.get())
        media_demanda = int(self.entry_media_demanda.get())
        prioridade = int(self.entry_prioridade.get())
        
        
        cromossomos = []      
        for _ in range(n):
            cromossomo = Cromossomo()
            InicializarCromossomo(cromossomo)
            cromossomos.append(cromossomo)
            tamanho_lote = cromossomo.genes[:tamanho_cromossomo // 2]
            tamanho_lote_string = ''.join(map(str, tamanho_lote))
            decimal_tamanho_lote = int(tamanho_lote_string, 2)
            ponto_reposicao = cromossomo.genes[tamanho_cromossomo //2:]
            ponto_reposicao_string = ''.join(map(str, ponto_reposicao))
            decimal_ponto_reposicao = int(ponto_reposicao_string, 2)


        #como aqui é OR apenas um dos valores tem que estar dentro da condição 
        if decimal_ponto_reposicao > 2 * media_demanda and decimal_ponto_reposicao < 10 * media_demanda or \
            decimal_tamanho_lote > 2 * media_demanda and decimal_tamanho_lote < 10 * media_demanda:
                if prioridade == 1:
                    if tamanho_lote < ponto_reposicao:
                        label_cromossomo = tk.Label(janela_gerar_problema, text=f"Cromossomo {_}: {cromossomo.genes}")
                        label_cromossomo.pack(pady=10)
            #separa o cromossomo e pega a parte do tamanho lote e imprimi
                        tamanho_lote = cromossomo.genes[:tamanho_cromossomo // 2]
                        
                        label_tamanho_lote = tk.Label(janela_gerar_problema, text="Cromossomo de Tamanho Lote: {}".format(tamanho_lote))
                        label_tamanho_lote.pack(pady=10)
            #transforma o cromossomo do tamanho lote em decimal e imprimi
                        tamanho_lote_string = ''.join(map(str, tamanho_lote))
                        decimal_tamanho_lote = int(tamanho_lote_string, 2)
                        label_decimal_tl = tk.Label(janela_gerar_problema, text="Tamanho Lote em decimal: {}".format(decimal_tamanho_lote))
                        label_decimal_tl.pack(pady=10)
            #separa o cromossomo e pega a parte do ponto reposição e imprimi
                        ponto_reposicao = cromossomo.genes[tamanho_cromossomo //2:]
                        label_ponto_reposicao = tk.Label(janela_gerar_problema, text="Cromossomo de Ponto de Reposição: {}".format(ponto_reposicao))
                        label_ponto_reposicao.pack(pady=10)
            #tranforma o cromossomo ponto reposição em decimal e imprimi
                        ponto_reposicao_string = ''.join(map(str, ponto_reposicao))
                        decimal_ponto_reposicao = int(ponto_reposicao_string, 2)
                        label_decimal_pr = tk.Label(janela_gerar_problema, text="Ponto Reposição em decimal: {}".format(decimal_ponto_reposicao))
                        label_decimal_pr.pack(pady=10)
        else:
            if tamanho_lote >= ponto_reposicao:
                        
#imprimi os cromossomos inteiros
                label_cromossomo = tk.Label(janela_gerar_problema, text=f"Cromossomo {_}: {cromossomo.genes}")
                label_cromossomo.pack(pady=10)
    #separa o cromossomo e pega a parte do tamanho lote e imprimi
                tamanho_lote = cromossomo.genes[:tamanho_cromossomo // 2]
                
                label_tamanho_lote = tk.Label(janela_gerar_problema, text="Cromossomo de Tamanho Lote: {}".format(tamanho_lote))
                label_tamanho_lote.pack(pady=10)
    #transforma o cromossomo do tamanho lote em decimal e imprimi
                tamanho_lote_string = ''.join(map(str, tamanho_lote))
                decimal_tamanho_lote = int(tamanho_lote_string, 2)
                label_decimal_tl = tk.Label(janela_gerar_problema, text="Tamanho Lote em decimal: {}".format(decimal_tamanho_lote))
                label_decimal_tl.pack(pady=10)
    #separa o cromossomo e pega a parte do ponto reposição e imprimi
                ponto_reposicao = cromossomo.genes[tamanho_cromossomo //2:]
                label_ponto_reposicao = tk.Label(janela_gerar_problema, text="Cromossomo de Ponto de Reposição: {}".format(ponto_reposicao))
                label_ponto_reposicao.pack(pady=10)
    #tranforma o cromossomo ponto reposição em decimal e imprimi
                ponto_reposicao_string = ''.join(map(str, ponto_reposicao))
                decimal_ponto_reposicao = int(ponto_reposicao_string, 2)
                label_decimal_pr = tk.Label(janela_gerar_problema, text="Ponto Reposição em decimal: {}".format(decimal_ponto_reposicao))
                label_decimal_pr.pack(pady=10)


    """   NA JANELA SOLUCAO   """

    def criar_janela_solucao_inicial(self):
        janela_solucao_inicial = tk.Toplevel(self.root)
        janela_solucao_inicial.title("Solução Inicial")
        janela_solucao_inicial.geometry("800x600")
        # Implemente a lógica para a solução inicial aqui

        # calcular a funcao objetivo
        def FuncaoObjetivo(media_demanda, estoque_diario, demanda_total, soma_deman_atend, a, b):

            a = 0.5
            b = 0.5

            demanda_total_entry = int(self.entry_demanda_total.get())
            estoque_diario_entry = int(self.entry_estoque_medio.get())
            soma_deman_atend_entry = int(self.entry_soma_atendido.get())
            media_demanda_entry = int(self.entry_media_demanda.get())

            media_demanda = media_demanda_entry
            estoque_diario = estoque_diario_entry
            demanda_total = demanda_total_entry
            soma_deman_atend = soma_deman_atend_entry

            # calcular o criterio economico
            criterio_economico = 2.71828**(math.log((10 ** -3 / 10 * media_demanda) * estoque_diario))

            # calcular o nivel de atendimento
            nivel_atendimento = soma_deman_atend/demanda_total

            # calcular funcao objetivo
            funcao_objetivo = (nivel_atendimento * a) + (criterio_economico * b)

            return criterio_economico, nivel_atendimento, funcao_objetivo

        criterio_economico, nivel_atendimento, funcao_objetivo = FuncaoObjetivo(0, 0, 0, 0, 0, 0)

        label_ce = tk.Label(janela_solucao_inicial, text="Critério Econômico: {}".format(criterio_economico))
        label_ce.pack(pady=10)

        label_na = tk.Label(janela_solucao_inicial, text="Nivel Atendimento: {}".format(nivel_atendimento))
        label_na.pack(pady=10)
            
        label_fo = tk.Label(janela_solucao_inicial, text="Função Objetivo: {}".format(funcao_objetivo))
        label_fo.pack(pady=10)        



    """   NA JANELA AVALIA   """

    def criar_janela_avalia(self):          
        janela_avalia = tk.Toplevel(self.root)
        janela_avalia.title("Avalia")
        janela_avalia.geometry("800x600")
            # Implemente a lógica para avaliação aqui

                
            

            # instanciar da classe Cromossomo
        def CromossomoAleatorio(cromossomo):

            for x in range(tamanho_cromossomo):
                    # gerar numeros aleatorios de 1 e 0
                cromossomo.genes[x] = random.randint(0 , 1)
                        

                    # pegar a saida da funcao
            

        def Aptidao(media_demanda):
            media_demanda = 50
            ponto_reposicao = 0
            tamanho_lote = 0

            tamanho_lote = cromossomo.genes[:tamanho_cromossomo // 2]
            tamanho_lote_string = ''.join(map(str, tamanho_lote))
            decimal_tamanho_lote = int(tamanho_lote_string, 2)
            ponto_reposicao = cromossomo.genes[tamanho_cromossomo //2:]
            ponto_reposicao_string = ''.join(map(str, ponto_reposicao))
            decimal_ponto_reposicao = int(ponto_reposicao_string, 2)
                # se o tamanho lote for menor que 2 x demanda media ou maior 10 x demanda media 
            if decimal_tamanho_lote < 2 * media_demanda or decimal_tamanho_lote >= 10 * media_demanda:
                return -9999
                
            if decimal_ponto_reposicao < 2 * media_demanda or decimal_ponto_reposicao >=10 * media_demanda:
                return -9999

        def SelecaoTorneio(populacao, media_demanda):

            torneio = random.sample(populacao, tamanho_torneio)
            vencedor = torneio[0]
            melhor_aptidao = Aptidao(vencedor, media_demanda)
            for cromossomo in torneio[1:]:
                atual_vencedor = Aptidao(cromossomo, media_demanda)
                if atual_vencedor > melhor_aptidao:
                    melhor_aptidao = atual_vencedor
                    vencedor = cromossomo
            return vencedor

            # realizar o cruzamento
        def Crossover(pai1, pai2):

            filho = Cromossomo()
            ponto_cruzamento = random.randint(0, tamanho_cromossomo)
            for x in range(tamanho_cromossomo):
                filho.genes[x] = pai1.genes[x] if x < ponto_cruzamento else pai2.genes[x]

                print("Pai (1): ",pai1)
                print("Pai (2): ",pai2)
                print("Filho: ",filho)

            return filho

        def Mutacao(cromossomo):
            for x in range(tamanho_cromossomo):
                if random.random() < taxa_mutacao:
                        # trocar bit
                    cromossomo.genes[x] = 1 - cromossomo.genes[x]

        # criar uma populacao
        populacao = [Cromossomo() for _ in range(tamanho_populacao)]
        for cromossomo in populacao:
                InicializarCromossomo(cromossomo)

            # criar geracoes
        for geracao in range(geracoes):
            media_demanda = 50
                # chamar as funcoes como torneio, crossover etc
            nova_populacao = []
            for _ in range(tamanho_populacao):
                pai1 = SelecaoTorneio(populacao, media_demanda)
                pai2 = SelecaoTorneio(populacao, media_demanda)
                filho = Crossover(pai1,pai2)
                Mutacao(filho)
            nova_populacao.append(filho)
                # atualizar nova populacao
            populacao = nova_populacao

            # melhor cromossomo
        melhor_cromossomo = populacao[0]
        melhor_aptidao = Aptidao(media_demanda)
        for cromossomo in populacao[1:]:
            atual_aptidao = Aptidao(media_demanda)
            if atual_aptidao > melhor_aptidao:
                melhor_aptidao = atual_aptidao
                melhor_aptidao = cromossomo

            ponto_reposicao = 0
            tamanho_lote = 0
            for x in range(tamanho_cromossomo //2):
                ponto_reposicao += melhor_cromossomo.genes[x] * (2 ** (tamanho_cromossomo // 2 - 1 - x))
            for x in range(tamanho_cromossomo // 2, tamanho_cromossomo):
                tamanho_lote += melhor_cromossomo.genes[x] * (2 ** (tamanho_cromossomo - 1 - x))

            # avaliacao
            print("Melhor ponto de reposição:", ponto_reposicao)
            print("Melhor tamanho de lote:", tamanho_lote)
            print("Melhor valor da função objetivo:", melhor_aptidao)

        label_melhor_pr = tk.Label(janela_avalia, text="Melhor ponto de reposição: {}".format(ponto_reposicao))
        label_melhor_pr.pack(pady=10)
            
        label_melhor_tl = tk.Label(janela_avalia, text="Melhor tamanho de lote: {}".format(tamanho_lote))
        label_melhor_tl.pack(pady=10)

        label_melhor_fo = tk.Label(janela_avalia, text="Melhor valor da função objetivo: {}".format(melhor_aptidao))
        label_melhor_fo.pack(pady=10)


if __name__ == "__main__":
    root = tk.Tk()
    app = GestaoEstoqueApp(root)
    root.mainloop()
