from app.dao.matricula_dao import MatriculaDAO

class MatriculaRepository:
    def __init__(self, dao: MatriculaDAO):
        self.dao = dao

    def place_holders(self):
        return self.dao.get_place_holders()

    def total_matriculas_por_ano(self, modalidade=None, estado=None):
        return self.dao.get_matriculas_por_ano(modalidade, estado)

    def total_matriculas_por_curso(self, estado=None,ano=None):
        return self.dao.get_matriculas_por_curso(estado,ano)