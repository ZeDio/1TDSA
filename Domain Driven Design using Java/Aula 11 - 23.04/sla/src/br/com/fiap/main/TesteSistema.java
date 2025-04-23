package br.com.fiap.main;

import br.com.fiap.beans.Produto;

import javax.swing.*;

public class TesteSistema {
    static String texto(String texto){
        return JOptionPane.showInputDialog(texto);
    }
    static int numero(String numero){
        return Integer.parseInt(JOptionPane.showInputDialog(numero));
    }
    static double numeroQuebrado(String numeroQuebrado){
        return Double.parseDouble(JOptionPane.showInputDialog(numeroQuebrado));
    }

    public static void main(String[] args) {
        Produto objProduto = new Produto(
                numero("Digite o codigo do produto: "),
                texto("Digite o tipo do produto: "),
                texto("Digite a marca do produto: "),
                numero("Digite a quantidade do estoque: "),
                numeroQuebrado("Digite o valor do produto: ")
        );

        /*
        objProduto.setCodigo(numero("Digite o codigo do produto: "));
        objProduto.setMarca(texto("Digite a marca do produto: "));
        objProduto.setQuantidade(numero("Digite a quantidade do estoque: "));
        objProduto.setTipo(texto("Digite o tipo do produto: "));
        objProduto.setValor(numeroQuebrado("Digite o valor do produto: "));
         */

        System.out.println(objProduto);
    }
}
