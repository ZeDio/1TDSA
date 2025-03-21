package br.com.fiap.beans;

public class Cliente {

    //visibilidade de atributos e de dados
    private int idade;
    private String nome;
    private String email;
    private double renda;

    //Entrada e retornar e exibir
    public void setIdade(int idade) {
        this.idade = idade;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public void setEmail(String email) {
        this.email = email;
    }

    public void setRenda(double renda) {
        this.renda = renda;
    }


    public int getIdade() {
        return idade;
    }

    public String getNome() {
        return nome;
    }

    public String getEmail() {
        return email;
    }

    public double getRenda() {
        return renda;
    }
}
