package br.com.fiap.main;

import br.com.fiap.beans.produto;

public class ProdutoTeste {
    public static void main(String[] args) {
        produto objProduto = new produto();

        objProduto.setCodigo(00001);
        objProduto.setTipo("Alguma coisa");
        objProduto.setMarca("Alguma marca");
        objProduto.setValor(0.0);

        System.out.println("Codigo: "+objProduto.getCodigo());
        System.out.println("Tipo: "+objProduto.getTipo());
        System.out.println("Marca: "+objProduto.getMarca());
        System.out.println("Valor: "+objProduto.getValor());
    }
}
