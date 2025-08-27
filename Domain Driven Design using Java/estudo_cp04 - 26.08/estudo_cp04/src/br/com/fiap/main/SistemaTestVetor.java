package br.com.fiap.main;

import br.com.fiap.beans.Produto;

import javax.swing.*;

public class SistemaTestVetor {

    static String texto(String b){
       return JOptionPane.showInputDialog(b);
    };
    static int texto2(String b){
        return Integer.parseInt(JOptionPane.showInputDialog(b));
    };
    static double texto3(String b){
        return Double.parseDouble(JOptionPane.showInputDialog(b));
    };

    public static void main(String[] args) {
        Produto[] vetorProduto = new Produto[3];
        int i = 0;
        do {
            vetorProduto[i] = new Produto();
            vetorProduto[i].setNome(texto("Nome Produto"));
            vetorProduto[i].setEstoque(texto2("Estoque"));
            vetorProduto[i].setPreco(texto3("Valor"));
            i++;
        }while(JOptionPane.showConfirmDialog(null,"Cadrastrar Produto",
                "Cadastrar Produto", JOptionPane.YES_NO_OPTION,
                JOptionPane.QUESTION_MESSAGE)==0);

        for (int ii = 0; ii < i; ii++){
            System.out.println(
                    "Nome"+vetorProduto[ii].getNome()+
                            "Estoque"+vetorProduto[ii].getEstoque()+
                            "Valor"+vetorProduto[ii].getPreco()
            );
        };
    }
}