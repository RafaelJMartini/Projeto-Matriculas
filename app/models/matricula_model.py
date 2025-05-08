class RegistroAno:
    def __init__(self, ano, matriculados):
        self.ano = ano
        self.matriculados = matriculados

class RegistroFaculdade:
    def __init__(self, faculdade, matriculados):
        self.faculdade = faculdade
        self.matriculados = matriculados

class Matricula:
    def __init__(self, nome_curso, matriculados):
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