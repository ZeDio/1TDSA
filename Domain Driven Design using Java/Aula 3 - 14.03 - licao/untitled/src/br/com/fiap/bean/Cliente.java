package br.com.fiap.bean;

public class Cliente {

    //entrada -> processamento -> saida

    //tipo de dado e atributos
    int idade;
    String nome;
    String email;
    double renda;

    // metodos Setters (entrada)
    public void setIdade(int idade){
        this.idade = idade;
    }
    public void setNome(String nome){
        this.nome = nome;
    }
    public void setEmail(String email) {
        this.email = email;
    }
    public void setRenda(double renda) {
        this.renda = renda;
    }

    //metodos Getters (retornar/exibir)
    public int getIdade(){
        return idade;
    }
    public String getNome(){
        return nome;
    }
    public String getEmail() {
        return email;
    }
    public double getRenda() {
        return renda;
    }
}
