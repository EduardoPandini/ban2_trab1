package biblioteca.model;

import biblioteca.view.RegistroBean;
import biblioteca.view.UsuarioBean;
import com.mongodb.MongoException;
import com.mongodb.client.MongoCollection;
import com.mongodb.client.MongoDatabase;
import biblioteca.exceptions.SelectException;
import biblioteca.exceptions.UpdateException;

import java.util.LinkedList;
import java.util.List;
import static com.mongodb.client.model.Filters.*;
public class RegistroModel {


    public static List<RegistroBean> listAll(MongoDatabase database) throws SelectException {
        MongoCollection<RegistroBean> collection = database.getCollection("registros",RegistroBean.class);
        try{
            List<RegistroBean> registros;
            registros = collection.find().into(new LinkedList<>());
            return registros;
        }catch (MongoException ex){
            throw new SelectException("Erro ao procurar pelo registro");
        }


    }

    public static RegistroBean escolheRegistro(int escolha_registro, MongoDatabase database){
        MongoCollection<RegistroBean> collection = database.getCollection("registros",RegistroBean.class);
        RegistroBean rb = new RegistroBean();
        rb = collection.find(eq("id_registro",escolha_registro)).first();

        return rb;
    }

    public static void renovaLivro(RegistroBean registro_escolhido, UsuarioBean ub, MongoDatabase database) throws UpdateException {
        MongoCollection<RegistroBean> collection = database.getCollection("registros",RegistroBean.class);
        int valor_renovado = registro_escolhido.getRenovado()+1;
        registro_escolhido.setRenovado(valor_renovado);

        if(registro_escolhido.getRenovado()>3){
            System.out.println("Renovação de livros máxima alcançada!");
            return;
        }

        try{
            collection.replaceOne(eq("id_registro",registro_escolhido.getId_registro()), registro_escolhido);
        }catch (MongoException ex){
            throw new UpdateException("Erro ao renovar livro");
        }
    }


    public static void reservaLivro(RegistroBean registro_escolhido, UsuarioBean ub, MongoDatabase database) throws UpdateException{
        MongoCollection<RegistroBean> collection = database.getCollection("registros",RegistroBean.class);
        registro_escolhido.setReservado(true);
        try{
            collection.replaceOne(eq("id_registro",registro_escolhido.getId_registro()),registro_escolhido);
        }catch (MongoException ex){
            throw new UpdateException("Erro ao reservar livro");
        }
    }
}
