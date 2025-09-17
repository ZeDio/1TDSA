package br.com.fiap.main;

import br.com.fiap.beans.Aluno;
import br.com.fiap.dao.AlunoDAO;

import java.sql.SQLException;
import java.util.ArrayList;
import java.util.List;

public class TesteSelecionar {
    public static void main(String[] args) throws SQLException, ClassNotFoundException {
        AlunoDAO alunoDAO = new AlunoDAO();
        List<Aluno> listaAluno = (ArrayList<Aluno>) alunoDAO.selecionar();

        if(listaAluno != null){
            for (Aluno a: listaAluno){
                System.out.println(
                        "\n"+a.getRm()+" "+
                                a.getNome()+" "+
                                a.getTurma()+" "+
                                a.getNota()+" \n"
                );
            }
        }
    }
}