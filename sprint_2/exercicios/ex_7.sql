-- Apresente a query para listar o nome dos autores com nenhuma publicação. Apresentá-los em ordem crescente.

select 
nome
from autor 
where 
codautor not in (select autor from livro) 
order by nome