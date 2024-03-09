/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package dto;

import java.util.Scanner;

/**
 *
 * @author analu
 */
public class gestaoEstoque {

    public int mediaDemanda, estoqueMedio, demandaTotal, somaDemandAtendimento;
    public float a, b, aa, ce, na, fo, e;
    public Scanner s;

    public gestaoEstoque() {

        //parametros de ponderacao
        a = (float) 0.7;
        b = (float) 0.3;

        mediaDemanda = estoqueMedio = demandaTotal = somaDemandAtendimento = 0;
        s = new Scanner(System.in);

        aa = ce = na = fo = 0;

        //euler
        e = (float) 2.718;

    }

    public void lerDados() {

        System.out.println("Digite a media de demanda: ");
        mediaDemanda = s.nextInt();
        System.out.println("Digite o estoque medio: ");
        estoqueMedio = s.nextInt();
        System.out.println("Digite a demanda total: ");
        demandaTotal = s.nextInt();
        System.out.println("Digite soma de demanda atendido: ");
        somaDemandAtendimento = s.nextInt();

    }

    public void prioridadeGestao() {
        //ainda colocar a condicao aqui
    }

    public void calcularCriterioEconomico() {

        //calculando o logaritmo (A)
        aa = (float) Math.log10(Math.pow(10, -3) / (10 * mediaDemanda));

        ce = (float) Math.exp(aa) * estoqueMedio;

        System.out.println("-> Criterio Economico = " + ce);

    }

    public void calculaNivelAtendimento() {
        
        na = (float) somaDemandAtendimento/demandaTotal;
        System.out.println("-> Nivel de Atendimento = "+na);
        
    }

    public void calcularFuncaoObjetivo() {

        fo = (na*a) + (ce*b);
        System.out.println("-> Funcao Objetivo = "+fo);
        
    }

    public void gerarProblema() {
        
    }

    public void gerarSolucaoInicial() {

    }

    public void gerarAvaliacao() {

    }

    public static void main(String arg[]) {
        gestaoEstoque obj = new gestaoEstoque();
        obj.lerDados();
        obj.calcularCriterioEconomico();
        obj.calculaNivelAtendimento();
        obj.calcularFuncaoObjetivo();
        obj.gerarProblema();
        obj.gerarSolucaoInicial();
        obj.gerarAvaliacao();
    }
}
