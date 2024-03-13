package DAO;

import DTO.estoqueDTO;
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
    public void calcularFuncaoObjeivo(){
        
    }
}
