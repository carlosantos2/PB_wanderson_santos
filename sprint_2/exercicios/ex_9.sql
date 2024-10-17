-- Apresente a query para listar o código e nome do produto mais vendido entre as datas de 2014-02-03 até 2018-02-02, e que estas vendas estejam com o status concluída. As colunas presentes no resultado devem ser cdpro e nmpro.          

select 
tbv.cdpro,
tbv.nmpro
from tbvendas as tbv
where tbv.dtven between '2014-02-03' and '2018-02-02' 
and tbv.status = 'Concluído'
group by tbv.cdpro, tbv.nmpro 
order by sum(tbv.qtd) desc 
limit 1 
