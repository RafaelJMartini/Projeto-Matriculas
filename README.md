# Sistema matrículas

Nomes: Douglas B. e Rafael M.

**Linguagem:** Python<br/>
**Framework:**  Flask<br/>
**Arquitetura:**  MVC (Model View Controller)<br/>
**Persistência:**  Repository + DAO + PostgreSQL<br/>
**Interface:**  Web (HTML + CSS com Jinja2 no Flask)<br/>
**Fonte de dados:** Matriculados Brasil - Projeto.csv

Objetivo: Fazer análises agregadas por curso, ano, estado e modalidade, com armazenamento de consultas recentes.

---

## Execução do projeto:

1. Crie um ambiente e instale todos os requisitos do arquivo "*requirements.txt*".

2. Crie um arquivo .env no diretório raíz, com os seguintes conteúdos:

    ```
    USER = 'postgres'
    PORT = '5432'
    ENROLL_TABLE = 'matriculas'
    PW = 'ucs'
    HOST = 'localhost'
    ```

3. Com PostgreSQL instalado, crie um banco de dados "matriculas" e rode o arquivo "create.sql" da pasta "data" no pgAdmin.

    (Na linha 52, mude o caminho para encontrar o CSV.)<br/>
    (Se o postgresql não tiver permissão, pôr em um diretório no C:\ e rodar a partir de lá.)
    <br/><br/>
    Assim deve ficar:

    <img src="docs/postgresql_overview.png"/>

4. Execute o arquivo run.py 