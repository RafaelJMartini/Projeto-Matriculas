import base64
import json
import urllib.parse
from datetime import datetime
from sqlalchemy import text

class MatriculaDAO:
    def __init__(self, engine):
        self.engine = engine

    def get_place_holders(self):
        query1 = """
        SELECT DISTINCT ano
        FROM matriculas
        """

        query2 = """
        SELECT DISTINCT modalidade
        FROM faculdades
        """

        query3 = """
        SELECT DISTINCT estado
        FROM faculdades
        """

        with self.engine.connect() as conexao:
            resultado1 = conexao.execute(text(query1)).fetchall()
            resultado2 = conexao.execute(text(query2)).fetchall()
            resultado3 = conexao.execute(text(query3)).fetchall()


        return resultado1, resultado2, resultado3

    def get_matriculas_por_ano(self, modalidade=None, estado=None):
        filtros = []
        params = {}

        if modalidade:
            filtros.append("AND f.modalidade = :modalidade")
            params["modalidade"] = modalidade

        if estado:
            filtros.append("AND f.estado = :estado")
            params["estado"] = estado

        filtro_sql = "\n        ".join(filtros)

        query = f"""
        SELECT m.ano, SUM(m.numero_matriculados)
        FROM matriculas m
        JOIN faculdades f ON f.id = m.faculdade_id
        WHERE m.ano IS NOT NULL
            {filtro_sql}
        GROUP BY ano
        ORDER BY ano;
        """

        with self.engine.connect() as conexao:
            resultado = conexao.execute(text(query), params).fetchall()

        return resultado

    def get_matriculas_por_curso(self,estado=None,ano=None):
        filtros = []
        params = {}

        if estado:
            filtros.append("AND f.estado = :estado")
            params["estado"] = estado

        if ano:
            filtros.append("AND m.ano = :ano")
            params["ano"] = ano

        print("DEBUG estado:", estado)
        print("DEBUG ano:", ano)

        filtro_sql = "\n        ".join(filtros)
        query = f"""
        SELECT f.nome_curso, SUM(m.numero_matriculados)
        FROM matriculas m
        JOIN faculdades f ON f.id = m.faculdade_id
        WHERE m.numero_matriculados IS NOT NULL
        {filtro_sql}
        GROUP BY f.nome_curso
        ORDER BY SUM(m.numero_matriculados) DESC
        LIMIT 10;
        """

        with self.engine.connect() as conexao:
            resultado = conexao.execute(text(query), params).fetchall()

        return resultado

    def add_consulta(self, consulta, resultado):
        teste = dict(resultado)
        teste = json.dumps(teste)

        query = "INSERT INTO consultas (consulta, resultado, data_consulta) "
        query += f"VALUES ('{consulta}', '{teste}', '{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}');"
        print(query)
        with self.engine.connect() as conexao:
            transaction = conexao.begin()
            result = conexao.execute(text(query))
            conexao.commit()
        print(result.rowcount)

        return None

    def get_consulta(self, numero=2):
        query = f"""
        SELECT * FROM consultas
        ORDER BY id DESC
        """
        with self.engine.connect() as conexao:
            resultado = conexao.execute(text(query)).fetchall()
        return resultado