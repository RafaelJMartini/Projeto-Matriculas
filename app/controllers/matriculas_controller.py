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
    dados = repo.total_matriculas_por_ano(modalidade)
    return render_template("matriculasAno.html", dados=dados, ph=placeH)

@app.route('/ranking_cursos/<ano>')
def ranking_cursos(ano):
    if ano.isnumeric():
        dados = repo.total_matriculas_por_curso(ano)
        return render_template('rankingCursos.html', ano=ano, ph=placeH, dados=dados)
    else:
        return render_template('rankingCursos.html',ph=placeH)