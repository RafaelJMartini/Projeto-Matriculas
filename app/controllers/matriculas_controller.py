
from flask import Blueprint, render_template, request
from app.repositories.matricula_repository import MatriculaRepository
from app.dao.matricula_dao import MatriculaDAO
import psycopg2

bp = Blueprint('matriculas', __name__)

# Conexão com banco
conn = psycopg2.connect(dbname="seubanco", user="usuario", password="senha", host="localhost")
dao = MatriculaDAO(conn)
repo = MatriculaRepository(dao)

@bp.route('/')
def index():
    modalidade = request.args.get('modalidade')
    dados = repo.total_matriculas_por_ano(modalidade)
    return render_template("home.html", dados=dados)