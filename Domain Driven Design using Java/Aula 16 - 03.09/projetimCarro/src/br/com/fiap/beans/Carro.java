package br.com.fiap.beans;

public class Carro {

     private String modelo;
     private String marca;
     private String descricao;
     private int ano;
     private double vlaor;

    public Carro(String modelo, String marca, String descricao, int ano, double vlaor) {
        this.modelo = modelo;
        this.marca = marca;
        this.descricao = descricao;
        this.ano = ano;
        this.vlaor = vlaor;
    }

    public Carro() {
    }

    public String getModelo() {
        return modelo;
    }

    public void setModelo(String modelo) {
        this.modelo = modelo;
    }

    public String getMarca() {
        return marca;
    }

    public void setMarca(String marca) {
        this.marca = marca;
    }

    public String getDescricao() {
        return descricao;
    }

    public void setDescricao(String descricao) {
        this.descricao = descricao;
    }

    public int getAno() {
        return ano;
    }

    public void setAno(int ano) {
        this.ano = ano;
    }

    public double getVlaor() {
        return vlaor;
    }

    public void setVlaor(double vlaor) {
        this.vlaor = vlaor;
    }

    @Override
    public String toString() {
        return "Carro\n" +
                "modelo= " + modelo +
                "\nmarca= " + marca +
                "\ndescricao= " + descricao +
                "\nano= " + ano +
                "\nvlaor= " + vlaor;
    }
}