package DAO;

import static java.lang.Math.exp;
import static java.lang.Math.log;
import static java.lang.Math.pow;
import static java.lang.Math.random;
import static java.lang.StrictMath.random;


public class testeDAO {

    private int tamanho_cromossomo = 22;
    private int tamanho_populacao = 100;
    private double mutacao = 0.01;
    private int torneio = 5;
    public int geracoes = 100;

    //representacao de cromossomo
    public testeDAO () {
        int[] genes = new int[tamanho_cromossomo];
    }

    //calcular funcao objetivo
    public double funcaoObjetivo(double negativoInfinito, int media_demanda, int estoque_diario, int demanda_total, int soma_dem_atendido, int ponto_reposicao, int tamanho_lote, double a, double b, int prioridade) {
        double nivel_atendimento, criterio_economico;
        //usuario entra com os valore de soma dem atend demanda total
        nivel_atendimento = (double) soma_dem_atendido / demanda_total;
        criterio_economico = exp(pow(2.718, (log((pow(10, -3)) / (10 * media_demanda)) * estoque_diario)));

        //prioridade
        if (prioridade == 1 && tamanho_lote < ponto_reposicao) {
            if (tamanho_lote < ponto_reposicao) return Double.NEGATIVE_INFINITY;
        } else {
            if (tamanho_lote >= ponto_reposicao) return Double.NEGATIVE_INFINITY;
        }
        //funcao objetivo
        return (nivel_atendimento * a) + (criterio_economico * b);
    }
    
    public void inicializarCromossomo(testeDAO cromossomo)
    {
        for(int vetor=0;vetor <= tamanho_cromossomo;vetor++)
        {
            cromossomo.genes[vetor] = (int) (Math.random() * 2);
            System.out.println(cromossomo.genes[vetor]);
        }
    }
    public static void main(String[] args) {
        testeDAO obj = new testeDAO();
        obj.funcaoObjetivo(0, 0, 0, 0, 0, 0, 0, 0, 0, 0);
    }
}
