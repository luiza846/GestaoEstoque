import tkinter as tk
from PIL import Image, ImageTk

class GestaoEstoqueApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestão de Estoque")
        self.root.geometry("800x600")

        # Carregar a imagem de fundo
        imagem_fundo = Image.open("C:/Users/analu/OneDrive - Fatec Centro Paula Souza/5º PERÍODO/Programação Linear/GestaoEstoque/gestaoEstoque_python/interfaceI.png")
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

        # Frame para os botões
        self.frame_botoes = tk.Frame(self.canvas, bd=0, highlightthickness=0)
        self.frame_botoes.place(relx=0.88, rely=0.8, anchor="e")

        # Botões
        self.botao_gerar_problema = tk.Button(self.frame_botoes, text="Gerar Problema", command=self.criar_janela_gerar_problema)
        self.botao_gerar_problema.pack(side=tk.RIGHT, padx=3)

        self.botao_solucao_inicial = tk.Button(self.frame_botoes, text="Solução Inicial", command=self.criar_janela_solucao_inicial)
        self.botao_solucao_inicial.pack(side=tk.RIGHT, padx=3)

        self.botao_avalia = tk.Button(self.frame_botoes, text="Avalia", command=self.criar_janela_avalia)
        self.botao_avalia.pack(side=tk.RIGHT, padx=3)

    def criar_janela_gerar_problema(self):
        janela_gerar_problema = tk.Toplevel(self.root)
        janela_gerar_problema.title("Gerar Problema")
        janela_gerar_problema.geometry("800x600")
        # Implemente a lógica para gerar o problema aqui

    def criar_janela_solucao_inicial(self):
        janela_solucao_inicial = tk.Toplevel(self.root)
        janela_solucao_inicial.title("Solução Inicial")
        janela_solucao_inicial.geometry("800x600")
        # Implemente a lógica para a solução inicial aqui

    def criar_janela_avalia(self):
        janela_avalia = tk.Toplevel(self.root)
        janela_avalia.title("Avalia")
        janela_avalia.geometry("800x600")
        # Implemente a lógica para avaliação aqui

if __name__ == "__main__":
    root = tk.Tk()
    app = GestaoEstoqueApp(root)
    root.mainloop()
