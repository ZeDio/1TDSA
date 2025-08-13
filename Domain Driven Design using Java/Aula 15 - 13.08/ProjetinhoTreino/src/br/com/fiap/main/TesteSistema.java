package br.com.fiap.main;

import br.com.fiap.beans.Aluno;

import javax.swing.*;

public class TesteSistema {

    //String
    static String texto(String j){
        return JOptionPane.showInputDialog(j);
    }
    //int
    static int interiro(String j){
        return Integer.parseInt(JOptionPane.showInputDialog(j));
    }
    //double
    static double quebrado(String j){
        return Double.parseDouble(JOptionPane.showInputDialog(j));
    }

    public static void main(String[] args) {

        // Preparar a quantidade maxima de vetores
        Aluno[] vetorAluno = new Aluno[3]; // [0] [1] [2] [n]
        // Preparar indice para controlar as posições dos vetores
        int indice = 0;
        //Laço de repetição      do/while
        do {
            //Entradas
            vetorAluno[indice] = new Aluno();
            vetorAluno[indice].setNome(texto("Nome"));
            vetorAluno[indice].setRm(texto("Rm"));
            vetorAluno[indice].setTurma(texto("Turma"));
            vetorAluno[indice].setIdade(interiro("Idade"));
            vetorAluno[indice].setNota(quebrado("Nota"));

            indice ++;
        }while( JOptionPane.showConfirmDialog(
                null,
                "Cadastras mais Alunos(as)?",
                "Cadastro De Alunos",
                JOptionPane.YES_NO_OPTION,
                JOptionPane.QUESTION_MESSAGE)== 0);

        //Saidas utilizando   for
        for(int buscar = 0; buscar < indice; buscar++){
            System.out.println(
                    "Nome: "+ vetorAluno[buscar].getNome() +
                            "\nRm: "+ vetorAluno[buscar].getRm()+
                            "\nTurma: "+ vetorAluno[buscar].getTurma()+
                            "\nIdade: "+ vetorAluno[buscar].getIdade()+
                            "\nNota: "+ vetorAluno[buscar].getNota()
            );
        }
    }
}