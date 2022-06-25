package biblioteca.conexao;

import com.mongodb.*;

import com.mongodb.client.MongoClient;
import com.mongodb.client.MongoClients;
import com.mongodb.client.MongoDatabase;
import org.bson.codecs.configuration.CodecRegistry;
import org.bson.codecs.pojo.PojoCodecProvider;

import static org.bson.codecs.configuration.CodecRegistries.fromProviders;
import static org.bson.codecs.configuration.CodecRegistries.fromRegistries;

/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 *
 * @author rebeca
 * (obrigado rs)
 */

public class Conexao {
    private static Conexao conexao = null;
    private CodecRegistry pojoCodecRegistry;
    private MongoClientSettings settings;
    private MongoClient mongoClient;
    private MongoDatabase database;

    public Conexao() {
        pojoCodecRegistry = fromRegistries(MongoClientSettings.getDefaultCodecRegistry(),
                fromProviders(PojoCodecProvider.builder().automatic(true).build()));

        settings = MongoClientSettings.builder().codecRegistry(pojoCodecRegistry).build();

        mongoClient = MongoClients.create(settings);
        database = mongoClient.getDatabase("Biblioteca");

    }



    public static Conexao getConexao() {
        if(conexao == null){
            conexao = new Conexao();
        }

        return conexao;
    }

    public MongoDatabase getDatabase(){
        return database;
    }


    public void closeConexao(){
        mongoClient.close();
    }
}
