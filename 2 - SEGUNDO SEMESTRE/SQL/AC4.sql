--AC4 (LINGUAGEM SQL)
--Autor: Alexandro Barros de Carvalho
--Email: alexandro.carvalho@aluno.faculdadeimpacta.com.br
--Data: 19/04/2020



CREATE DATABASE CONCESSIONARIA --Criação da base de dados
GO

USE CONCESSIONARIA --Seleciona a base de dados
GO

CREATE TABLE Ano --Tabela ano com chave primária idAno
(
    idAno INT NOT NULL IDENTITY(1,1),
    ano INT NOT NULL,
    CONSTRAINT PK_IDANO PRIMARY KEY(idAno)
)
GO

CREATE TABLE Mes --Tabela ano com chave primária idMes
(
    idMes INT NOT NULL IDENTITY(1,1),
    mes INT NOT NULL,
    CONSTRAINT PK_IDMES PRIMARY KEY(idMes)
)
GO

CREATE TABLE Modelo --Tabela com modelos dos veículos com chave primária idModelo
(
    idModelo INT NOT NULL IDENTITY(1,1),
    Descricao VARCHAR(50),
    CONSTRAINT PK_IDMODELO PRIMARY KEY(idModelo)
)
GO

CREATE TABLE Fabricante --Tabela com os fabricantes com chave primária idFabricante
(
    idFabricante INT NOT NULL IDENTITY(1,1),
    Nome VARCHAR(50),
    cidade VARCHAR(50),
    endereco VARCHAR(50),
    UF CHAR(2),
    telefone VARCHAR(14),
    contato VARCHAR(50)
    CONSTRAINT PK_FABRICANTE PRIMARY KEY(idFabricante)
)
GO

CREATE TABLE Veiculo --Tabela de veículos com PK idVeiculo, FKs idModelo, idFabricante e idAnoFabricacao
(
    idVeiculo INT NOT NULL IDENTITY(1,1),
    descricao VARCHAR(50),
    valor FLOAT NOT NULL,
    idModelo INT NOT NULL,
    idFabricante INT NOT NULL,
    idAnoFabricacao INT NOT NULL,
    dataCompra DATE,
    CONSTRAINT PK_IDVEICULO PRIMARY KEY(idVeiculo),
    CONSTRAINT FK_IDMODELO FOREIGN KEY(idModelo) REFERENCES Modelo(idModelo),
    CONSTRAINT FK_IDFABRICANTE FOREIGN KEY(idFabricante) REFERENCES Fabricante(idFabricante),
    CONSTRAINT FK_IDANOFABRICACAO FOREIGN KEY(idAnoFabricacao) REFERENCES Ano(idAno)
)
GO

CREATE TABLE VendasAnuais -- Tabela de Vendas com PK idVendas, FKs idVeiculo, idAnodaVenda e idMesdaVenda
(
    idVendas INT NOT NULL IDENTITY(1,1),
    qtd INT NOT NULL,
    idVeiculo INT NOT NULL,
    idAnodaVenda INT NOT NULL,
    idMesdaVenda INT NOT NULL,
    CONSTRAINT PK_IDVENDAS PRIMARY KEY (idVendas),
    CONSTRAINT FK_IDVEICULOS FOREIGN KEY (idVeiculo) REFERENCES Veiculo(idVeiculo),
    CONSTRAINT FK_IDANOVENDA FOREIGN KEY (idAnodaVenda) REFERENCES Ano(idAno),
    CONSTRAINT FK_IDMESDAVENDA FOREIGN KEY (idMesdaVenda) REFERENCES Mes(idMes)
)
GO