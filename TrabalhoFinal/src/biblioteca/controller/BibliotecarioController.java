package biblioteca.controller;

import biblioteca.model.BibliotecarioModel;
import biblioteca.view.FuncionarioBean;
import com.mongodb.client.MongoDatabase;
import biblioteca.exceptions.SelectException;

import java.util.List;

public class BibliotecarioController {


    public static void listarFuncionarios(MongoDatabase database) throws SelectException {
        List<FuncionarioBean> all = BibliotecarioModel.listAll(database);
        for (FuncionarioBean bb:all) {
            System.out.println(bb);
        }
    }


}
