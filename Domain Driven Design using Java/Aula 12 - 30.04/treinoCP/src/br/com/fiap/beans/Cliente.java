package br.com.fiap.beans;

public class Cliente {
    private String nome;
    private String cpf;
    private int idade;
    private double renda;
    private Endereco endereco;

    public Cliente(){

    }

    public Cliente(String nome, String cpf, int idade, double renda) {
        this.nome = nome;
        this.cpf = cpf;
        this.idade = idade;
        this.renda = renda;
    }

    public Endereco getEndereco() {
        return endereco;
    }

    public void setEndereco(Endereco endereco) {
        this.endereco = endereco;
    }

    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public String getCpf() {
        return cpf;
    }

    public void setCpf(String cpf) {
        this.cpf = cpf;
    }

    public int getIdade() {
        return idade;
    }

    public void setIdade(int idade) {
        this.idade = idade;
    }

    public double getRenda() {
        return renda;
    }

    public void setRenda(double renda) {
        this.renda = renda;
    }

    @Override
    public String toString() {
        return "\n\nCliente" +
                "\nnome= " + nome +
                "\ncpf= " + cpf +
                "\nidade= " + idade +
                "\nrenda= " + renda +
                "\nendereço= " + endereco;
    }
}