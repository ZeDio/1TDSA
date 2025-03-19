package br.com.fiap.main;

import br.com.fiap.bean.Produto;

public class TesteProduto {

    //execução - psvm
    public static void main(String[] args){

        //instanciar objetos
        Produto objProduto = new Produto();

        //entradas
        objCliente.setCodigo(17);
        objCliente.setTipo("José Diogo");
        objCliente.setMarca(1480.00);
        objCliente.setValor("jose.diogo100407@gmail.com");

        //saída - sout
        System.out.println("Tipo: " + objCliente.getTipo());
        System.out.println("Codigo: " + objCliente.getCodigo());
        System.out.println("Marca: " + objCliente.getMarcar());
        System.out.println("Valor: " + objCliente.getValor());
    }

}