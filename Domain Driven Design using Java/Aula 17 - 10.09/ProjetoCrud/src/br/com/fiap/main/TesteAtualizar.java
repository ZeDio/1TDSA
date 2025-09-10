package br.com.fiap.main;

import br.com.fiap.beans.Aluno;
import br.com.fiap.dao.AlunoDAO;

import javax.swing.*;
import java.sql.SQLException;

public class TesteAtualizar {

    static int inteiro(String j){
        return  Integer.parseInt(JOptionPane.showInputDialog(j));
    }
    static String text(String j){
        return  JOptionPane.showInputDialog(j);
    }
    static double quebrado(String j){
        return  Double.parseDouble(JOptionPane.showInputDialog(j));
    }

    public static void main(String[] args) throws SQLException, ClassNotFoundException {
        // instanciar objetos
        AlunoDAO alunoDAO = new AlunoDAO();
        Aluno objAluno = new Aluno();
        objAluno.setRm(inteiro("Rm do aluno para atualizar"));
        objAluno.setNome(text("Nome"));
        objAluno.setTurma(text("Turma"));
        objAluno.setNota(quebrado("Nota"));
        System.out.println(alunoDAO.atualizar(objAluno));
    }
}
