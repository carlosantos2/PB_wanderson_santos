-- Apresente a query para listar os 10 produtos menos vendidos pelos canais de E-Commerce ou Matriz (Considerar apenas vendas concluídas).  As colunas presentes no resultado devem ser cdpro, nmcanalvendas, nmpro e quantidade_vendas.

select 
tbv.cdpro,
tbv.nmcanalvendas,
tbv.nmpro,
sum(qtd) as quantidade_vendas
from tbvendas as tbv
where (nmcanalvendas = 'Ecommerce' or nmcanalvendas = 'Matriz')
and status = 'Concluído'
group by tbv.cdpro, tbv.nmcanalvendas, tbv.nmpro
order by quantidade_vendas
limit 10
