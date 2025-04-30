package br.com.fiap.main;
import br.com.fiap.beans.Cliente;
import br.com.fiap.beans.Endereco;
import br.com.fiap.beans.Produto;

import javax.swing.*;

public class TesteSistema {

    static String texto(String t){
        return JOptionPane.showInputDialog(t);
    }
    static int number(String n){
        return Integer.parseInt(JOptionPane.showInputDialog(n));
    }
    static double quebrado(String q){
        return Double.parseDouble(JOptionPane.showInputDialog(q));
    }

    public static void main(String[] args) {
        Cliente objCliente = new Cliente(
                texto("Informe o Nome: "),
                texto("Informe o CPF: "),
                number("Informe a Idade: "),
                quebrado("Informe a renda: ")
        );
        Endereco objEndereco = new Endereco(
                texto("Informe o Logradouro: "),
                number("Informe o Numero: "),
                texto("Informe o CEP: "),
                texto("Informe o Bairro: "),
                texto("Informe a Cidade: ")
        );
        Produto objProduto = new Produto(
                number("Digite o codigo: "),
                texto("Digite o tipo: "),
                texto("Digite a marca: "),
                number("Digite a quantidade: "),
                quebrado("Digite o valor: ")
        );


        System.out.println(objCliente);
        System.out.println(objProduto);
    }
}
