from app import app
from flask import render_template
from app.repositories.matricula_repository import MatriculaRepository
from app.dao.matricula_dao import MatriculaDAO
from app.models.matricula_model import PlaceHolders

dao = MatriculaDAO()
repo = MatriculaRepository(dao)
placeH = PlaceHolders(repo.place_holders())

@app.route('/')
def index():
    return render_template("home.html")

@app.route('/matriculas_por_ano')
def matriculas_por_ano():
    return render_template("matriculasAno.html", ph=placeH)

@app.route('/matriculas_por_ano/<estado>/<modalidade>')
def matriculas_por_ano_estado(estado, modalidade):

    estado = None if estado == 'all' else estado
    modalidade = None if modalidade == 'all' else modalidade
    dados_por_ano = repo.total_matriculas_por_ano(modalidade,estado)
    repo.add_consulta(consulta=f"/matriculas_por_ano/{estado or 'all'}/{modalidade or 'all'}", resultado=dados_por_ano)
    return render_template('matriculasAno.html',dados=dados_por_ano, ph=placeH,modalidade=modalidade, estado=estado)
@app.route('/ranking_cursos')
def ranking_cursos_geral():
    return render_template('rankingCursos.html', ph=placeH)

@app.route('/ranking_cursos/<estado>/<ano>')
def ranking_cursos(estado,ano):
    estado = None if estado == 'all' else estado
    ano = None if ano == 'all' else ano
    dados_por_curso = repo.total_matriculas_por_curso(estado,ano)
    repo.add_consulta(consulta=f"/ranking_cursos/{estado or 'all'}/{ano or 'all'}", resultado=dados_por_curso)
    return render_template('rankingCursos.html', ph=placeH, dados=dados_por_curso, ano=ano, estado=estado)

@app.route('/faculdades_por_matricula')
def faculdades_por_matricula_geral():
    return render_template('faculdadesMatricula.html',ph=placeH)

@app.route('/faculdades_por_matricula/<estado>/<ano>')
def faculdades_por_matricula(estado,ano):
    estado = None if estado == 'all' else estado
    ano = None if ano == 'all' else ano
    dados = repo.total_matriculas_por_faculdade(estado,ano)
    repo.add_consulta(consulta=f"/faculdades_por_matricula/{estado or 'all'}/{ano or 'all'}", resultado=dados)
    return render_template('faculdadesMatricula.html', ph=placeH, ano=ano, estado=estado, dados=dados)

@app.route('/ultimas_consultas')
def ultimas_consultas():
    consultas = repo.get_consultas()
    return render_template("ultimasConsultas.html", consultas=consultas)

