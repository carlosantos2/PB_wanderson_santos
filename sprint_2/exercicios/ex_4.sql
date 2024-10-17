--Apresente a query para listar a quantidade de livros publicada por cada autor. Ordenar as linhas pela coluna nome (autor), em ordem crescente. Além desta, apresentar as colunas codautor, nascimento e quantidade (total de livros de sua autoria).

select 
aut.nome,
aut.codautor,
aut.nascimento, 
count(lv.cod) quantidade
from autor as aut
left join livro as lv 
on aut.codautor = lv.autor 
group by aut.nome 
order by aut.nome