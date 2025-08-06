package br.com.fiap.beans;

public class Cliente {
    private String nome;
    private String cpf;
    private String numeroCelular;
    private int idade;
    private double renda;

    public Cliente() {
    }

    public Cliente(String nome, String cpf, String numeroCelular, int idade, double renda) {
        this.nome = nome;
        this.cpf = cpf;
        this.numeroCelular = numeroCelular;
        this.idade = idade;
        this.renda = renda;
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

    public String getNumeroCelular() {
        return numeroCelular;
    }

    public void setNumeroCelular(String numeroCelular) {
        this.numeroCelular = numeroCelular;
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
        return "Cliente{" +
                "nome='" + nome + '\'' +
                ", cpf='" + cpf + '\'' +
                ", numeroCelular='" + numeroCelular + '\'' +
                ", idade=" + idade +
                ", renda=" + renda +
                '}';
    }
}