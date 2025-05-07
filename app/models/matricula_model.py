class RegistroAno:
    def __init__(self, ano, num_matriculados):
        self.ano = ano
        self.num_matriculados = num_matriculados

class RegistroFaculdade:
    def __init__(self, faculdade, matriculados):
        self.faculdade = faculdade
        self.matriculados = matriculados

class Matricula:
    def __init__(self, estado, modalidade, nome_curso, ano, matriculados):
        self.nome_curso = nome_curso
        self.matriculados = matriculados

class PlaceHolders:
    def __init__(self, lista):
        anos, modalidades, estados = lista
        modalidades = [m[0] for m in modalidades]
        anos = [a[0] for a in anos]
        estados = [e[0] for e in estados]

        self.anos = anos
        self.modalidades = modalidades
        self.estados = estados