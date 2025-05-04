CREATE TABLE faculdades (
    id SERIAL PRIMARY KEY,
    estado TEXT,
    cidade TEXT,
    ies TEXT,
    sigla TEXT,
    organizacao TEXT,
    categoria_administrativa TEXT,
    nome_curso TEXT,
    nome_detalhado TEXT,
    modalidade TEXT,
    grau TEXT
);

CREATE TABLE matriculas (
    id SERIAL PRIMARY KEY,
    faculdade_id INT REFERENCES faculdades(id),
    ano INT,
    numero_matriculados INT
);

-- Uma tabela temporária que recebe o CSV inteiro
CREATE TABLE temp_faculdades (
    estado TEXT,
    cidade TEXT,
    ies TEXT,
    sigla TEXT,
    organizacao TEXT,
    categoria_administrativa TEXT,
    nome_curso TEXT,
    nome_detalhado TEXT,
    modalidade TEXT,
    grau TEXT,
    a2014 INT,
    a2015 INT,
    a2016 INT,
    a2017 INT,
    a2018 INT,
    a2019 INT,
    a2020 INT,
    a2021 INT,
    a2022 INT
);

CREATE TABLE consultas (
    id SERIAL PRIMARY KEY,
    consulta TEXT,
    resultado JSON,
    data_consulta TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

COPY temp_faculdades FROM '/caminho/para/arquivo.csv' DELIMITER ';' CSV HEADER;

INSERT INTO faculdades (
    estado, cidade, ies, sigla, organizacao, categoria_administrativa,
    nome_curso, nome_detalhado, modalidade, grau
)
SELECT DISTINCT
    estado, cidade, ies, sigla, organizacao, categoria_administrativa,
    nome_curso, nome_detalhado, modalidade, grau
FROM temp_faculdades;

INSERT INTO matriculas (faculdade_id, ano, numero_matriculados)
SELECT f.id, ano::INT, numero_matriculados
FROM (
    SELECT
        tf.estado, tf.cidade, tf.ies, tf.sigla, tf.organizacao, tf.categoria_administrativa,
        tf.nome_curso, tf.nome_detalhado, tf.modalidade, tf.grau,
        unnest(ARRAY[2014,2015,2016,2017,2018,2019,2020,2021,2022]) AS ano,
        unnest(ARRAY[a2014, a2015, a2016, a2017, a2018, a2019, a2020, a2021, a2022]) AS numero_matriculados
    FROM temp_faculdades tf
) AS dados
JOIN faculdades f ON
    f.estado = dados.estado AND f.cidade = dados.cidade AND f.ies = dados.ies AND
    f.sigla = dados.sigla AND f.organizacao = dados.organizacao AND
    f.categoria_administrativa = dados.categoria_administrativa AND
    f.nome_curso = dados.nome_curso AND f.nome_detalhado = dados.nome_detalhado AND
    f.modalidade = dados.modalidade AND f.grau = dados.grau;