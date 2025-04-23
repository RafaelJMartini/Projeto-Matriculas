from app.dao.matricula_dao import MatriculaDAO

class MatriculaRepository:
    def __init__(self, dao: MatriculaDAO):
        self.dao = dao

    def total_matriculas_por_ano(self, modalidade=None):
        return self.dao.get_matriculas_por_ano(modalidade)