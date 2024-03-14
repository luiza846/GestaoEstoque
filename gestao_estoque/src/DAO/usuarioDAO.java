package DAO;

import DTO.usuarioDTO;

import java.sql.Connection;
import java.sql.ResultSet;
import java.sql.SQLException;
import javax.swing.JOptionPane;
import java.sql.PreparedStatement;

public class usuarioDAO {
    
    PreparedStatement pstm;
    Connection conn;

    //metodo autenticacaoUsuario
    public ResultSet auticacaoUsuario(usuarioDTO objusuariodto) {
        
        conn = new conexaoDAO().conectaBD();

        try {

            String sql = "select * from usuario where nome_usuario = ? and senha_usuario = ?";
            //preparando a conexao e passando o comando sql para ser executado
            PreparedStatement pstm = conn.prepareStatement(sql);
            pstm.setString(1, objusuariodto.getNome_usuario());//usuario
            pstm.setString(2, objusuariodto.getSenha_usuario());//senha
            
            ResultSet rs = pstm.executeQuery();
            return rs;
            
        } catch (SQLException erro) {
            JOptionPane.showMessageDialog(null, "Erro no Usuario DAO" + erro);
            return null;
        }

    }

    public usuarioDAO() {
    }
    
    public ResultSet listarPrioridade(){
        conn = new conexaoDAO().conectaBD();
        String sql = "select * from prioridade order by id_prioridade;";
        
        try {
            
            pstm = conn.prepareStatement(sql);
            return pstm.executeQuery();
            
        } catch (SQLException erro) {
            JOptionPane.showMessageDialog(null, "Erro ao listar prioridade"+erro.getMessage());
            return null;
        }
    }

}
