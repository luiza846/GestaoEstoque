
package DTO;


public class estoqueDTO {
    
    private int media_demanda, estoque_diario, demanda_total, soma_dem_atendido;
    private String prioridade;

    public int getMedia_demanda() {
        return media_demanda;
    }

    public void setMedia_demanda(String media_demanda) {
        int valor_inteiro = Integer.parseInt(media_demanda);
        this.media_demanda = valor_inteiro;
    }

    public int getEstoque_diario() {
        return estoque_diario;
    }

    public void setEstoque_diario(String estoque_diario) {
        int valor_inteiro = Integer.parseInt(estoque_diario);
        this.estoque_diario = valor_inteiro;
    }

    public int getDemanda_total() {
        return demanda_total;
    }

    public void setDemanda_total(String demanda_total) {
        int valor_inteiro = Integer.parseInt(demanda_total);
        this.demanda_total = valor_inteiro;
    }

    public int getSoma_dem_atendido() {
        return soma_dem_atendido;
    }

    public void setSoma_dem_atendido(String soma_dem_atendido) {
        int valor_inteiro = Integer.parseInt(soma_dem_atendido);
        this.soma_dem_atendido = valor_inteiro;
    }

    public String getPrioridade() {
        return prioridade;
    }

    public void setPrioridade(String prioridade) {
        this.prioridade = prioridade;
    }
}
