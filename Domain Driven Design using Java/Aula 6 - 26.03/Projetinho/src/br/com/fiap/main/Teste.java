package br.com.fiap.main;

import br.com.fiap.beans.Cliente;
import br.com.fiap.beans.Endereco;
import br.com.fiap.beans.Produto;

public class Teste {
    public static void main(String[] args) {

        Cliente objCliente = new Cliente();
        Produto objProduto = new Produto();
        Endereco objEndereco = new Endereco();

        objCliente.setIdade(18);
        objCliente.setNome("José");
        objCliente.setEmail("jose.diogo100407@gmail.com");
        objCliente.setRenda(1500.00);
        objCliente.setEndereco(objEndereco);

        objEndereco.setLogradouro("Rua Helena Zerrener");
        objEndereco.setNumero(39);
        objEndereco.setComplemento("1214");
        objEndereco.setCidade("São Paulo");
        objEndereco.setBairro("Liberdade");
        objEndereco.setCep("01512-020");

        objProduto.setCodigo(001);
        objProduto.setMarca("Pulma");
        objProduto.setTipo("Sapato");
        objProduto.setValor(400.00);

        System.out.println("Nome cliente: "+objCliente.getNome()
                +"\nIdade cliente"+objCliente.getIdade()
                +"\nEmail cliente"+objCliente.getEmail()
                +"\nRenda cliente"+objCliente.getRenda()
        );
        System.out.println("\tLogradouro: "+objEndereco.getLogradouro()
                +"\nNumero: "+objEndereco.getNumero()
                +"\nComplemento: "+objEndereco.getComplemento()
                +"\nCidade: "+objEndereco.getCidade()
                +"\nBairro: "+objEndereco.getBairro()
                +"\nCep: "+objEndereco.getCep()
        );
        System.out.println("\tCodigo produto: "+objProduto.getCodigo()
                +"\nMarca produto"+objProduto.getMarca()
                +"\nTipo produto"+objProduto.getTipo()
                +"\nValor produto"+objProduto.getValor()
        );

    }
}
