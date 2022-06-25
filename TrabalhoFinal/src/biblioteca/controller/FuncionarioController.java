package biblioteca.controller;

import biblioteca.model.AssistenteModel;
import biblioteca.model.BibliotecarioModel;
import biblioteca.model.FuncionarioModel;
import biblioteca.view.FuncionarioBean;
import com.mongodb.client.MongoDatabase;
import biblioteca.exceptions.InsertException;
import biblioteca.exceptions.SelectException;
import biblioteca.exceptions.UpdateException;

import java.util.List;
import java.util.Scanner;

public class FuncionarioController {
    public static void createFuncionario(MongoDatabase database) throws InsertException, SelectException, UpdateException {

        Scanner sc = new Scanner(System.in);
        System.out.println("Insira os dados para a criacao de um novo Funcionario.\n nome: ");
        String nome = sc.nextLine();
        sc.nextLine();
        System.out.println("\nAgora seu numero de cpf: ");
        int cpf = sc.nextInt();
        sc.nextLine();
        System.out.println("O funcionario é um bibliotecario ou um assistente?\n1 - Bibliotecario, 2 - Assistente");
        int eh_bibliotecario = sc.nextInt();
        FuncionarioBean fb = new FuncionarioBean(0, nome, cpf);
        sc.nextLine();
        if (eh_bibliotecario == 1) {
            FuncionarioModel.create(fb, database);
            BibliotecarioModel.create(fb, database);
            return;

        } else if (eh_bibliotecario == 2) {
            FuncionarioModel.create(fb, database);
            System.out.println("Defina o supervisor deste assistente (Por ID de bibliotecario): ");
            BibliotecarioController.listarFuncionarios(database);
            int escolha = sc.nextInt();
            AssistenteModel.create(fb, database, escolha);

        } else {
            System.out.println("Entre com um valor válido para funcionário ou assistente");
            return;


        }
    }

    public static void listarFuncionarios(MongoDatabase database) throws SelectException {
        List<FuncionarioBean> all = FuncionarioModel.listAll(database);
        for (FuncionarioBean funcionariobean : all) {
            System.out.println(funcionariobean);
        }
    }

}
