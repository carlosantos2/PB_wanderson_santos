select e.codeditora as CodEditora, e.nome as NomeEditora, COUNT(l.cod) as QuantidadeLivros
from livro l
join editora e on l.editora = e.codeditora
group by e.codeditora, e.nome
order by QuantidadeLivros desc
limit 5;
