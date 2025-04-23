CREATE TABLE matriculas (
    id SERIAL PRIMARY KEY,
    estado VARCHAR(50),
    cidade VARCHAR(100),
    ies VARCHAR(150),
    sigla VARCHAR(10),
    organizacao VARCHAR(100),
    categoria VARCHAR(100),
    nome_curso VARCHAR(150),
    nome_detalhado VARCHAR(150),
    modalidade VARCHAR(20),
    grau VARCHAR(50),
    ano INT,
    matriculados INT
);