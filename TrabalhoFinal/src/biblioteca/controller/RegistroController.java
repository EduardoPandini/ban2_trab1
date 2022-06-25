package biblioteca.controller;

import biblioteca.model.RegistroModel;
import biblioteca.view.RegistroBean;
import biblioteca.view.UsuarioBean;
import com.mongodb.client.MongoDatabase;
import biblioteca.exceptions.SelectException;
import biblioteca.exceptions.UpdateException;

import java.sql.SQLException;
import java.util.List;
import java.util.Scanner;

public class RegistroController {

    public static void renovaLivro(UsuarioBean ub, MongoDatabase database) throws UpdateException, SelectException, SQLException {
        Scanner sc = new Scanner(System.in);
        System.out.println("Escolha um livro emprestado para renovar!");
        listarRegistros(database);
        int escolha_registro = sc.nextInt();
        RegistroBean registro_escolhido = RegistroModel.escolheRegistro(escolha_registro,database);
        if(ub.getId_usuario() != registro_escolhido.getId_usuario()){ // usa o id pra ver se o usuário realmente emprestou o livro
            System.out.println("Apenas renove um livro que você emprestou!");
            return;
        }
        RegistroModel.renovaLivro(registro_escolhido,ub,database);

    }

    public static void reservaLivro(UsuarioBean ub, MongoDatabase database) throws UpdateException, SelectException {
        Scanner sc = new Scanner(System.in);
        System.out.println("Escolha um livro para reservar! (Por ID de registro): ");
        listarRegistros(database);
        int escolha_registro = sc.nextInt();
        RegistroBean registro_escolhido = RegistroModel.escolheRegistro(escolha_registro,database);
        if(registro_escolhido.isReservado()){
            System.out.println("O livro em questão já está reservado!");
            return;
        }
        RegistroModel.reservaLivro(registro_escolhido,ub,database);

    }

    public static void listarRegistros(MongoDatabase database) throws SelectException {
        List<RegistroBean> all = RegistroModel.listAll(database);
        for (RegistroBean registroBean : all) {
            System.out.println(registroBean);
        }
    }


}
