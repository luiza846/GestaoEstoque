import math
import random
import random as rd

tamanho_cromossomo = 22

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

# tamanho do problema
n = int(input("Tamanho do problema: "))

# gerar um cromossomo de 22 genes
def GerarProblema(n, min_tl, max_tl, min_pr, max_pr):

    tamanho_lote = []
    ponto_reposicao = []

    # restricao para tamanho lote (minimo 2 e maximo 10)
    min_tl = 2
    max_tl = 10

    # restricao para ponto de reposicao
    min_pr = 2
    max_pr = 10
    
    # gerar problema p/ tamanho lote
    for i in range(n):
        tamanho_lote.append(rd.randint(min_tl,max_tl))
    print("Cromossomo Tamanho Lote: ",tamanho_lote)

    # gerar problema p/ ponto de reposicao
    for i in range(n):
        ponto_reposicao.append(rd.randint(min_pr,max_pr))
    print("Cromossomo Ponto de Reposicao: ",ponto_reposicao)

    return tamanho_lote, ponto_reposicao

# tamanho lote
min_tl = 2
max_tl = 10

# ponto de reposicao
min_pr = 2
max_pr = 10

# chamar a funcao GerarProblema
tamanho_lote, ponto_reposicao = GerarProblema(n, min_tl, max_tl, min_pr, max_pr)

# funcao aptidao
def Aptidao (tamanho_lote, ponto_reposicao, prioridade):

    if(prioridade == 1):
        # se a prioridade for nivel de atendimento
        for tl, pr in zip(tamanho_lote, ponto_reposicao):
            if(tl > pr):
                print("Tamanho Lote = ",tl," Ponto de Reposição = ",pr)

    if(prioridade == 2):
        # se a prioridade for nivel de atendimento
        for tl, pr in zip(tamanho_lote, ponto_reposicao):
            if(tl < pr):
                print("Aptidao: Tamanho Lote",tl," Ponto de Reposição: ",pr)

# escolher a prioridade
prioridade = int(input("Prioridade 1 = Nivel de Atendimento e Prioridade 2 = Critério Economico: "))

print("\nAptidao:\n ")
# chamar a funcao Aptidao
Aptidao(tamanho_lote, ponto_reposicao, prioridade)