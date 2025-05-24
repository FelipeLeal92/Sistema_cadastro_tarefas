import typer
from datetime import datetime
from typing_extensions import Annotated
from controlador.gerenciador import GerenciadorDeTarefas

app = typer.Typer()


@app.command()  # -- Cadastrar tarefas -----------------------------------------------------
def cadastrar(
    titulo: str = typer.Option(..., prompt="Título da tarefa"), 
              descricao: str = typer.Option(..., prompt="Descrição"),
              previsao_termino: str = typer.Option(..., prompt="Previsão de término (dd-mm-aaaa)"),
              concluida: bool = typer.Option(False, help="Marcar como concluída")
    ):
     
    tarefas = GerenciadorDeTarefas()
    criado_em = datetime.now().isoformat()
    concluida_int = 1 if concluida else 0
    
    tarefas.cadastrar_tarefa(
        titulo=titulo, 
        descricao=descricao,
        criado_em=criado_em, 
        previsao_termino=previsao_termino,
        concluida=concluida_int
    )
 
    typer.echo(f"Tarefa {titulo} cadastrada com sucesso. Previsão de termino {previsao_termino}.")
    tarefas.fechar()


@app.command()  # -- Listar tarefas -----------------------------------------------------
def listar(filtro: str = 'todas'):
    
    tarefas = GerenciadorDeTarefas()
    lista = tarefas.listar_tarefa(filtro)
    print(type(lista))
    print(f"DEBUG - Tipo de lista: {type(lista)}, Conteúdo: {lista}")
    
    if not lista:
        typer.echo("❌ Nenhuma tarefa encontrada.")
        return

    typer.echo("\n📋 Lista de Tarefas:")
    for tarefa in lista:
        id, titulo, descricao, criado_em, previsao_termino, concluida = tarefa
        status = "✅ Concluída" if concluida else "❗ Pendente"
        typer.echo(f"""
---------------------------------------------------------------------------------------------------------------------------
🆔 ID: {id} | 📝 Título: {titulo}
📄 Descrição: {descricao} | 🕓 Criada em: {criado_em} | ⏳ Previsão de término: {previsao_termino} | 📌 Status: {status}
---------------------------------------------------------------------------------------------------------------------------
""")
        
    tarefas.fechar()


@app.command()  # -- Concluir tarefas --------------------------------------------------------
def concluir(id: int):
    tarefas = GerenciadorDeTarefas()
    lista = tarefas.listar_tarefa('pendentes')
    
    if any(t[0] == id for t in lista):
        tarefas.marcar_concluida(id)
        typer.echo(f"Tarefa com ID {id} concluída com sucesso.")
    else:
        typer.echo(f"Nenhuma tarefa pendente encontrada com ID {id}.")
    
    listar('pendentes')
    tarefas.fechar()
   

@app.command()  # -- Excluir tarefas --------------------------------------------------------
def excluir(id: int, force: Annotated[bool, typer.Option(prompt=f'Tem certeza que deseja deletar esta tarefa?')]):
    tarefas = GerenciadorDeTarefas()
    lista = tarefas.listar_tarefa('todas')
    
    if force:
        tarefas.excluir_tarefa(id)
        typer.echo(f"Tarefa deletada: {id}")
        listar('todas')
    else:
        print("Operção cancelada")
    
    tarefas.fechar()
    

@app.command()  # -- Atualizar tarefas --------------------------------------------------------
def atualizar(
            force: Annotated[bool, typer.Option(prompt=f'Tem certeza que deseja atualizar esta tarefa?')],
            id: Annotated[int, typer.Argument(..., help="ID da tarefa a ser atualizada")],
            titulo: str = typer.Option(..., prompt="Título da tarefa"), 
            descricao: str = typer.Option(..., prompt="Descrição"),
            previsao_termino: str = typer.Option(..., prompt="Previsão de término (dd-mm-aaaa)"),
            concluida: bool = typer.Option(False, help="Marcar como concluída", prompt="Marcar tarefa como concluída?"),
    ):
        
    if not force:
        typer.echo("Operação cancelada.")
        return
    
    tarefas = GerenciadorDeTarefas()
    concluida_int = 1 if concluida else 0
    
    tarefas.atualizar_tarefa(
        id=id,
        titulo=titulo, 
        descricao=descricao,
        previsao_termino=previsao_termino,
        concluida = concluida_int
    )
  
    typer.echo(f"Tarefa ID {id} atualizada com sucesso.")
    #exibir_tarefa(id) # Criar função para exibir só a tarefa atualizada/criada/concluida
    tarefas.fechar()


if __name__ == "__main__": 
    app()