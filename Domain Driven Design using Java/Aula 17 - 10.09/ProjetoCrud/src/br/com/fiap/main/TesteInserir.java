package br.com.fiap.main;

import br.com.fiap.beans.Aluno;
import br.com.fiap.dao.AlunoDAO;

import javax.swing.*;
import java.sql.SQLException;

public class TesteInserir {

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
        AlunoDAO alunoDAOO = new AlunoDAO();

        Aluno objAluno = new Aluno();
        objAluno.setRm(inteiro("RM"));
        objAluno.setNota(quebrado("Nota"));
        objAluno.setNome(text("Nome"));
        objAluno.setTurma(text("Turma"));
        System.out.println(AlunoDAO.inserir(objAluno));

    }

}
