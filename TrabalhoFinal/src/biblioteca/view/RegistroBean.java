package biblioteca.view;

import org.bson.types.ObjectId;

import java.time.LocalDate;

public class RegistroBean {
        private ObjectId _id;
        private int id_registro;
        private LocalDate data;
        private LocalDate data_devolucao, devolvido;
        private boolean reservado;
        private int renovado;
        private int id_usuario;
        private int nro_livro;

        public RegistroBean(){

        }

        public RegistroBean(LocalDate data, LocalDate data_devolucao, LocalDate devolvido, boolean reservado, int renovado, int id_usuario, int nro_livro, int id_registro) {
                this.id_registro = id_registro;
                this.data = data;
                this.data_devolucao = data_devolucao;
                this.devolvido = devolvido;
                this.reservado = reservado;
                this.renovado = renovado;
                this.id_usuario = id_usuario;
                this.nro_livro = nro_livro;
        }

        public LocalDate getData() {
                return data;
        }

        public void setData(LocalDate data) {
                this.data = data;
        }

        public ObjectId get_id() {
                return _id;
        }

        public void set_id(ObjectId _id) {
                this._id = _id;
        }

        public LocalDate getData_devolucao() {
                return data_devolucao;
        }

        public void setData_devolucao(LocalDate data_devolucao) {
                this.data_devolucao = data_devolucao;
        }

        public LocalDate getDevolvido() {
                return devolvido;
        }

        public void setDevolvido(LocalDate devolvido) {
                this.devolvido = devolvido;
        }

        public boolean isReservado() {
                return reservado;
        }

        public void setReservado(boolean reservado) {
                this.reservado = reservado;
        }

        public int getRenovado() {
                return renovado;
        }

        public void setRenovado(int renovado) {
                this.renovado = renovado;
        }

        public int getId_usuario() {
                return id_usuario;
        }

        public void setId_usuario(int id_usuario) {
                this.id_usuario = id_usuario;
        }

        public int getNro_livro() {
                return nro_livro;
        }

        public void setNro_livro(int nro_livro) {
                this.nro_livro = nro_livro;
        }

        @Override
        public String toString() {
                return "Emprestimos{id_registro: "+id_registro+", nro_livro: "+nro_livro+", id_usuario: "+id_usuario+", data: "+data+ ", data_devolucao: "+data_devolucao+", reservado: "+reservado+", renovado: "+renovado;
        }

        public int getId_registro() {
                return id_registro;
        }

        public void setId_registro(int id_registro) {
                this.id_registro = id_registro;
        }
}
