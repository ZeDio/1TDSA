package br.com.fiap.main;

import br.com.fiap.api.Endereco;
import br.com.fiap.services.ViacepService;

import javax.swing.*;
import java.io.IOException;

public class TestViaCep {
    static String texto(String j){
        return JOptionPane.showInputDialog(j);
    }
    public static void main(String[] args) throws IOException {

        ViacepService viacepService = new ViacepService();

        String cep = texto("CEP");
        Endereco endereco = viacepService.getEndereco(cep);
        System.out.println(endereco);

    }
}
