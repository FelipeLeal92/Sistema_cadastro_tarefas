import typer
from controlador.gerenciador import GerenciadorDeTarefas

app = typer.Typer()

@app.command()
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

if __name__ == "__main__": 
    app()