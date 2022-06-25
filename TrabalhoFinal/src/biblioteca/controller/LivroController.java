package biblioteca.controller;

import biblioteca.model.LivroModel;
import biblioteca.view.LivroBean;
import biblioteca.view.UsuarioBean;
import com.mongodb.MongoException;
import com.mongodb.client.MongoCollection;
import com.mongodb.client.MongoDatabase;
import biblioteca.exceptions.InsertException;
import biblioteca.exceptions.SelectException;

import java.text.ParseException;
import java.time.LocalDate;
import java.util.*;

public class LivroController {
    public static void createLivro(MongoDatabase database) throws InsertException {
        MongoCollection<LivroBean> collection = database.getCollection("livro",LivroBean.class);

        Scanner sc = new Scanner(System.in);
        System.out.println("Insira os dados para a criacao de um livvro no sistema\n Titulo: ");
        String titulo = sc.nextLine();
        System.out.println("\nSeu numero de ISBN:  ");
        int isbn = sc.nextInt();
        sc.nextLine();
        System.out.println("Seu autor: ");
        List<String> autores = new ArrayList<>();
        autores.add(sc.nextLine()) ;
        System.out.println("Sua editora: ");
        String editora = sc.nextLine();
        System.out.println("E a sua colecao (publica ou reserva): ");
        String colecao = sc.nextLine();

        LivroBean lb = new LivroBean(titulo, (ArrayList<String>) autores,isbn,editora,colecao);
        LivroModel.create(lb, database);
        //LivroModel.addAutor(lb,con);
    }


    public static void emprestaLivro(UsuarioBean ub, MongoDatabase database) throws SelectException, InsertException, ParseException {
        Scanner sc = new Scanner(System.in);

        if (ub.getValorMulta()>0){
            System.out.println("Não pode emprestar um livro com multas pendentes!");
            return;
        }

        LocalDate data = LocalDate.now(); // pega a data atual para empréstimo
        System.out.println("Escolha um livro para emprestar! (Por ISBN): ");
        listarLivros(database);
        int escolha_livro = sc.nextInt();
        LivroBean livro_escolhido = LivroModel.escolheLivro(escolha_livro,database);
        if(livro_escolhido.getColecao().equalsIgnoreCase("reserva")){
            System.out.println("Um livro da reserva não pode ser emprestado!");
            return;
        }
        LivroModel.addEmprestimo(livro_escolhido,ub,data,database);


    }

    public static void addAutorExtra(LivroBean lb, MongoDatabase database) throws SelectException {
        try{
            Scanner sc = new Scanner(System.in);
            System.out.println("Entre com um autor para ser agregado ao livro: ");
            String autor = sc.nextLine();
            LivroModel.addAutorExtra(lb,autor,database);
        }catch(MongoException ex){
            throw new SelectException("Erro na insercao de autor no livro");
        }
        System.out.println("Autor adicionado com sucesso!");
    }


    public static void listarLivros(MongoDatabase database) throws SelectException {
        List<LivroBean> all = LivroModel.listAll(database);
        for (LivroBean livroBean : all) {
            System.out.println(livroBean);
        }
    }



}
