/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/GUIForms/JFrame.java to edit this template
 */
package VIEW;

import DTO.usuarioDTO;
import DAO.usuarioDAO;
import java.sql.SQLException;
import javax.swing.JOptionPane;
import java.sql.ResultSet;

/**
 *
 * @author analu
 */
public class frmLoginVIEW extends javax.swing.JFrame {

    /**
     * Creates new form frmLoginVIEW
     */
    public frmLoginVIEW() {
        initComponents();
    }

    /**
     * This method is called from within the constructor to initialize the form.
     * WARNING: Do NOT modify this code. The content of this method is always
     * regenerated by the Form Editor.
     */
    @SuppressWarnings("unchecked")
    // <editor-fold defaultstate="collapsed" desc="Generated Code">//GEN-BEGIN:initComponents
    private void initComponents() {

        txtNomeUsuario = new javax.swing.JTextField();
        txtSenhaUsuario = new javax.swing.JTextField();
        btnEntrarSistema = new javax.swing.JButton();
        jLabel3 = new javax.swing.JLabel();

        setDefaultCloseOperation(javax.swing.WindowConstants.EXIT_ON_CLOSE);
        getContentPane().setLayout(new org.netbeans.lib.awtextra.AbsoluteLayout());
        getContentPane().add(txtNomeUsuario, new org.netbeans.lib.awtextra.AbsoluteConstraints(450, 260, 220, 30));
        getContentPane().add(txtSenhaUsuario, new org.netbeans.lib.awtextra.AbsoluteConstraints(450, 340, 220, 30));

        btnEntrarSistema.setText("ENTRAR");
        btnEntrarSistema.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                btnEntrarSistemaActionPerformed(evt);
            }
        });
        getContentPane().add(btnEntrarSistema, new org.netbeans.lib.awtextra.AbsoluteConstraints(490, 420, 120, -1));

        jLabel3.setIcon(new javax.swing.ImageIcon(getClass().getResource("/IMAGES/login.png"))); // NOI18N
        getContentPane().add(jLabel3, new org.netbeans.lib.awtextra.AbsoluteConstraints(0, 0, 800, 600));

        pack();
    }// </editor-fold>//GEN-END:initComponents

    private void btnEntrarSistemaActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_btnEntrarSistemaActionPerformed
        try {
            // get no usuario e senha
            String nome_usuario, senha_usuario;

            //daclarando a variavel do textField
            nome_usuario = txtNomeUsuario.getText();
            senha_usuario = txtSenhaUsuario.getText();

            usuarioDTO objusuariodto = new usuarioDTO();

            //pegar o valor (campo usuario e senha) que usuario inseriu e comparar com o do banco de dados
            objusuariodto.setNome_usuario(nome_usuario);
            objusuariodto.setSenha_usuario(senha_usuario);
            
            //acessar a classe DAO
            usuarioDAO objusuariodao = new usuarioDAO();
            ResultSet rsusuariodao = objusuariodao.auticacaoUsuario(objusuariodto);

            if (rsusuariodao.next()) {
                //chamar tela que eu quero abrir
                frmPrincipalVIEW objfrmprincipalview = new frmPrincipalVIEW();
                objfrmprincipalview.setVisible(true);
                
                //fechar a tela de login
                dispose();
            }else{
                //enviar mensagem dizendo incorreto
                JOptionPane.showMessageDialog(null, "Usuário ou senha unválida");
            }
        } catch (SQLException erro) {
            JOptionPane.showMessageDialog(null,"Erro na Tela Login"+ erro);
        }
    }//GEN-LAST:event_btnEntrarSistemaActionPerformed

    /**
     * @param args the command line arguments
     */
    public static void main(String args[]) {
        /* Set the Nimbus look and feel */
        //<editor-fold defaultstate="collapsed" desc=" Look and feel setting code (optional) ">
        /* If Nimbus (introduced in Java SE 6) is not available, stay with the default look and feel.
         * For details see http://download.oracle.com/javase/tutorial/uiswing/lookandfeel/plaf.html 
         */
        try {
            for (javax.swing.UIManager.LookAndFeelInfo info : javax.swing.UIManager.getInstalledLookAndFeels()) {
                if ("Nimbus".equals(info.getName())) {
                    javax.swing.UIManager.setLookAndFeel(info.getClassName());
                    break;
                }
            }
        } catch (ClassNotFoundException ex) {
            java.util.logging.Logger.getLogger(frmLoginVIEW.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        } catch (InstantiationException ex) {
            java.util.logging.Logger.getLogger(frmLoginVIEW.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        } catch (IllegalAccessException ex) {
            java.util.logging.Logger.getLogger(frmLoginVIEW.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        } catch (javax.swing.UnsupportedLookAndFeelException ex) {
            java.util.logging.Logger.getLogger(frmLoginVIEW.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        }
        //</editor-fold>

        /* Create and display the form */
        java.awt.EventQueue.invokeLater(new Runnable() {
            public void run() {
                new frmLoginVIEW().setVisible(true);
            }
        });
    }

    // Variables declaration - do not modify//GEN-BEGIN:variables
    private javax.swing.JButton btnEntrarSistema;
    private javax.swing.JLabel jLabel3;
    private javax.swing.JTextField txtNomeUsuario;
    private javax.swing.JTextField txtSenhaUsuario;
    // End of variables declaration//GEN-END:variables
}
