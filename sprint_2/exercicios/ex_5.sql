--Apresente a query para listar o nome dos autores que publicaram livros através de editoras NÃO situadas na região sul do Brasil. Ordene o resultado pela coluna nome, em ordem crescente.

Select distinct 
Autor.nome
From livro
Left join autor
On livro.autor = autor.codautor
Left join editora 
On livro.editora = editora.codeditora
Left join endereco 
On editora.endereco = endereco.codendereco
Where
Lower (endereco.estado) not like '%RIO GRANDE DO SUL %' and lower(endereco.estado) not like '%PARANÁ%'
Order by autor.nome
