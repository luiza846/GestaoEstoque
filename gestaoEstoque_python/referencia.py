def Aptidao(tamanho_lote, ponto_reposicao, prioridade):
    if prioridade == 1:
        # se a prioridade for nivel de atendimento
        for tl, pr in zip(tamanho_lote, ponto_reposicao):
            if tl > pr:
                print("Aptidao: Tamanho Lote", tl, " Ponto de Reposição: ", pr)

    elif prioridade == 2:
        # se a prioridade for critério econômico
        for tl, pr in zip(tamanho_lote, ponto_reposicao):
            if tl < pr:
                print("Aptidao: Tamanho Lote", tl, " Ponto de Reposição: ", pr)

# Não precisamos receber a prioridade como um parâmetro da função Aptidao, pois você está solicitando-a dentro da função.
# Remova também a chamada para input dentro da função.


# Exemplo de uso:
prioridade = int(input("Prioridade 1 = Nivel de Atendimento e Prioridade 2 = Critério Economico: "))
Aptidao(tamanho_lote, ponto_reposicao, prioridade)
