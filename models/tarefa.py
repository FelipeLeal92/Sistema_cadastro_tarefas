from datetime import datetime

# Cria a classse de tarefas
class Tarefa:

    def __init__(self, titulo: str, descricao: str, previsao_termino: str, concluida: bool=False):
        self.titulo = titulo
        self.descricao = descricao
        self.criado_em = datetime.now()
        self.previsao_termino = previsao_termino
        self.concluida = concluida 

