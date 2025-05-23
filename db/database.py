from db.conexao import conectar

# Inicia o banco de dados
def inicializar_banco():

    con = conectar()    
    cursor = con.cursor()
    # Cria a tabela no banco de dados
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tarefas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            descricao TEXT,
            criado_em TEXT,
            previsao_termino TEXT,
            concluida INTEGER DEFAULT 0
    ) 
""")

    con.commit()
    con.close()
