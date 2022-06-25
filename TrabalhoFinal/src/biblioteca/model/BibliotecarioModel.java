package biblioteca.model;

import biblioteca.view.FuncionarioBean;
import com.mongodb.BasicDBObject;
import com.mongodb.MongoException;
import com.mongodb.client.MongoCollection;
import com.mongodb.client.MongoDatabase;
import biblioteca.exceptions.SelectException;
import biblioteca.exceptions.UpdateException;
import org.bson.conversions.Bson;

import java.util.LinkedList;
import java.util.List;

import static com.mongodb.client.model.Filters.eq;

public class BibliotecarioModel{
    public static void create(FuncionarioBean fb, MongoDatabase database) throws UpdateException {
        Bson query = eq("id_bibliotecario", 0);
        MongoCollection<FuncionarioBean> collection = database.getCollection("funcionario", FuncionarioBean.class);
        try{
            long id_bibliotecario = collection.countDocuments(query);
            if (id_bibliotecario == 0){ // não encontrou nenhum bibliotecário, portanto é o primeiro a ser inserido. Então o id_bibliotecário = 0 pra esse funcionario;
                BasicDBObject query_primeiro_biblio = new BasicDBObject();
                query_primeiro_biblio.put("cpf",fb.getCpf());
                BasicDBObject push_id = new BasicDBObject("$set", new BasicDBObject("id_bibliotecario",id_bibliotecario));
                collection.findOneAndUpdate(query_primeiro_biblio,push_id);

            }else{// se o bibliotecário já existe, o id_bibliotecário já vai ter um valor. É só adicionar o valor já existente pra esse funcionário;
                BasicDBObject query_existente_biblio = new BasicDBObject();
                query_existente_biblio.put("cpf",fb.getCpf());
                BasicDBObject push_id = new BasicDBObject("$set", new BasicDBObject("id_bibliotecario",id_bibliotecario));
                collection.findOneAndUpdate(query_existente_biblio,push_id);
                // que puta dor de cabeça foi conseguir fazer essa query junto com o count, cacete.


            }
        }catch (MongoException ex){
            throw new UpdateException("Erro ao atualizar funcionario");
        }
    }

    public static List<FuncionarioBean> listAll(MongoDatabase database) throws SelectException {
        MongoCollection<FuncionarioBean> collection = database.getCollection("funcionario",FuncionarioBean.class);
        try{
            List<FuncionarioBean> funcionarios;
            funcionarios = collection.find().into(new LinkedList<>());
            return funcionarios;

        }catch (MongoException ex){
            throw new SelectException("Erro ao procurar funcionarios");
        }
    }
}
