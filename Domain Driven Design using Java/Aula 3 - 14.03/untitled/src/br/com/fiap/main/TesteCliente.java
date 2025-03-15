package br.com.fiap.main;

import br.com.fiap.bean.Cliente;

public class TesteCliente {

    //execução - psvm
    public static void main(String[] args){

        //instanciar objetos
        Cliente objCliente = new Cliente();

        //entradas
        objCliente.setCodigo(119038);
        objCliente.setMarca("Samsung");
        objCliente.setTipo("Z Flip 5 - 512gb");
        objCliente.setValor(3500.00);

        //saída - sout
        System.out.println("Codigo Produto: " + objCliente.getCodigo());
        System.out.println("Marca: " + objCliente.getMarca());
        System.out.println("Tipo: " + objCliente.getTipo());
        System.out.println("Preço: " + objCliente.getValor());
    }

}