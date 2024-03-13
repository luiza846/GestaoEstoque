package DAO;


import java.sql.Connection;
import javax.swing.JOptionPane;
import java.sql.DriverManager;
import java.sql.SQLException;

public class conexaoDAO {

    //metodo conexaoBD tipo Connection
    public Connection conectaBD() {
        //variavel conn
        Connection conn = null;

        try {
            //conexao com banco de dados
            
            String url = "jdbc:mysql://localhost:3306/estoque?user=root&password=";
            conn = DriverManager.getConnection(url);
            
            /*
                ou pode ser representado dessa forma:
                conn = DriverManager.getConnection("jdbc:mysql://localhost:3306//bancoteste?user=root&password=");
            */
            
            
        } catch (SQLException erro) {
            //metodo para exibir erro de conexao
            JOptionPane.showMessageDialog(null,"Erro na conexaoDAO"+ erro.getMessage());
        }
        return conn;

    }
}
