package br.com.fiap.main;

import javax.swing.*;

public class SistemaTestVetor {

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

    }
}