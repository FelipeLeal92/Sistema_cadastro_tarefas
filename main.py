from db.database import inicializar_banco
from controlador. gerenciador import GerenciadorDeTarefas
from models.tarefa import Tarefa


inicializar_banco()
print("Banco inicializado com sucesso.")

nova_tarefa = Tarefa(titulo='Trabalhar', descricao='Trade', previsao_termino='30-05-2025', concluida='0' )


atividades = GerenciadorDeTarefas()
atividades.cadastrar_tarefa(nova_tarefa)


atividades.listar_tarefa('todas')
