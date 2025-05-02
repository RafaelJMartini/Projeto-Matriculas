
class Matricula:
    def __init__(self, estado, modalidade, nome_curso, ano, matriculados):
        self.estado = estado
        self.modalidade = modalidade
        self.nome_curso = nome_curso
        self.ano = ano
        self.matriculados = matriculados

class PlaceHolders:
    def __init__(self, anos,modalidades):
        modalidades = [m[0] for m in modalidades]
        anos = [a[0] for a in anos]

        self.anos = anos
        self.modalidades = modalidades