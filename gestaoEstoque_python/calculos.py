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

    # gerar problema p/ tamanho lote
    for i in range(n):
        tamanho_lote.append(rd.randint(min_tl,max_tl))
    print("Cromossomo Tamanho Lote: ",tamanho_lote)

    # gerar problema p/ ponto de reposicao
    for i in range(n):
        ponto_reposicao.append(rd.randint(min_pr,max_pr))
    print("Cromossomo Ponto de Reposicao: ",ponto_reposicao)

    return tamanho_lote, ponto_reposicao

# Exemplo de uso:
min_tl = 2
max_tl = 10
min_pr = 0
max_pr = 100
tamanho_lote, ponto_reposicao = GerarProblema(n, min_tl, max_tl, min_pr, max_pr)

