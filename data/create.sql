CREATE TABLE faculdades (
    id_facul SERIAL PRIMARY KEY,
    estado VARCHAR(50),
    cidade VARCHAR(100),
    ies VARCHAR(150),
    sigla VARCHAR(10),
    organizacao VARCHAR(100),
    categoria VARCHAR(100),
    nome_curso VARCHAR(150),
    nome_detalhado VARCHAR(150),
    modalidade VARCHAR(20),
    grau VARCHAR(50)
);

CREATE TABLE matriculados (
    id SERIAL PRIMARY KEY,
    id_facul INT REFERENCES faculdades(id_facul),
    ano INT,
    matriculados INT
);