package biblioteca;

import biblioteca.conexao.Conexao;
import biblioteca.controller.FuncionarioController;
import biblioteca.controller.LivroController;
import biblioteca.controller.RegistroController;
import biblioteca.controller.UsuarioController;
import biblioteca.view.LivroBean;
import biblioteca.view.UsuarioBean;
import com.mongodb.client.MongoCollection;
import com.mongodb.client.MongoDatabase;
import biblioteca.exceptions.InsertException;
import biblioteca.exceptions.SelectException;
import biblioteca.exceptions.UpdateException;
import static com.mongodb.client.model.Filters.*;
import java.sql.SQLException;
import java.text.ParseException;
import java.util.Scanner;


public class Main {
    public static void main(String[] args){
        int opcao;
        Conexao con = Conexao.getConexao();
        MongoDatabase database = con.getDatabase();


        do {
            opcao = menu();
            try {
                switch (opcao) {
                    case 1:
                        UsuarioController.createUsuario(database);
                        break;
                    case 2:
                        escolheUsuario(database);
                        break;
                    case 3:
                        FuncionarioController.createFuncionario(database);
                        break;
                    case 4:
                        LivroController.createLivro(database);
                        break;
                    case 5:
                        escolheLivro(database);
                        break;
                    case 6:
                        RegistroController.listarRegistros(database);
                        break;


                    default:
                        System.out.println("Saindo...\n");
                        break;
                }


            }catch (InsertException | SelectException | UpdateException | ParseException | SQLException ex) {
                System.out.println(ex.getMessage());
            }
        }while(opcao>0 && opcao<7); // lembrar de mudar isso quando tiver o tamanho final do menu

        con.closeConexao();
    }


    /* fazer um menu que permite:
            * empréstimo de um livro para um usuário (Tem que anotar o id_usuário e o nro_livro junto com os campos da tabela
            * as verificações se o usuário em questão pode emprestar livros (chama as funções valida_emprestimo e checa_devolucao)
            * reservar um livro já emprestado por outro usuário
            * renovação do empréstimo do usuário por no máximo 3 vezes
        */

    public static int menu() {
        System.out.println("\nBem vindo ao sistema de gerenciamento de Biblioteca! Para iniciar, Escolha seu usuário ou crie um novo.");
        System.out.println("1: Criar Usuario\n2: Escolher Usuario ja existente\n3: Criar Funcionario\n4: Adicionar Livro\n5: Adicionar Autor para Livro\n6: Mostrar empréstimos\nEscreva qualquer outro numero para sair\n");
        Scanner sc = new Scanner(System.in);
        return sc.nextInt();
    }

    public static void menuUsuario(UsuarioBean ub, MongoDatabase database) throws InsertException, SelectException, ParseException, SQLException, UpdateException {
        Scanner sc = new Scanner(System.in);
        System.out.println("1: Emprestar Livro\n2: Renovar livro\n3: Reservar Livro\n4: Adicionar Telefone extra\n");

        int escolha_usuario = sc.nextInt();

        switch(escolha_usuario){

            case 1:
                LivroController.emprestaLivro(ub,database);
                UsuarioController.AddLivro(ub,database);
                break;
            case 2:
                RegistroController.renovaLivro(ub,database);
                break;
            case 3:
               RegistroController.reservaLivro(ub,database);
                break;
            case 4:
                UsuarioController.createFoneExtra(ub,database);
        }

    }

    private static void escolheLivro(MongoDatabase database) throws SelectException {
        MongoCollection<LivroBean> collection = database.getCollection("livro",LivroBean.class);
        Scanner sc = new Scanner(System.in);

        LivroController.listarLivros(database);
        System.out.println("Escolha um livro (por ISBN): ");
        int escolha_livro = sc.nextInt();
        new LivroBean();
        LivroBean lb;
        lb = collection.find(eq("iSBN",escolha_livro)).first();
        System.out.println("livro escolhido foi: "+lb.getISBN()+"\n");
        LivroController.addAutorExtra(lb,database);

    }


    public static void escolheUsuario(MongoDatabase database) throws SelectException, InsertException, ParseException, UpdateException, SQLException {
        MongoCollection<UsuarioBean> collection = database.getCollection("usuario",UsuarioBean.class);

        Scanner sc = new Scanner(System.in);

        UsuarioController.listarUsuarios(database);
        System.out.println("Escolha um usuario (por ID): ");
        int escolha = sc.nextInt();
        UsuarioBean ub = new UsuarioBean();
        ub = collection.find(eq("id_usuario",escolha)).first();
        menuUsuario(ub, database);


    }
}
