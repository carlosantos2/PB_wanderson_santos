-- Apresente a query para listar o código e o nome do vendedor com maior número de vendas (contagem), e que estas vendas estejam com o status concluída.  As colunas presentes no resultado devem ser, portanto, cdvdd e nmvdd.

select 
cdvdd, 
nmvdd
from tbvendedor 
where cdvdd = (select cdvdd 
from tbvendas
where status = 'Concluído'
group by cdvdd 
order by count (cdvdd) desc limit 1)