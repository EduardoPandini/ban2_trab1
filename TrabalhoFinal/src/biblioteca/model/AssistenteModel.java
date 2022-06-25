package biblioteca.model;

import biblioteca.view.FuncionarioBean;
import com.mongodb.BasicDBObject;
import com.mongodb.MongoException;
import com.mongodb.client.MongoCollection;
import com.mongodb.client.MongoDatabase;
import com.mongodb.client.model.Projections;
import biblioteca.exceptions.UpdateException;
import org.bson.conversions.Bson;

import static com.mongodb.client.model.Filters.eq;
public class AssistenteModel {
    public static void create(FuncionarioBean fb, MongoDatabase database, int escolha) throws UpdateException {
        MongoCollection<FuncionarioBean> collection = database.getCollection("funcionario", FuncionarioBean.class);
        Bson query_id_func = eq("id_assistente", null);
        int id_bibliotecario = collection.find().projection(Projections.include("id_bibliotecario")).first().getId_funcionario();
        try{
            long id_assistente = collection.countDocuments(query_id_func);
            BasicDBObject query = new BasicDBObject();
            query.put("cpf",fb.getCpf());
            System.out.println("o cpf do funcionario eh: "+fb.getCpf()+"\n");
            BasicDBObject push_id_assistente = new BasicDBObject("$set", new BasicDBObject("id_assistente",id_assistente));
            collection.findOneAndUpdate(query,push_id_assistente);
            BasicDBObject push_id_bibliotecario = new BasicDBObject("$set", new BasicDBObject("id_bibliotecario",id_bibliotecario));
            collection.findOneAndUpdate(query,push_id_bibliotecario);


        }catch (MongoException ex){
            throw new UpdateException("Erro na atualização de funcionario");
        }

    }
}
