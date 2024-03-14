
package DTO;


public class prioridadeDTO {
    
    private int idPrioridade;
    private String nivelAtendimento;
    private String criterioEconimico;

    public String getNivelAtendimento() {
        return nivelAtendimento;
    }

    public void setNivelAtendimento(String nivelAtendimento) {
        this.nivelAtendimento = nivelAtendimento;
    }

    public String getCriterioEconimico() {
        return criterioEconimico;
    }

    public void setCriterioEconimico(String criterioEconimico) {
        this.criterioEconimico = criterioEconimico;
    }

    public int getIdPrioridade() {
        return idPrioridade;
    }

    public void setIdPrioridade(int idPrioridade) {
        this.idPrioridade = idPrioridade;
    }
}
