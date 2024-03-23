import random as rd

def GerarProblema(media_demanda,estoque_medio,demanda_total,soma_deman_atend,min_p1,max_p1,min_p2,max_p2,min_p3,max_p3):
    tp = []
    pr = []
    tl = []
    
    for i in range(media_demanda,estoque_medio,demanda_total,soma_deman_atend):
        tp.append(rd.randint(min_p1,max_p1))
    
    for i in range(media_demanda,estoque_medio,demanda_total,soma_deman_atend):
        pr.append(rd.randint(min_p2,max_p2))
    
    for i in range(media_demanda,estoque_medio,demanda_total,soma_deman_atend):
        tl.append(rd.randint(min_p3,max_p3))
    
    return tp, pr, tl

media_demanda = int(input("Media demanda diaria: "))
estoque_medio = int(input("Estoque Médio: "))
demanda_total = int(input("Demanda Total: "))
soma_deman_atend = int(input("Soma de Demanda Atendido: "))
# tempo de processamento
min_p1 = 2
max_p1 = 9
# ponto de reposicao
min_p2 = 7
max_p2 = 30
# tamanho lote
min_p3 = 2
max_p3 = 10

c_max = 50

pe1, pe2, pe3 = GerarProblema(media_demanda,estoque_medio,demanda_total,soma_deman_atend,min_p1,max_p1,min_p2,max_p2,min_p3,max_p3)
print("Problema:")
print(pe1,pe2,pe3)