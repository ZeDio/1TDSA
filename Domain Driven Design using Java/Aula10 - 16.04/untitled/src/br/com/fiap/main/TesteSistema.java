package br.com.fiap.main;

import br.com.fiap.beans.Produto;

import javax.swing.*;

public class TesteSistema {

    static String texto(String t){
        return JOptionPane.showInputDialog(t);
    }
    static int inteiro(String i){
        return Integer.parseInt(JOptionPane.showInputDialog(i));
    }
    static double quebrado(String q){
        return Double.parseDouble(JOptionPane.showInputDialog(q));
    }

    public static void main(String[] args) {
        Produto objProduto = new Produto();

        objProduto.setCodigo(inteiro("Digite o codigo do produto: "));
        objProduto.setMarca(texto("Digite a marca do produto: "));
        objProduto.setQuantidade(inteiro("Digite a quantidade que tem desse produto: "));
        objProduto.setTipo(texto("Digite o tipo do produto: "));
        objProduto.setValor(quebrado("Digite o valor do produto: "));

        System.out.println(
            objProduto
        );
    }
}
