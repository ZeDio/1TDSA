package br.com.fiap.main;

import br.com.fiap.bean.Cliente;

public class TesteCliente {

    //execução - psvm
    public static void main(String[] args){

        //instanciar objetos
        Cliente objCliente = new Cliente();

        //entradas
        objCliente.setIdade(17);
        objCliente.setNome("José Diogo");
        objCliente.setRenda(1480.00);
        objCliente.setEmail("jose.diogo100407@gmail.com");

        //saída - sout
        System.out.println("Nome: " + objCliente.getNome());
        System.out.println("Idade: " + objCliente.getIdade());
        System.out.println("Email: " + objCliente.getEmail());
        System.out.println("Renda: " + objCliente.getRenda());
    }

}