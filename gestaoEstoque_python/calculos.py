import math
import random
import random as rd

tamanho_cromossomo = 22
tamanho_torneio = 5
taxa_mutacao = 0.01
tamanho_populacao = 100
geracoes = 100

# atribuir valores (tirar depois)
soma_dem_atend = 60
estoque_diario = 50
media_demanda = 10
demanda_total = 200


class Cromomossomo:
    def __init__(crom):
        crom.genes = [0] * tamanho_cromossomo

# calcular a funcao objetivo
def FuncaoObjetivo(media_demanda, estoque_diario, demanda_total, soma_deman_atend, a, b, funcao_objetivo):

    a = 0,7
    b = 0,3

    # calcular o criterio economico
    criterio_economico = math.exp((math.log((10 ** -3) / (10 * media_demanda)) * estoque_diario))

    # calcular o nivel de atendimento
    nivel_atendimento = soma_deman_atend/demanda_total

    # calcular funcao objetivo
    funcao_objetivo = (nivel_atendimento * a) + (criterio_economico * b)

    return funcao_objetivo

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


def Aptidao(media_demanda, tamanho_lote, ponto_reposicao):
    
    # se o tamanho lote for menor que 2 x demanda media ou maior 10 x demanda media 
    if tamanho_lote < 2 * media_demanda or 10 * media_demanda:
        return -9999
    
    if ponto_reposicao < 2 * media_demanda or 10 * media_demanda:
        return -9999
    
def SelecaoTorneio(populacao):

    torneio = random.sample(populacao, tamanho_torneio)
    vencedor = torneio[0]
    melhor_aptidao = Aptidao(vencedor, media_demanda)
    for cromossomo in torneio[1:]:
        atual_vencedor = Aptidao(cromossommo, media_demanda)
        if atual_vencedor > melhor_aptidao:
            melhor_aptidao = atual_vencedor
            vencedor = cromossommo

    return vencedor

# realizar o cruzamento
def Crossover(pai1, pai2):

    filho = Cromomossomo()
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
            cromossommo.genes[x] = 1 - cromossommo.genes[x]

# criar uma populacao
populacao = [Cromomossomo() for _ in range(tamanho_populacao)]
for cromossomo in populacao:
    InicializarCromossomo(cromossommo)

# criar geracoes
for geracao in range(geracoes):
    # chamar as funcoes como torneio, crossover etc
    nova_populacao = []
    for _ in range(tamanho_populacao):
        pai1 = SelecaoTorneio(populacao)
        pai2 = SelecaoTorneio(populacao)
        filho = Crossover(pai1,pai2)
        Mutacao(filho)
        nova_populacao.append(filho)
    # atualizar nova populacao
        populacao = nova_populacao

# melhor cromossomo
melhor_cromossomo = populacao[0]
melhor_aptidao = Aptidao(media_demanda, tamanho_lote, ponto_reposicao)
for cromossomo in populacao[1:]:
    atual_aptidao = Aptidao(media_demanda, tamanho_lote, ponto_reposicao)
    if atual_aptidao > melhor_aptidao:
        melhor_aptidao = atual_aptidao
        melhor_aptidao = cromossommo

ponto_reposicao = 0
tamanho_lote = 0
for x in range(tamanho_cromossomo //2):
    ponto_reposicao += melhor_cromossomo.genes[x] * (2 ** (tamanho_cromossomo // 2 - 1 - x))
for x in range(tamanho_cromossomo // 2, tamanho_cromossomo):
    tamanho_lote += melhor_cromossomo.genes[x] * (2 ** (tamanho_cromossomo - 1 - x))

# avaliacao
print("Melhor ponto de reposição:", ponto_reposicao)
print("Melhor tamanho de lote:", tamanho_lote)
print("Melhor valor da função objetivo:", best_fitness)


# instanciar a classe Cromossomo
cromossommo = Cromomossomo()

# chamar a funcao Inicializar Cromossomo
InicializarCromossomo(cromossommo)

# chamar a funcao Aptidao
Crossover(cromossommo)