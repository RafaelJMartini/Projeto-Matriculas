from app import app
from flask import render_template, request, redirect
from app.repositories.matricula_repository import MatriculaRepository
from app.dao.matricula_dao import MatriculaDAO
from app.models.matricula_model import PlaceHolders
import json

dao = MatriculaDAO()
repo = MatriculaRepository(dao)
placeH = PlaceHolders(repo.place_holders())

@app.route('/')
def index():
    return render_template("home.html")


@app.route('/matriculas_por_ano')
def matriculas_por_ano():
    return redirect(f"/matriculas_por_ano/home/pesquisa")

@app.route('/matriculas_por_ano/<estado>/<modalidade>', methods=["GET","POST"])
def matriculas_por_ano_estado(estado, modalidade):
    estado = None if estado == 'all' else estado
    modalidade = None if modalidade == 'all' else modalidade

    if request.method == 'POST':
        estado = request.form.get('estado') or 'all'
        modalidade = request.form.get('modalidade') or 'all'
        return redirect(f"/matriculas_por_ano/{estado}/{modalidade}")

    if modalidade != 'pesquisa':
        dados_por_ano = repo.total_matriculas_por_ano(modalidade, estado)
        repo.add_consulta(consulta=f"/matriculas_por_ano/{estado or 'all'}/{modalidade or 'all'}", resultado=dados_por_ano)
    else:
        dados_por_ano = None

    return render_template('matriculasAno.html', dados=dados_por_ano, ph=placeH, modalidade=modalidade, estado=estado)
@app.route('/ranking_cursos')
def ranking_cursos_geral():
    return redirect(f"/ranking_cursos/home/pesquisa")

@app.route('/ranking_cursos/<estado>/<ano>', methods=["GET","POST"])
def ranking_cursos(estado,ano):
    estado = None if estado == 'all' else estado
    ano = None if ano == 'all' else ano

    if request.method == 'POST':
        estado = request.form.get('estado') or 'all'
        ano = request.form.get('ano') or 'all'
        return redirect(f"/ranking_cursos/{estado}/{ano}")

    if ano != 'pesquisa':
        dados_por_curso = repo.total_matriculas_por_curso(estado,ano)
        repo.add_consulta(consulta=f"/ranking_cursos/{estado or 'all'}/{ano or 'all'}", resultado=dados_por_curso)
    else:
        dados_por_curso = None

    return render_template('rankingCursos.html', ph=placeH, dados=dados_por_curso, ano=ano, estado=estado)


@app.route('/faculdades_por_matricula')
def faculdades_por_matricula_geral():
    return redirect(f"/faculdades_por_matricula/home/pesquisa")

@app.route('/faculdades_por_matricula/<estado>/<ano>', methods=["GET","POST"])
def faculdades_por_matricula(estado,ano):
    estado = None if estado == 'all' else estado
    ano = None if ano == 'all' else ano

    if request.method == 'POST':
        estado = request.form.get('estado') or 'all'
        ano = request.form.get('ano') or 'all'
        return redirect(f"/faculdades_por_matricula/{estado}/{ano}")

    if ano != 'pesquisa':
        dados = repo.total_matriculas_por_faculdade(estado,ano)
        repo.add_consulta(consulta=f"/faculdades_por_matricula/{estado or 'all'}/{ano or 'all'}", resultado=dados)
    else:
        dados = None

    return render_template('faculdadesMatricula.html', ph=placeH, ano=ano, estado=estado, dados=dados)

@app.route('/ultimas_consultas')
def ultimas_consultas():
    dados = repo.get_consultas()
    consultas = []
    for linha in dados:
        consulta_dict = dict(linha._mapping)
        try:
            if isinstance(consulta_dict["resultado"], str):
                consulta_dict["resultado"] = json.loads(consulta_dict["resultado"])
        except Exception:
            consulta_dict["resultado"] = []
        consultas.append(consulta_dict)

    return render_template("ultimasConsultas.html", consultas=consultas)

