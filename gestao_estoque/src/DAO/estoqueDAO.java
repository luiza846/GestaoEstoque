package DAO;

import DTO.estoqueDTO;
import static java.lang.Math.exp;
import static java.lang.Math.log;
import static java.lang.Math.pow;
import java.sql.Connection;
import java.sql.PreparedStatement;
import javax.swing.JOptionPane;

public class estoqueDAO {

    Connection conn;
    PreparedStatement pstm;

    //metodo void porque nao vai ter retorno
    public void cadastrarDadosEstoque(estoqueDTO objestoque) {
        String sql = "insert into dados (media_demanda, estoque_diario, demanda_total, soma_dem_atendido, prioridade) values (?,?,?,?,?)";

        //chamar o metodo conectaBD na classe conexaoDAO
        conn = new conexaoDAO().conectaBD();

        try {

            pstm = conn.prepareStatement(sql);
            pstm.setInt(1, objestoque.getMedia_demanda());
            pstm.setInt(2, objestoque.getEstoque_diario());
            pstm.setInt(3, objestoque.getDemanda_total());
            pstm.setInt(4, objestoque.getSoma_dem_atendido());
            pstm.setString(5, objestoque.getPrioridade());

            pstm.execute();
            pstm.close();
            JOptionPane.showMessageDialog(null, "Cadastrado com sucesso!");

        } catch (Exception erro) {
            JOptionPane.showMessageDialog(null, "Erro no estoqueDAO" + erro);
        }
    }

    private static final int CHROMOSOME_LENGTH = 22;
    private static final int POPULATION_SIZE = 100;
    private static final double MUTATION_RATE = 0.01;
    private static final int TOURNAMENT_SIZE = 5;
    private static final int GENERATIONS = 100;

    private int[] genes;

    public void Chromosome() {
        this.genes = new int[CHROMOSOME_LENGTH];
    }

    int[] getGenes() {
        return genes;
    }

    public void setGenes(int[] genes) {
        this.genes = genes;
    }

    public double funcaoObjetivo(int mediaDemanda, int estoqueMedio, int demandaTotal, int ponto_reposicao, int tamanho_lote, double a, double b, int prioridade) {
        double negativoInfinito = Double.NEGATIVE_INFINITY;
        double nivel_atendimento = (double) mediaDemanda / demandaTotal;
        double criterio_economico = exp(pow(2.71828, ((log((pow(10, -3)) / (10 * mediaDemanda)) * estoqueMedio))));
        if (prioridade == 1) {
            if (tamanho_lote < ponto_reposicao) {
                return negativoInfinito;
            }
        } else {
            if (tamanho_lote >= ponto_reposicao) {
                return negativoInfinito;
            }
        }
        return (nivel_atendimento * a) + (criterio_economico * b);
    }
    // Função para inicializar um cromossomo aleatório
/*
    void initialize_chromosome(Chromosome  
        *chromosome) {
    for (int i = 0; i < CHROMOSOME_LENGTH; i++) {
            chromosome -> genes[i] = rand() % 2; // Bit aleatório 0 ou 1
        }
    }*/
    public void gerarCromossomoAleatorio (){
        
    }
}
