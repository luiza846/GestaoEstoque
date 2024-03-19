
import java.util.Random;


public class teste2DAO {
    static final int CHROMOSOME_LENGTH = 22;
    static final int POPULATION_SIZE = 100;
    static final double MUTATION_RATE = 0.01;
    static final int TOURNAMENT_SIZE = 5;
    static final int GENERATIONS = 100;

    // Classe para representar um cromossomo
    static class Chromosome {
        int[] genes = new int[CHROMOSOME_LENGTH];
    }

    // Função objetivo
    static double objectiveFunction(int[] demanda, int pontoReposicao, int tamanhoLote, double a, double b, int prioridade) {
        double nivelAtendimento = (double) (demanda[0] + demanda[1]) / demanda[2];
        double criterioEconomico = Math.exp((Math.log((Math.pow(10, -3)) / (10 * demanda[1])) * demanda[0]));
        if (prioridade == 1) {
            if (tamanhoLote < pontoReposicao) return Double.NEGATIVE_INFINITY;
        } else {
            if (tamanhoLote >= pontoReposicao) return Double.NEGATIVE_INFINITY;
        }
        return (nivelAtendimento * a) + (criterioEconomico * b);
    }

    // Função para inicializar um cromossomo aleatório
    static void initializeChromosome(Chromosome chromosome) {
        Random random = new Random();
        for (int i = 0; i < CHROMOSOME_LENGTH; i++) {
            chromosome.genes[i] = random.nextInt(2); // Bit aleatório 0 ou 1
        }
    }

    // Função para calcular a aptidão de um cromossomo
    static double fitness(Chromosome chromosome, int[] demanda, double a, double b, int prioridade) {
        int pontoReposicao = 0;
        int tamanhoLote = 0;
        // Decodificação do cromossomo para ponto de reposição e tamanho do lote
        for (int i = 0; i < CHROMOSOME_LENGTH / 2; i++) {
            pontoReposicao += chromosome.genes[i] * Math.pow(2, CHROMOSOME_LENGTH / 2 - 1 - i);
        }
        for (int i = CHROMOSOME_LENGTH / 2; i < CHROMOSOME_LENGTH; i++) {
            tamanhoLote += chromosome.genes[i] * Math.pow(2, CHROMOSOME_LENGTH - 1 - i);
        }
        // Checagem das restrições
        if (pontoReposicao < 2 * demanda[1] || pontoReposicao > 10 * demanda[1] ||
                tamanhoLote < 2 * demanda[1] || tamanhoLote > 10 * demanda[1]) {
            return Double.NEGATIVE_INFINITY; // Penalização para cromossomos inválidos
        }
        // Cálculo da função objetivo
        return objectiveFunction(demanda, pontoReposicao, tamanhoLote, a, b, prioridade);
    }

    // Função para realizar o torneio para seleção de pais
    static Chromosome tournamentSelection(Chromosome[] population, int[] demanda, double a, double b, int prioridade) {
        Chromosome[] tournament = new Chromosome[TOURNAMENT_SIZE];
        Random random = new Random();
        // Seleção de cromossomos aleatórios para o torneio
        for (int i = 0; i < TOURNAMENT_SIZE; i++) {
            tournament[i] = population[random.nextInt(POPULATION_SIZE)];
        }
        // Encontrar o cromossomo mais apto no torneio
        Chromosome winner = tournament[0];
        double bestFitness = fitness(winner, demanda, a, b, prioridade);
        for (int i = 1; i < TOURNAMENT_SIZE; i++) {
            double currentFitness = fitness(tournament[i], demanda, a, b, prioridade);
            if (currentFitness > bestFitness) {
                bestFitness = currentFitness;
                winner = tournament[i];
            }
        }
        return winner;
    }

    // Função para realizar o crossover de dois pais
    static Chromosome crossover(Chromosome parent1, Chromosome parent2) {
        Chromosome child = new Chromosome();
        Random random = new Random();
        // Ponto de crossover aleatório
        int crossoverPoint = random.nextInt(CHROMOSOME_LENGTH);
        for (int i = 0; i < CHROMOSOME_LENGTH; i++) {
            if (i < crossoverPoint) {
                child.genes[i] = parent1.genes[i];
            } else {
                child.genes[i] = parent2.genes[i];
            }
        }
        return child;
    }

    // Função para realizar a mutação de um cromossomo
    static void mutate(Chromosome chromosome) {
        Random random = new Random();
        for (int i = 0; i < CHROMOSOME_LENGTH; i++) {
            if (random.nextDouble() < MUTATION_RATE) {
                chromosome.genes[i] = 1 - chromosome.genes[i]; // Troca do bit
            }
        }
    }

    public static void main(String[] args) {
        // Definição da demanda média diária, a e b
        int[] demanda = {50, 10, 200};
        double a = 1.0;
        double b = 1.0;

        // Definição da prioridade (1 para NA>CE, 2 para CE>NA)
        int prioridade = 1;

        // Inicialização da população inicial
        Chromosome[] population = new Chromosome[POPULATION_SIZE];
        for (int i = 0; i < POPULATION_SIZE; i++) {
            population[i] = new Chromosome();
            initializeChromosome(population[i]);
        }

        // Loop principal do algoritmo genético
        for (int generation = 0; generation < GENERATIONS; generation++) {
            // Seleção, crossover e mutação para gerar a nova população
            Chromosome[] newPopulation = new Chromosome[POPULATION_SIZE];
            for (int i = 0; i < POPULATION_SIZE; i++) {
                Chromosome parent1 = tournamentSelection(population, demanda, a, b, prioridade);
                Chromosome parent2 = tournamentSelection(population, demanda, a, b, prioridade);
                Chromosome child = crossover(parent1, parent2);
                mutate(child);
                newPopulation[i] = child;
            }
            // Atualização da população
            for (int i = 0; i < POPULATION_SIZE; i++) {
                population[i] = newPopulation[i];
            }
        }

        // Encontrar o cromossomo mais apto na população final
        Chromosome bestChromosome = population[0];
        double bestFitness = fitness(bestChromosome, demanda, a, b, prioridade);
        for (int i = 1; i < POPULATION_SIZE; i++) {
            double currentFitness = fitness(population[i], demanda, a, b, prioridade);
            if (currentFitness > bestFitness) {
                bestFitness = currentFitness;
                bestChromosome = population[i];
            }
        }

        // Decodificação do melhor cromossomo
        int pontoReposicao = 0;
        int tamanhoLote = 0;
        for (int i = 0; i < CHROMOSOME_LENGTH / 2; i++) {
            pontoReposicao += bestChromosome.genes[i] * Math.pow(2, CHROMOSOME_LENGTH / 2 - 1 - i);
        }
        for (int i = CHROMOSOME_LENGTH / 2; i < CHROMOSOME_LENGTH; i++) {
            tamanhoLote += bestChromosome.genes[i] * Math.pow(2, CHROMOSOME_LENGTH - 1 - i);
        }

        // Impressão dos resultados
        System.out.println("Melhor ponto de reposição: " + pontoReposicao);
        System.out.println("Melhor tamanho de lote: " + tamanhoLote);
        System.out.println("Melhor valor da função objetivo: " + bestFitness);
    }
}
