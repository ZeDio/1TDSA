package br.com.fiap.bean;

public class Produto {

    //entrada -> processamento -> saida

    //tipo de dado e atributos
    int codigo;
    String tipo;
    String marca;
    double valor;

    // metodos Setters (entrada)
    public void setCodigo(int codigo){
        this.codigo = codigo;
    }
    public void setTipo(String tipo){
        this.tipo = tipo;
    }
    public void setMarca(String marca) {
        this.marca = marca;
    }
    public void setValor(double valor) {
        this.valor = valor;
    }

    //metodos Getters (retornar/exibir)
    public int getcodigo(){
        return codigo;
    }
    public String getTipo(){
        return tipo;
    }
    public String getMarca() {
        return marca;
    }
    public double getValor() {
        return valor;
    }
}
