CREATE TABLE produtos
(
    id int PRIMARY KEY,
    nome VARCHAR(50)

);

CREATE TABLE precos
(
    id int PRIMARY KEY,
    valor DECIMAL(14,2) NOT NULL,
    desconto_maximo DECIMAL (5,2) NOT NULL,
    CONSTRAINT ck_desconto check (desconto_maximo > 0)

);

CREATE TABLE proutos_preco
(
    id_produtos int FOREIGN KEY  REFERENCES produtos(id),
    id_precos int FOREIGN KEY  REFERENCES precos(id),
    ativo int NOT NULL DEFAULT(0) -- 1 para ativo / 0 para inativo
);