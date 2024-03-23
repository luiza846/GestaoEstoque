import math
import random


tamanho_cromossomo = 22

class Cromomossomo:
    def __init__(crom):
        crom.genes = [0] * tamanho_cromossomo

def FuncaoObjetivo(media_demanda, estoque_diario, demanda_total, soma_deman_atend, a, b, funcao_objetivo):

    a = 0,7
    b = 0,3

    # calcular o criterio economico
    criterio_economico = math.exp((math.log((10 ** -3) / (10 * media_demanda)) * estoque_diario))

    # calcular o nivel de atendimento
    nivel_atendimento = soma_deman_atend/demanda_total

    # calcular funcao objetivo
    funcao_objetivo = (nivel_atendimento * a) + (criterio_economico * b)

    return (funcao_objetivo)


    def InicializarCromossomo(cromossomo):

        # gerar cromossomos aleatorios utilizando 0 e 1
        for x in range(tamanho_cromossomo):
            cromossomo.genes[x] = random.randint (0,1)
            print(cromossomo.genes)

    def Aptidao()
            # eu pensei em colocar metodos dentro dos ifs, se a prioridade for NA, entao ao gerar numeros aleatorios, o TL tera que ser maior que PR 

            # se a prioridade for nivel de atendimento
            if(prioridade == 1):
                if(tamanho_lote > ponto_reposicao):
                     

            # se a prioridade for criterio economico
            if(prioridade == 2):
                if(tamanho_lote < ponto_reposicao):