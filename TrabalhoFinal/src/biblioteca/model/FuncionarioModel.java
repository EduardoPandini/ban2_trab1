package biblioteca.model;

import biblioteca.view.FuncionarioBean;
import com.mongodb.MongoException;
import com.mongodb.client.MongoCollection;
import com.mongodb.client.MongoDatabase;
import biblioteca.exceptions.InsertException;
import biblioteca.exceptions.SelectException;

import java.util.LinkedList;
import java.util.List;

public class FuncionarioModel {
    public static void create(FuncionarioBean fb, MongoDatabase database) throws InsertException {
        MongoCollection<FuncionarioBean> collection = database.getCollection("funcionario", FuncionarioBean.class);
        try {
                long id_funcionario = collection.estimatedDocumentCount();
                fb.setId_funcionario((int) id_funcionario);
                collection.insertOne(fb);
        } catch (MongoException ex) {
            throw new InsertException("Erro na insercao de funcionario");
        }
    }


    public static List<FuncionarioBean> listAll(MongoDatabase database) throws SelectException {
        MongoCollection<FuncionarioBean> collection = database.getCollection("funcionario", FuncionarioBean.class);
        try {
            List<FuncionarioBean> funcionarios;
            funcionarios = collection.find().into(new LinkedList<>());
            return funcionarios;
        } catch (MongoException ex) {
            throw new SelectException("Erro ao procurar funcionarios");
        }
    }
}
