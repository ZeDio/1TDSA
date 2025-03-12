package br.com.fiap.main;

import br.com.fiap.beans.Cliente;

public class TesteCliente {

    //execução - psvm
    public static void main(String[] args){

        //instanciar objetos
        Cliente objCLiente = new Cliente();

        //entradas
        objCLiente.setIdade(17);
        objCLiente.setNome("José Diogo");
        objCLiente.setAltura(1.69);

        //saída - sout
        System.out.println("Idade " + objCLiente.getIdade() + ". Me chamo " + objCLiente.getNome() + ", e tenho " + objCLiente.getAltura() + " de altura");

    }



}
