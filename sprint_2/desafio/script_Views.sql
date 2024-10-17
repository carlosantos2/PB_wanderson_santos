-- criação de views
-- View para a Dimensão Cliente
CREATE VIEW vw_DimCliente AS
SELECT 
    idCliente,
    nomeCliente,
    cidadeCliente,
    estadoCliente,
    paisCliente
FROM DimCliente;

-- View para a Dimensão Carro
CREATE VIEW vw_DimCarro AS
SELECT 
    C.idCarro,
    C.marcaCarro,
    C.modeloCarro,
    C.anoCarro,
    C.kmCarro,
    C.classiCarro,
    Comb.tipoCombustivel
FROM DimCarro C
JOIN DimCombustivel Comb ON C.idCombustivel = Comb.idCombustivel;

-- View para a Dimensão Combustível
CREATE VIEW vw_DimCombustivel AS
SELECT 
    idCombustivel,
    tipoCombustivel
FROM DimCombustivel;

-- View para a Dimensão Vendedor
CREATE VIEW vw_DimVendedor AS
SELECT 
    idVendedor,
    nomeVendedor,
    sexoVendedor,
    estadoVendedor
FROM DimVendedor;

-- vieew para consultas
CREATE VIEW vw_FatoLocacoes AS
SELECT 
    FatoLocacoes.idLocacao,
    DimCliente.nomeCliente,
    DimCarro.marcaCarro,
    DimCarro.modeloCarro,
    DimVendedor.nomeVendedor,
    FatoLocacoes.dataLocacao,
    FatoLocacoes.dataEntrega,
    FatoLocacoes.qtdDiaria,
    FatoLocacoes.vlrDiaria,
    FatoLocacoes.qtdDiaria * FatoLocacoes.vlrDiaria AS valorTotal
FROM 
    FatoLocacoes
JOIN DimCliente ON FatoLocacoes.idCliente = DimCliente.idCliente
JOIN DimCarro ON FatoLocacoes.idCarro = DimCarro.idCarro
JOIN DimVendedor ON FatoLocacoes.idVendedor = DimVendedor.idVendedor;

