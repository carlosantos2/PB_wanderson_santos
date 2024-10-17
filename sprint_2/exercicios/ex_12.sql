-- Apresente a query para listar código, nome e data de nascimento dos dependentes do vendedor com menor valor total bruto em vendas (não sendo zero). As colunas presentes no resultado devem ser cddep, nmdep, dtnasc e valor_total_vendas.
-- Observação: Apenas vendas com status concluído.
select
tbd.cddep, 
tbd.nmdep,
tbd.dtnasc,
sum(tbvendas.qtd * tbvendas.vrunt) as valor_total_vendas
from tbdependente as tbd 
left join tbvendedor 
on tbd.cdvdd = tbvendedor.cdvdd 
left join tbvendas 
on tbvendedor.cdvdd = tbvendas.cdvdd 
where 
tbvendas.status = 'Concluído'
group by tbd.cddep, tbd.nmdep, tbd.dtnasc
having sum(tbvendas.qtd * tbvendas.vrunt)> 0
order by sum(tbvendas.qtd * tbvendas.vrunt) 
limit 1
