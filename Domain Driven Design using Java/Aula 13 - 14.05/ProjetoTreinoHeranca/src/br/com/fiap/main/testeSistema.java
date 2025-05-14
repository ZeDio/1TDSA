package br.com.fiap.main;

import br.com.fiap.beans.Cliente;
import br.com.fiap.beans.Colaborador;
import br.com.fiap.beans.Endereco;

import javax.swing.*;

public class testeSistema {

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
        Cliente objCLiente = new Cliente(
                //String nome, int idade, String cpf, String rg, double renda, String status
                texto("Nome Do cliente"),
                inteiro("Idade do cliente"),
                texto("Cpf do cliente"),
                texto("RG do cliente"),
                quebrado("Renda do cliente"),
                texto("Status do cliente")
        );
        Endereco objEndereco = new Endereco(
                //String logradouro, int numero, String cep, String bairro, String cidade
                texto("Logradouro"),
                inteiro("Numero"),
                texto("Cep"),
                texto("Bairro"),
                texto("Cidade")
        );
        objCLiente.setEndereco(objEndereco);
        Colaborador objColaborador = new Colaborador(
                //String nome, int idade, String cpf, String rg, double renda, int numeroCracha
                texto("Nome Do colaborador"),
                inteiro("Idade do colaborador"),
                texto("Cpf do colaborador"),
                texto("RG do colaborador"),
                quebrado("Renda do colaborador"),
                inteiro("Numero de Cracha do colaborador")
        );

        System.out.println(objCLiente + "" + objColaborador);
    }
}
