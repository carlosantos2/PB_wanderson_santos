  --Apresente a query para listar o autor com maior número de livros publicados. O resultado deve conter apenas as colunas codautor, nome, quantidade_publicacoes.

select 
aut.codautor,
aut.nome,
count(lv.cod) as quantidade_publicacoes 
from livro as lv
left join autor as aut 
on lv.autor = aut.codautor 
group by aut.codautor, aut.nome 
order by quantidade_publicacoes desc
limit 1