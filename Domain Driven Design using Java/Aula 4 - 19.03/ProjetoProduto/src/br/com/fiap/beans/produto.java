package br.com.fiap.beans;

public class produto {
    private int codigo;
    private String tipo;
    private String marca;
    private double valor;


    public void setCodigo(int codigo) {
        this.codigo = codigo;
    }

    public void setMarca(String marca) {
        this.marca = marca;
    }

    public void setTipo(String tipo) {
        this.tipo = tipo;
    }

    public void setValor(double valor) {
        this.valor = valor;
    }


    public int getCodigo() {
        return codigo;
    }

    public String getMarca() {
        return marca;
    }

    public String getTipo() {
        return tipo;
    }

    public double getValor() {
        return valor;
    }
}
