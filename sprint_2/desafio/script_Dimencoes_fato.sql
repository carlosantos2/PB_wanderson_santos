-- segunda parte, tabelas dimencional.

-- dimençao  cliente
CREATE TABLE DimCliente (
    idCliente INT PRIMARY KEY,
    nomeCliente VARCHAR(100),
    cidadeCliente VARCHAR(40),
    estadoCliente VARCHAR(40),
    paisCliente VARCHAR(40)
);
-- Dimenção carro
CREATE TABLE DimCarro (
    idCarro INT PRIMARY KEY,
    marcaCarro VARCHAR(80),
    modeloCarro VARCHAR(80),
    anoCarro INT,
    kmCarro INT,
    classiCarro VARCHAR(50),
    idCombustivel INT,
    FOREIGN KEY (idCombustivel) REFERENCES DimCombustivel(idCombustivel)
);

-- Dimenção combustivel
CREATE TABLE DimCombustivel (
    idCombustivel INT PRIMARY KEY,
    tipoCombustivel VARCHAR(20)
);
-- Dimenção Vendedor
CREATE TABLE DimVendedor (
    idVendedor INT PRIMARY KEY,
    nomeVendedor VARCHAR(15),
    sexoVendedor SMALLINT,
    estadoVendedor VARCHAR(40)
);
-- Tabela De Fatos
CREATE TABLE FatoLocacoes (
    idLocacao INT PRIMARY KEY,
    idCliente INT,
    idCarro INT,
    idVendedor INT,
    dataLocacao DATETIME,
    horaLocacao TIME,
    dataEntrega DATE,
    horaEntrega TIME,
    qtdDiaria INT,
    vlrDiaria DECIMAL(18,2),
    FOREIGN KEY (idCliente) REFERENCES DimCliente(idCliente),
    FOREIGN KEY (idCarro) REFERENCES DimCarro(idCarro),
    FOREIGN KEY (idVendedor) REFERENCES DimVendedor(idVendedor)
);
