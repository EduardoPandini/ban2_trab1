package biblioteca.controller;

import biblioteca.model.UsuarioModel;
import biblioteca.view.UsuarioBean;
import com.mongodb.client.MongoDatabase;
import biblioteca.exceptions.InsertException;
import biblioteca.exceptions.SelectException;
import biblioteca.exceptions.UpdateException;

import java.util.*;

public class UsuarioController {

    public static void createUsuario(MongoDatabase database) throws InsertException {

            Scanner sc = new Scanner(System.in);
            sc.nextLine();
            System.out.println("Insira os dados para a criacao de um novo usuario.\n nome: ");
            String nome = sc.nextLine();
            sc.nextLine();
            System.out.println("\nEndereço: ");
            String endereco = sc.nextLine();
            sc.nextLine();
            System.out.println("Telefones (é possível adicionar mais posteriormente): ");
            List<Integer> telefones = new ArrayList<>();
            telefones.add(sc.nextInt());
            sc.nextLine();
            System.out.println("Qual categoria você pertence?\n1 - Graduação\n2 - Pós-Graduação\n3 - Professor Graduação\n4 - Professor Pós-Graduação\n");
            System.out.println("Sua categoria: ");
            int categoria = sc.nextInt();

            // alterar o primeiro "0" aqui, coloquei só de placeholder pra IDE não reclamar
            // quando precisar, vai ter um statement recuperando o objeto inteiro do DB pra pegar o valor auto-incremental de fato

            UsuarioBean ub = new UsuarioBean(0, 0, nome, endereco, telefones, categoria);
            UsuarioModel.create(ub,database);


        System.out.println("Usuario criado com sucesso!");

    }

    public static void createFoneExtra(UsuarioBean ub, MongoDatabase database) throws InsertException{
        try{
            Scanner sc = new Scanner(System.in);

            System.out.println("Entre com um telefone para ser adicionado ao usuário escolhido! \n");
            int telefone = sc.nextInt();
            UsuarioModel.addFoneExtra(ub, telefone, database);

        }catch(SelectException ex){
            throw new InsertException("Problema na inserção de outro telefone no usuario.");
        }

        System.out.println("Telefone adicionado com sucesso!\n");
    }

    public static void AddLivro(UsuarioBean ub, MongoDatabase database) throws UpdateException {
        UsuarioModel.addLivroExtra(ub,database);
    }

    public static void listarUsuarios(MongoDatabase database) throws SelectException {
        List<UsuarioBean> all = UsuarioModel.listAll(database);
        for (UsuarioBean usuarioBean : all) {
            System.out.println(usuarioBean);
        }
    }

}
