package br.com.fiap.beans;

public class Endereco {
    private String lougradouro;
    private int numero;
    private String cep;
    private String bairro;
    private String cidade;

    public Endereco() {

    }

    public Endereco(String lougradouro, int numero, String cep, String bairro, String cidade) {
        this.lougradouro = lougradouro;
        this.numero = numero;
        this.cep = cep;
        this.bairro = bairro;
        this.cidade = cidade;
    }

    public String getLougradouro() {
        return lougradouro;
    }

    public void setLougradouro(String lougradouro) {
        this.lougradouro = lougradouro;
    }

    public int getNumero() {
        return numero;
    }

    public void setNumero(int numero) {
        this.numero = numero;
    }

    public String getCep() {
        return cep;
    }

    public void setCep(String cep) {
        this.cep = cep;
    }

    public String getBairro() {
        return bairro;
    }

    public void setBairro(String bairro) {
        this.bairro = bairro;
    }

    public String getCidade() {
        return cidade;
    }

    public void setCidade(String cidade) {
        this.cidade = cidade;
    }

    @Override
    public String toString() {
        return "\nlougradouro= " + lougradouro +
                "\nnumero= " + numero +
                "\ncep= " + cep +
                "\nbairro= " + bairro +
                "\ncidade= " + cidade;
    }
}
