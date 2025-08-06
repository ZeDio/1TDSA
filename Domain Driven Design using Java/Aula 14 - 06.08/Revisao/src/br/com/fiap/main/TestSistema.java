package br.com.fiap.main;

import br.com.fiap.beans.Cliente;

import javax.swing.*;

public class TestSistema {

    static String texto(String t){
        return JOptionPane.showInputDialog(t);
    }
    static int numeroInteiro(String i){
        return Integer.parseInt(JOptionPane.showInputDialog(i));
    }
    static double numeroQuebrado(String q){
        return Double.parseDouble(JOptionPane.showInputDialog(q));
    }

    public static void main(String[] args) {
        Cliente objCliente = new Cliente();

        //String nome, String cpf, String numeroCelular, int idade, double renda
        objCliente.setNome(texto("Nome Cliente"));
        objCliente.setCpf(texto("Digite seu CPF"));
        objCliente.setNumeroCelular(texto("Digite seu numero de ceular"));
        objCliente.setIdade(numeroInteiro("Digite sua idade"));
        objCliente.setRenda(numeroQuebrado("Digite sua renda"));

        System.out.println(objCliente);
    }
}
