package br.com.fiap.main;

import br.com.fiap.beans.Aluno;

import javax.swing.*;
import java.util.ArrayList;

public class TesteSistemaArrayList {

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
        ArrayList<Aluno> listAluno = new ArrayList<Aluno>();

        Aluno objAluno = null;
        do {
            objAluno.setNome(texto("Nome"));
            objAluno.setRm(texto("Rm"));
            objAluno.setTurma(texto("Turma"));
            objAluno.setIdade(interiro("Idade"));
            objAluno.setNota(quebrado("Nota"));

            listAluno.add(objAluno);

        }while( JOptionPane.showConfirmDialog(
                null,
                "Cadastras mais Alunos(as)?",
                "Cadastro De Alunos",
                JOptionPane.YES_NO_OPTION,
                JOptionPane.QUESTION_MESSAGE)== 0);

        for(Aluno a: listAluno){
            System.out.println(
                    "Nome: "+ a.getNome() +
                            "\nRm: "+ a.getRm()+
                            "\nTurma: "+ a.getTurma()+
                            "\nIdade: "+ a.getIdade()+
                            "\nNota: "+ a.getNota()
            );
        }
    }
}