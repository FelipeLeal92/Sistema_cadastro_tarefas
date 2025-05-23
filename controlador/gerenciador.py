from db.conexao import conectar
from models.tarefa import Tarefa

# Classe que irá gerencias todas as  funcionalidades do sistema
class GerenciadorDeTarefas:

   # Inicializar a classe
    def __init__(self):
        self.con = conectar()
        self.cursor = self.con.cursor()
        

    # Recurso para criação de tarefa
    def cadastrar_tarefa(self, tarefa: Tarefa):
        try:
            self.cursor.execute("""
                                INSERT INTO tarefas (titulo, descricao, criado_em, previsao_termino, concluida)
                                VALUES (?, ?, ?, ?, ?)
                                """, (tarefa.titulo, tarefa.descricao, tarefa.criado_em, tarefa.previsao_termino, tarefa.concluida))           
            print(f'Tarefa {tarefa.titulo} cadastrada com sucesso')
            self.con.commit()
        except Exception as e:
            print(f"Ocorreu um erro: {e}")
            self.con.rollback()
            self.con.commit()      
        
        
    # Recurso para listar as tarefas    
    def listar_tarefa(self, filtro='todas'):
        if filtro == 'todas':
            self.cursor.execute("SELECT * FROM tarefas ORDER BY datetime(criado_em) DESC")
        
        elif filtro == 'pendentes':
            self.cursor.execute("SELECT * FROM tarefas WHERE concluida = 0 ORDER BY datetime(criado_em) DESC")
            
        elif filtro == 'concluidas':
            self.cursor.execute("SELECT * FROM tarefas WHERE concluida = 1 ORDER BY datetime(criado_em) DESC")
           
        return self.cursor.fetchall()
    

    # Recurso para marcar tarefa como concluida      
    def marcar_concluida(self, id: int):
        try:
            self.cursor.execute("UPDATE tarefas SET concluida=1 WHERE id = ?", (id,))
            self.con.commit()
        except Exception as e:
            print(f"Ocorreu um erro: {e}")
            self.con.rollback()
            self.con.commit()
        

    # Recurso para excluir tarefa        
    def excluir_tarefa(self, id: int):
        try:
            self.cursor.execute("DELETE FROM tarefas WHERE id=?", (id,))
            print(f'Tarefa com  ID: {id} excluido com sucesso')
            self.con.commit()
        except Exception as e:
            print(f"Ocorreu um erro: {e}")
            self.con.rollback()            
            self.con.commit()
        
           
    # Recurso para fechar a conexão com o banco de dados     
    def fechar(self):
        self.con.close()