package biblioteca.view;
import org.bson.codecs.pojo.annotations.BsonProperty;
import org.bson.types.ObjectId;

import java.util.ArrayList;
import java.util.List;


public class LivroBean {
    private ObjectId _id;
    private String titulo;
    @BsonProperty("autores")
    private List<String> autores;
    private int ISBN;
    private String editora;
    private String colecao;

    public LivroBean(String titulo, ArrayList<String> autores, int ISBN, String editora, String colecao) {
        this.titulo = titulo;
        this.autores = autores;
        this.ISBN = ISBN;
        this.editora = editora;
        this.colecao = colecao;
    }

    public LivroBean(){

    }

    public LivroBean(String titulo, int isbn, String editora, String colecao) {
        this.titulo = titulo;
        this.ISBN = isbn;
        this.editora = editora;
        this.colecao = colecao;

    }

    public ObjectId get_id() {
        return _id;
    }

    public void set_id(ObjectId _id) {
        this._id = _id;
    }

    public String getTitulo() {
        return titulo;
    }

    public void setTitulo(String titulo) {
        this.titulo = titulo;
    }

    public List<String> getAutores() {
        return autores;
    }

    public void setAutores(ArrayList<String> autores) {
        this.autores = autores;
    }

    public int getISBN() {
        return ISBN;
    }

    public void setISBN(int ISBN) {
        this.ISBN = ISBN;
    }

    public String getEditora() {
        return editora;
    }

    public void setEditora(String editora) {
        this.editora = editora;
    }

    public String getColecao() {
        return colecao;
    }

    public void setColecao(String colecao) {
        this.colecao = colecao;
    }

    @Override public String toString(){
        return "Livro{ titulo: "+titulo+", isbn: "+ISBN+", editora: "+editora+", colecao: "+colecao;
    }
}
