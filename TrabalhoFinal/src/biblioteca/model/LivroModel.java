package biblioteca.model;

import biblioteca.view.LivroBean;
import biblioteca.view.RegistroBean;
import biblioteca.view.UsuarioBean;
import com.mongodb.BasicDBObject;
import com.mongodb.MongoException;
import com.mongodb.client.MongoCollection;
import com.mongodb.client.MongoDatabase;
import biblioteca.exceptions.InsertException;
import biblioteca.exceptions.SelectException;

import static com.mongodb.client.model.Filters.*;

import java.text.ParseException;
import java.time.LocalDate;
import java.util.LinkedList;
import java.util.List;

public class LivroModel {

    public static void create(LivroBean lb, MongoDatabase database) throws InsertException {
        MongoCollection<LivroBean> collection = database.getCollection("livro",LivroBean.class);
        try{
            collection.insertOne(lb);
        }catch (MongoException ex){
            throw new InsertException("Erro na insercao do livro");
        }


    }


    public static LivroBean escolheLivro(int escolha_livro, MongoDatabase database){
        MongoCollection<LivroBean> collection = database.getCollection("livro",LivroBean.class);
        LivroBean lb = new LivroBean();
        lb = collection.find(eq("iSBN",escolha_livro)).first();

        return lb;
    }

    public static void addEmprestimo(LivroBean lb, UsuarioBean ub, LocalDate data, MongoDatabase database) throws InsertException, ParseException {
        MongoCollection<RegistroBean> collection = database.getCollection("registros",RegistroBean.class);
        long cont = collection.estimatedDocumentCount();
        if(lb.getColecao().equalsIgnoreCase("reserva")){
            System.out.println("Um livro da coleção de reserva não pode ser emprestado!");
            return;
        }
        RegistroBean rb = new RegistroBean();
        rb.setId_registro((int) cont);
        rb.setId_usuario(ub.getId_usuario());
        rb.setNro_livro(lb.getISBN());

        rb.setData(data);
        if (ub.getCategoria() == 1 && ub.getQntLivros()<3){ // 15 dias
            rb.setData_devolucao(data.plusDays(15));
        }
        else{
            if ((ub.getCategoria() == 2 && ub.getQntLivros() < 5) || (ub.getCategoria() == 3 && ub.getQntLivros() < 7 )){ // 30 dias
                rb.setData_devolucao(data.plusDays(30));
            }else{ // categoria == 4, 90 dias
                if (ub.getCategoria() == 4 && ub.getQntLivros() < 9){
                    rb.setData_devolucao(data.plusDays(90));
                }else{
                    System.out.println("Numero de livros excedida!!");
                    return;
                }
            }
        }

        try{
            collection.insertOne(rb);
        }catch (MongoException ex){
            throw new InsertException("Erro na insercao do registro");
        }



        // fazer rotina server-side pra verificar categoria e incrementar qnt_livros || FEITO! checa_categoria();
    }

    public static void addAutorExtra(LivroBean lb, String autor, MongoDatabase database){
        MongoCollection<LivroBean> collection = database.getCollection("livro",LivroBean.class);
        BasicDBObject query = new BasicDBObject();
        query.put("iSBN",lb.getISBN());
        BasicDBObject push_data = new BasicDBObject("$push", new BasicDBObject("autores",autor));
        collection.findOneAndUpdate(query,push_data);


    }



    public static List<LivroBean> listAll(MongoDatabase database) throws SelectException {
        MongoCollection<LivroBean> collection = database.getCollection("livro",LivroBean.class);

        try{
            List<LivroBean> livros;
            livros = collection.find().into(new LinkedList<LivroBean>());
            return livros;
        }catch (MongoException ex){
            throw new SelectException("Erro ao procurar usuarios");
        }

    }



}
