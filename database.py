import sqlite3
from typing import List, Tuple

def create_connection():
    conn = sqlite3.connect("transporte.db")
    return conn

def create_tables():
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS setores (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL
    );
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS demandas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        setor_id INTEGER,
        descricao TEXT NOT NULL,
        categoria TEXT NOT NULL,
        FOREIGN KEY (setor_id) REFERENCES setores (id)
    );
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS veiculos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        placa TEXT NOT NULL,
        modelo TEXT NOT NULL,
        tipo TEXT NOT NULL,
        lotacao INTEGER NOT NULL,
        motorista TEXT NOT NULL
    );
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS solicitacoes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        setor_id INTEGER,
        demanda_id INTEGER,
        grande_volume INTEGER,
        horario TEXT NOT NULL,
        tempo_estimado INTEGER,
        FOREIGN KEY (setor_id) REFERENCES setores (id),
        FOREIGN KEY (demanda_id) REFERENCES demandas (id)
    );
    """)

    conn.commit()
    conn.close()

create_tables()

def add_setor(nome: str) -> None:
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO setores (nome) VALUES (?)", (nome,))
    conn.commit()
    conn.close()

def update_setor(id: int, novo_nome: str) -> None:
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE setores SET nome = ? WHERE id = ?", (novo_nome, id))
    conn.commit()
    conn.close()

def get_setores() -> List[Tuple[int, str]]:
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, nome FROM setores")
    setores = cursor.fetchall()
    conn.close()
    return setores

def add_demanda(setor_id: int, descricao: str, categoria: str) -> None:
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO demandas (setor_id, descricao, categoria) VALUES (?, ?, ?)", (setor_id, descricao, categoria))
    conn.commit()
    conn.close()

def update_demanda(id: int, nova_descricao: str, nova_categoria: str) -> None:
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE demandas SET descricao = ?, categoria = ? WHERE id = ?", (nova_descricao, nova_categoria, id))
    conn.commit()
    conn.close()

def get_demandas(setor_id=None) -> List[Tuple[int, int, str, str]]:
    conn = create_connection()
    cursor = conn.cursor()
    if setor_id is None:
        cursor.execute("SELECT id, setor_id, descricao, categoria FROM demandas")
    else:
        cursor.execute("SELECT id, setor_id, descricao, categoria FROM demandas WHERE setor_id = ?", (setor_id,))
    demandas = cursor.fetchall()
    conn.close()
    return demandas

def add_veiculo(placa: str, modelo: str, tipo: str, lotacao: int, motorista: str) -> None:
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO veiculos (placa, modelo, tipo, lotacao, motorista) VALUES (?, ?, ?, ?, ?)", (placa, modelo, tipo, lotacao, motorista))
    conn.commit()
    conn.close()

def update_veiculo(id: int, nova_placa: str, novo_modelo: str, novo_tipo: str, nova_lotacao: int, novo_motorista: str) -> None:
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE veiculos SET placa = ?, modelo = ?, tipo = ?, lotacao = ?, motorista = ? WHERE id = ?", (nova_placa, novo_modelo, novo_tipo, nova_lotacao, novo_motorista, id))
    conn.commit()
    conn.close()

def get_veiculos() -> List[Tuple[int, str, str, str, int, str]]:
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, placa, modelo, tipo, lotacao, motorista FROM veiculos")
    veiculos = cursor.fetchall()
    conn.close()
    return veiculos

def add_solicitacao(setor_id: int, demanda_id: int, grande_volume: bool, horario: str, tempo_estimado: int) -> None:
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO solicitacoes (setor_id, demanda_id, grande_volume, horario, tempo_estimado) VALUES (?, ?, ?, ?, ?)", (setor_id, demanda_id, grande_volume, horario, tempo_estimado))
    conn.commit()
    conn.close()

def organizar_solicitacoes() -> List[Tuple[int, int, int, bool, str, int]]:
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("""
    SELECT s.id, s.setor_id, s.demanda_id, s.grande_volume, s.horario, s.tempo_estimado
    FROM solicitacoes s
    JOIN demandas d ON s.demanda_id = d.id
    ORDER BY d.categoria
    """)
    solicitacoes_organizadas = cursor.fetchall()
    conn.close()
    return solicitacoes_organizadas
