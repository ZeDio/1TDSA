package br.com.fiap.beans;

public class Colaborador {
    private String nome;
    private String email;
    private String cargo;
    private int idade;
    private double quantidadeDeHoras;
    private double valorHora;

    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }

    public String getCargo() {
        return cargo;
    }

    public void setCargo(String cargo) {
        this.cargo = cargo;
    }

    public int getIdade() {
        return idade;
    }

    public void setIdade(int idade) {
        this.idade = idade;
    }

    public double getQuantidadeDeHoras() {
        return quantidadeDeHoras;
    }

    public void setQuantidadeDeHoras(double quantidadeDeHoras) {
        this.quantidadeDeHoras = quantidadeDeHoras;
    }

    public double getValorHora() {
        return valorHora;
    }

    public void setValorHora(double valorHora) {
        this.valorHora = valorHora;
    }

    @Override
    public String toString() {
        return "\nColaborador{" +
                "\nnome='" + nome + '\'' +
                ",\n email='" + email + '\'' +
                ",\n cargo='" + cargo + '\'' +
                ",\n idade=" + idade +
                ",\n quantidadeDeHoras=" + quantidadeDeHoras +
                ",\n valorHora=\n" + valorHora +
                '}';
    }

    public double calcularSalario(){
        return quantidadeDeHoras * valorHora;
    }
}
