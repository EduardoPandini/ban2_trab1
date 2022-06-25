package biblioteca.view;

import org.bson.types.ObjectId;

import java.util.List;

public class UsuarioBean {
    private ObjectId _id;
    private int id_usuario;
    private int valorMulta, qntLivros;
    private String nome, endereco;
    private List<Integer> telefones;
    private int categoria; // Categoria: 1 = Graduação; 2 = Pós-Graduação: 3 = Professor; 4 = Professor Pós;

    public UsuarioBean(){

    }

    public UsuarioBean(int valorMulta, int qntLivros, String nome, String endereco, List<Integer> telefones, int categoria) {
        this.valorMulta = valorMulta;
        this.qntLivros = qntLivros;
        this.nome = nome;
        this.endereco = endereco;
        this.telefones = telefones;
        this.categoria = categoria;
    }

    public UsuarioBean(String string, String string1, int anInt1, int anInt2, int anInt3) {
        this.valorMulta = anInt3;
        this.qntLivros = anInt2;
        this.nome = string;
        this.endereco = string1;
        this.categoria = anInt1;
    }

    public UsuarioBean(String string) {
        this.nome = string;

    }

    public ObjectId get_id() {
        return _id;
    }

    public void set_id(ObjectId _id) {
        this._id = _id;
    }

    public int getValorMulta() {
        return valorMulta;
    }

    public void setValorMulta(int valorMulta) {
        this.valorMulta = valorMulta;
    }

    public int getQntLivros() {
        return qntLivros;
    }

    public void setQntLivros(int qntLivros) {
        this.qntLivros = qntLivros;
    }

    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public String getEndereco() {
        return endereco;
    }

    public void setEndereco(String endereco) {
        this.endereco = endereco;
    }

    public List<Integer> getTelefones() {
        return telefones;
    }

    public void setTelefones(List<Integer> telefones) {
        this.telefones = telefones;
    }

    public int getCategoria() {
        return categoria;
    }

    public void setCategoria(int categoria) {
        this.categoria = categoria;
    }

    @Override public String toString() {
        return "Usuario{id: "+id_usuario+", nome:" + nome+ ", qntLivros: "+qntLivros+ ", valor_multa: "+valorMulta+ '}';
    }

    public int getId_usuario() {
        return id_usuario;
    }

    public void setId_usuario(int id_usuario) {
        this.id_usuario = id_usuario;
    }
}
