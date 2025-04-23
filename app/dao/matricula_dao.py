from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class MatriculaDAO:
    def __init__(self, db_connection):
        self.db = db_connection

    def get_matriculas_por_ano(self, modalidade=None):
        query = """
        SELECT ano, SUM(matriculados) 
        FROM matriculas
        {}
        GROUP BY ano
        ORDER BY ano;
        """.format("WHERE modalidade = %s" if modalidade else "")

        cursor = self.db.cursor()
        cursor.execute(query, (modalidade,) if modalidade else ())
        return cursor.fetchall()