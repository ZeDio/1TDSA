package br.com.fiap.main;

import br.com.fiap.beans.Produto;

import javax.swing.*;
import java.util.ArrayList;

public class SistemaTestArry {

    static String texto(String t){
      return JOptionPane.showInputDialog(t);
    };
    static int texto2(String t){
        return Integer.parseInt(JOptionPane.showInputDialog(t));
    };
    static double texto3(String t){
        return Double.parseDouble(JOptionPane.showInputDialog(t));
    };

    public static void main(String[] args) {
        ArrayList<Produto> listaProduto = new ArrayList<Produto>();

        Produto objProduto = null;

        do {
            objProduto.setNome(texto("Nome Produto"));
            objProduto.setEstoque(texto2("Estoque"));
            objProduto.setPreco(texto3("Preço"));
            listaProduto.add(objProduto);
        }while (JOptionPane.showConfirmDialog(null,
                "Cadastrar Produto",
                "Cadastrar Produto",
                JOptionPane.YES_NO_OPTION,
                JOptionPane.QUESTION_MESSAGE)==0);

        for (Produto a: listaProduto){
            System.out.println(
                    "Nome"+a.getNome()+
                            "Estoque"+a.getEstoque()+
                            "Valor"+a.getPreco()
            );
        }
    }
}