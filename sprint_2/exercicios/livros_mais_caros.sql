select l.cod as CodLivro, l.titulo as Titulo, a.codautor as CodAutor, a.nome as NomeAutor, l.valor as Valor, e.codeditora as CodEditora, e.nome as NomeEditora
from livro l
join autor a on l.autor = a.codautor
join editora e on l.editora = e.codeditora
order by l.valor desc
limit 10;
