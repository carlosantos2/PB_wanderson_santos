-- Apresente a query para listar o gasto médio por estado da federação. As colunas presentes no resultado devem ser estado e gastomedio. Considere apresentar a coluna gastomedio arredondada na segunda casa decimal e ordenado de forma decrescente.
--Observação: Apenas vendas com status concluído.

select 
tbv.estado,
round(round(sum(vrunt * qtd),2) / count(qtd),2) as gastomedio
from tbvendas as tbv
where status = 'Concluído'
group by estado 
order by gastomedio desc
