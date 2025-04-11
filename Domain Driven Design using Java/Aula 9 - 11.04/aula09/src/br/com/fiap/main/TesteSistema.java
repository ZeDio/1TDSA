package br.com.fiap.main;

import br.com.fiap.beans.Colaborador;

import javax.swing.*;

public class TesteSistema {
    public static void main(String[] args) {
        Colaborador objColaborador = new Colaborador();

        objColaborador.setNome(JOptionPane.showInputDialog("Digite o nome do colaborador: "));
        objColaborador.setEmail(JOptionPane.showInputDialog("Digite seu email: "));
        objColaborador.setCargo(JOptionPane.showInputDialog("Digite seu cargo: "));
        objColaborador.setIdade(Integer.parseInt(JOptionPane.showInputDialog("Digite sua idade: ")));
        objColaborador.setValorHora(Double.parseDouble(JOptionPane.showInputDialog("Digite seu valor por hora: ")));
        objColaborador.setQuantidadeDeHoras(Double.parseDouble(JOptionPane.showInputDialog("Digite quantas horas você trabalha: ")));

        System.out.println(
                objColaborador
        );

        System.out.println(
                "\n\nSalario do colaborador"+objColaborador.calcularSalario()
        );
    }
}