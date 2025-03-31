package br.com.fiap.main;

import br.com.fiap.beans.Cliente;
import br.com.fiap.beans.Endereco;
import br.com.fiap.beans.Produto;

public class TesteSistema {
    public static void main(String[] args) {
        Cliente objCliente = new Cliente();
        Produto objProduto = new Produto();
        Endereco objEndereco = new Endereco();

        objCliente.setNome("josé");
        objCliente.setEmail("jose.diogo100407@gmail.com");
        objCliente.setIdade(17);
        objCliente.setRenda(1500);
        objCliente.setEndereco(objEndereco);

        objEndereco.setBairro("Liberdade");
        objEndereco.setLogradouro("Rua Hellena Zerrener");
        objEndereco.setCep("01512-020");
        objEndereco.setCidade("São Paulo");
        objEndereco.setNumero(39);

        objProduto.setMarca("Samsung");
        objProduto.setTipo("Celular");
        objProduto.setCodigo(101);
        objProduto.setValor(3500.00);

        System.out.println(objProduto.getMarca()+objEndereco.getCidade()+objCliente.getNome());

    }
}
