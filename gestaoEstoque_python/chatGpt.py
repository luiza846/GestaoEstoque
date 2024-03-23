import random
import math

CHROMOSOME_LENGTH = 22
POPULATION_SIZE = 100
MUTATION_RATE = 0.01
TOURNAMENT_SIZE = 5
GENERATIONS = 100

# Classe para representar um cromossomo
class Chromosome:
    def __init__(self):
        self.genes = [0] * CHROMOSOME_LENGTH

# Função objetivo
def objective_function(soma_dem_atendido, demanda_total, media_demanda, estoque_diario, ponto_reposicao, tamanho_lote, a, b, prioridade):
    nivel_atendimento = soma_dem_atendido / demanda_total
    criterio_economico = math.exp((math.log((10 ** -3) / (10 * media_demanda)) * estoque_diario))
    if prioridade == 1:
        if tamanho_lote < ponto_reposicao:
            return float('-inf')
    else:
        if tamanho_lote >= ponto_reposicao:
            return float('-inf')
    return (nivel_atendimento * a) + (criterio_economico * b)

# Função para inicializar um cromossomo aleatório
def initialize_chromosome(chromosome):
    for i in range(CHROMOSOME_LENGTH):
        chromosome.genes[i] = random.randint(0, 1) # Bit aleatório 0 ou 1
        print(chromosome.genes)

# Função para calcular a aptidão de um cromossomo
def fitness(chromosome, media_demanda, a, b, prioridade):
    ponto_reposicao = 0
    tamanho_lote = 0
    # Decodificação do cromossomo para ponto de reposição e tamanho do lote
    for i in range(CHROMOSOME_LENGTH // 2):
        ponto_reposicao += chromosome.genes[i] * (2 ** (CHROMOSOME_LENGTH // 2 - 1 - i))
    for i in range(CHROMOSOME_LENGTH // 2, CHROMOSOME_LENGTH):
        tamanho_lote += chromosome.genes[i] * (2 ** (CHROMOSOME_LENGTH - 1 - i))
    # Checagem das restrições
    if ponto_reposicao < 2 * media_demanda or ponto_reposicao > 10 * media_demanda or \
            tamanho_lote < 2 * media_demanda or tamanho_lote > 10 * media_demanda:
        return float('-inf') # Penalização para cromossomos inválidos
    # Cálculo da função objetivo
    return objective_function(soma_dem_atendido, demanda_total, media_demanda, estoque_diario, ponto_reposicao, tamanho_lote, a, b, prioridade)

# Função para realizar o torneio para seleção de pais
def tournament_selection(population, media_demanda, a, b, prioridade):
    tournament = random.sample(population, TOURNAMENT_SIZE)
    winner = tournament[0]
    best_fitness = fitness(winner, media_demanda, a, b, prioridade)
    for chromosome in tournament[1:]:
        current_fitness = fitness(chromosome, media_demanda, a, b, prioridade)
        if current_fitness > best_fitness:
            best_fitness = current_fitness
            winner = chromosome
    return winner


# Função para realizar o crossover de dois pais
def crossover(parent1, parent2):
    child = Chromosome()
    crossover_point = random.randint(0, CHROMOSOME_LENGTH)
    for i in range(CHROMOSOME_LENGTH):
        child.genes[i] = parent1.genes[i] if i < crossover_point else parent2.genes[i]
    return child

# Função para realizar a mutação de um cromossomo
def mutate(chromosome):
    for i in range(CHROMOSOME_LENGTH):
        if random.random() < MUTATION_RATE:
            chromosome.genes[i] = 1 - chromosome.genes[i] # Troca do bit

# Definição da demanda média diária, a e b
soma_dem_atendido = 60
estoque_diario = 50
media_demanda = 10
demanda_total = 200
a = 1.0
b = 1.0

# Definição da prioridade (1 para NA>CE, 2 para CE>NA)
prioridade = 1

# Inicialização da população inicial
population = [Chromosome() for _ in range(POPULATION_SIZE)]
for chromosome in population:
    initialize_chromosome(chromosome)

# Loop principal do algoritmo genético
for generation in range(GENERATIONS):
    # Seleção, crossover e mutação para gerar a nova população
    new_population = []
    for _ in range(POPULATION_SIZE):
        parent1 = tournament_selection(population, media_demanda, a, b, prioridade)
        parent2 = tournament_selection(population, media_demanda, a, b, prioridade)
        child = crossover(parent1, parent2)
        mutate(child)
        new_population.append(child)
    # Atualização da população
    population = new_population

# Encontrar o cromossomo mais apto na população final
best_chromosome = population[0]
best_fitness = fitness(best_chromosome, media_demanda, a, b, prioridade)
for chromosome in population[1:]:
    current_fitness = fitness(chromosome, media_demanda, a, b, prioridade)
    if current_fitness > best_fitness:
        best_fitness = current_fitness
        best_chromosome = chromosome
        

# Decodificação do melhor cromossomo
ponto_reposicao = 0
tamanho_lote = 0
for i in range(CHROMOSOME_LENGTH // 2):
    ponto_reposicao += best_chromosome.genes[i] * (2 ** (CHROMOSOME_LENGTH // 2 - 1 - i))
for i in range(CHROMOSOME_LENGTH // 2, CHROMOSOME_LENGTH):
    tamanho_lote += best_chromosome.genes[i] * (2 ** (CHROMOSOME_LENGTH - 1 - i))

# Impressão dos resultados
print("Melhor ponto de reposição:", ponto_reposicao)
print("Melhor tamanho de lote:", tamanho_lote)
print("Melhor valor da função objetivo:", best_fitness)
