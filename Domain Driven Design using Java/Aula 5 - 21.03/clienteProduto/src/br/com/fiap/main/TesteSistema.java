package br.com.fiap.main;

import br.com.fiap.beans.Cliente;
import br.com.fiap.beans.Produto;

public class TesteSistema {

    public static void main(String[] args) {

        Cliente objCliente = new Cliente();
        Produto objProduto = new Produto();

        objCliente.setIdade(17);
        objCliente.setNome("José Diogo");
        objCliente.setEmail("jose.diogo100407@gmail.com");
        objCliente.setRenda(600.00);

        objProduto.setCodigo(001);
        objProduto.setTipo("Computador");
        objProduto.setMarca("Windows");
        objProduto.setValor(4000.00);

        System.out.println(
                "\nIdade: "+objCliente.getIdade()+
                "\nNome: "+objCliente.getNome()+
                "\nEmail: "+objCliente.getEmail()+
                "\nRenda: "+objCliente.getRenda()
        );
        System.out.println(
                "\nCodigo: "+objProduto.getCodigo()+
                "\nTipo: "+objProduto.getTipo()+
                "\nMarca: "+objProduto.getMarca()+
                "\nValor: "+objProduto.getValor()
        );

    }

}
