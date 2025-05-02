from app import app
from flask import render_template, request
from app.repositories.matricula_repository import MatriculaRepository
from app.dao.matricula_dao import MatriculaDAO
from app.models.matricula_model import PlaceHolders
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

# Conexão com banco
load_dotenv()
engine = create_engine(f"postgresql+psycopg2://{os.getenv('USER')}:{os.getenv('PW')}@{os.getenv('HOST')}:{os.getenv('PORT')}/{os.getenv('SCHEMA')}")
dao = MatriculaDAO(engine)
repo = MatriculaRepository(dao)

anos, modalidades = repo.place_holders()
placeH = PlaceHolders(anos, modalidades)
@app.route('/')
def index():
    return render_template("home.html")

@app.route('/matriculas_por_ano')
def matriculas_por_ano():
    modalidade = request.args.get('modalidade')
    dados_por_ano = repo.total_matriculas_por_ano(modalidade)
    return render_template("matriculasAno.html", dados=dados_por_ano, ph=placeH, modalidade=modalidade)

@app.route('/ranking_cursos')
def ranking_cursos_geral():
    dados_por_curso = repo.total_matriculas_por_curso()
    return render_template('rankingCursos.html', ph=placeH, dados=dados_por_curso,geral=1)

@app.route('/ranking_cursos/<int:ano>')
def ranking_cursos(ano):
    dados_por_curso = repo.total_matriculas_por_curso(ano)
    return render_template('rankingCursos.html', ph=placeH, dados=dados_por_curso, ano_pesquisa=ano)