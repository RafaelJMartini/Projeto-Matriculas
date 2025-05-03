
class Matricula:
    def __init__(self, estado, modalidade, nome_curso, ano, matriculados):
        self.estado = estado
        self.modalidade = modalidade
        self.nome_curso = nome_curso
        self.ano = ano
        self.matriculados = matriculados

class PlaceHolders:
    def __init__(self, anos,modalidades,estados):
        modalidades = [m[0] for m in modalidades]
        anos = [a[0] for a in anos]
        estados = [e[0] for e in estados]

        self.anos = anos
        self.modalidades = modalidades
        self.estados = estados