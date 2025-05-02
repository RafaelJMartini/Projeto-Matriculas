from sqlalchemy import text

class MatriculaDAO:
    def __init__(self, engine):
        self.engine = engine

    def get_place_holders(self):
        query = """
        SELECT DISTINCT ano
        FROM matriculas
        """

        query1 = """
        SELECT DISTINCT modalidade
        FROM faculdades
        """
        with self.engine.connect() as conexao:
            resultado1 = conexao.execute(text(query)).fetchall()
            resultado2 = conexao.execute(text(query1)).fetchall()

        return resultado1,resultado2

    def get_matriculas_por_ano(self, modalidade=None):
        query = """
        SELECT m.ano, SUM(m.numero_matriculados)
        FROM matriculas m
        JOIN faculdades f ON f.id = m.faculdade_id
        {}
        GROUP BY ano
        ORDER BY ano;
        """.format("WHERE f.modalidade = :modalidade" if modalidade else "")

        with self.engine.connect() as conexao:
            if modalidade:
                resultado = conexao.execute(text(query), {"modalidade": modalidade}).fetchall()
            else:
                resultado = conexao.execute(text(query)).fetchall()

        return resultado

    def get_matriculas_por_curso(self, ano=None):
        query = """
        SELECT f.nome_curso, SUM(m.numero_matriculados)
        FROM matriculas m
        JOIN faculdades f ON f.id = m.faculdade_id
        WHERE m.numero_matriculados IS NOT NULL
        {}
        GROUP BY f.nome_curso
        ORDER BY SUM(m.numero_matriculados) DESC
        LIMIT 10;
        """.format("AND m.ano = :ano" if ano else "")

        with self.engine.connect() as conexao:
            if ano:
                resultado = conexao.execute(text(query), {"ano": ano}).fetchall()
            else:
                resultado = conexao.execute(text(query)).fetchall()
        return resultado