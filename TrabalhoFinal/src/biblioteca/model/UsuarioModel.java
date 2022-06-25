package biblioteca.model;

import com.mongodb.BasicDBObject;
import com.mongodb.MongoException;
import biblioteca.exceptions.*;
import biblioteca.view.UsuarioBean;
import com.mongodb.client.MongoCollection;
import com.mongodb.client.MongoDatabase;
import java.util.LinkedList;
import java.util.List;
import static com.mongodb.client.model.Filters.*;

public class UsuarioModel{

    public static void create(UsuarioBean ub, MongoDatabase database) throws InsertException{
        MongoCollection<UsuarioBean> collection = database.getCollection("usuario",UsuarioBean.class);
        long id_usuario = collection.estimatedDocumentCount();
        ub.setId_usuario((int) id_usuario);
        try{
            collection.insertOne(ub);
        }catch (MongoException ex){
            throw new InsertException("Erro na insercao de usuario");
        }
    }


    public static void addFoneExtra(UsuarioBean ub, int telefone, MongoDatabase database) throws SelectException {
        MongoCollection<UsuarioBean> collection = database.getCollection("usuario",UsuarioBean.class);
        BasicDBObject query = new BasicDBObject();
        query.put("nome",ub.getNome());
        System.out.println("o id desse caralho eh: "+ub.get_id()+"\n");
        BasicDBObject push_data = new BasicDBObject("$push", new BasicDBObject("telefones",telefone));
        collection.findOneAndUpdate(query,push_data);

    }

    public static void addLivroExtra(UsuarioBean ub, MongoDatabase database) throws UpdateException{
        MongoCollection<UsuarioBean> collection = database.getCollection("usuario",UsuarioBean.class);
        int quant_livros = ub.getQntLivros()+1;

        if (ub.getCategoria() == 1 && ub.getQntLivros()>=3){ // 15 dias
            System.out.println("Numero máximo de livros excedido!");
            return;
        }
        else{
            if ((ub.getCategoria() == 2 && ub.getQntLivros() >= 5) || (ub.getCategoria() == 3 && ub.getQntLivros() >= 7 )){ // 30 dias
                System.out.println("Numero máximo de livros excedido!");
                return;
            }else{ // categoria == 4, 90 dias
                if (ub.getCategoria() == 4 && ub.getQntLivros() >= 9){
                    System.out.println("Numero máximo de livros excedido!");
                    return;
                }else{
                    ub.setQntLivros(quant_livros); // tá nos conformes, então pode seguir
                }
            }
        }

        try{

            collection.replaceOne(eq("id_usuario",ub.getId_usuario()),ub);
            System.out.println("Livro emprestado com sucesso!");
        }catch (MongoException ex){
            throw new UpdateException("Erro adicionando livro extra ao usuario");
        }

    }


    public static List<UsuarioBean> listAll(MongoDatabase database) throws SelectException{
        MongoCollection<UsuarioBean> collection = database.getCollection("usuario",UsuarioBean.class);

        try{
            List<UsuarioBean> usuarios;
            usuarios = collection.find().into(new LinkedList<UsuarioBean>());
            return usuarios;
        }catch (MongoException ex){
            throw new SelectException("Erro ao procurar usuarios");
        }
    }

}
