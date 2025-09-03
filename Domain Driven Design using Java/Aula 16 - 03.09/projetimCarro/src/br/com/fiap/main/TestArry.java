package br.com.fiap.main;

import br.com.fiap.beans.Carro;

import javax.swing.*;
import java.lang.reflect.Array;
import java.util.ArrayList;

public class TestArry {

    static String texto(String t){
      return JOptionPane.showInputDialog(t);
    }
    static int texto2(String t){
        return Integer.parseInt(JOptionPane.showInputDialog(t));
    }
    static double texto3(String t){
        return Double.parseDouble(JOptionPane.showInputDialog(t));
    }

    public static void main(String[] args) {
        ArrayList<Carro> listCarro = new ArrayList<Carro>();

        do{
                Carro objCarro = new Carro();

                objCarro.setModelo(texto("Modelo"));
                objCarro.setMarca(texto("Marca"));
                objCarro.setDescricao(texto("Descrição"));
                objCarro.setAno(texto2("Ano"));
                objCarro.setVlaor(texto3("Valor"));

                listCarro.add(objCarro);
        }while(JOptionPane.showConfirmDialog(null,"Adicionar","Adicionar",JOptionPane.YES_NO_OPTION,JOptionPane.QUESTION_MESSAGE)==0);

        for (Carro c: listCarro){
            System.out.println(
                    "Modelo = "+c.getModelo()+
                            "\nMarca = "+c.getMarca()+
                            "\nDescrição = "+c.getDescricao()+
                            "\nAno = "+c.getAno()+
                            "\nValor = "+c.getVlaor()
            );
        };
    }
}
