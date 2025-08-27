package br.com.fiap.main;

import br.com.fiap.beans.Produto;

import javax.swing.*;

public class SistemaTestArry {

    static String texto(String t){
      return JOptionPane.showInputDialog(t);
    };
    static int number(String t){
        return Integer.parseInt(JOptionPane.showInputDialog(t));
    };
    static double number2(String t){
        return Double.parseDouble(JOptionPane.showInputDialog(t));
    };

    public static void main(String[] args) {
        Produto[] vetorProduto = new Produto[3];
        int i = 0;
        do{
            vetorProduto[i]=new Produto();
            vetorProduto[i].setNome(texto("Nome Produto"));
            vetorProduto[i].setEstoque(number("Quantidade Estoque"));
            vetorProduto[i].setPreco(number2("Valor"));
            i++;
        }while(JOptionPane.showConfirmDialog(null,
                "cadastrar produto",
                "cadastrar produto",
                JOptionPane.YES_NO_OPTION,
                JOptionPane.QUESTION_MESSAGE) == 0);

        for(int ii = 0; ii < i; ii++){
            System.out.println(
                    "nome"+vetorProduto[ii].getNome()+
                            "\nQuantidade Estoque"+vetorProduto[ii].getEstoque()+
                            "\nValor"+vetorProduto[ii].getPreco()
            );
        };
    }
}
