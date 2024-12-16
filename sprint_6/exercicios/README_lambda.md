# Exercicio 3- lambda 

### Guia para Configuração do AWS Lambda com Layer Personalizada


## Etapa 1: Criar a função do Lambda
![Etapa 1 - Criar a função do Lambda](../exercicios/criar_lamb.png)


## Etapa 2: Construir o código
Construa o código necessário para sua função Lambda.  
![Etapa 2 - Construir o código](../exercicios/func_lamb.png)

### Teste do Lambda
Realize o teste clicando em **Test** e escolha um nome para o teste.  
Ao executar, o erro abaixo deve ser exibido:  
![Erro durante o teste](../exercicios/teste_lsmb.jpg)


## Etapa 3: Criar uma Layer

### Passo 1: Criar uma pasta e o arquivo Dockerfile
Crie uma nova pasta e, nela, um arquivo chamado **Dockerfile**.  
![Passo 1 - Criação do Dockerfile](../exercicios/criar_dockerfile.png)

### Passo 2: Criar a imagem Docker
Use o arquivo **Dockerfile** para gerar a imagem Docker.  
![Passo 2 - Criação da imagem Docker](../exercicios/executar_docker.png)

### Passo 3: Acessar o shell do container
Execute o comando para acessar o shell do container Docker.  
![Passo 3 - Acesso ao shell do container](../exercicios/comando_cd.png)

### Passo 4: Criar a pasta para bibliotecas
No shell do container, crie uma pasta chamada **python** para armazenar as bibliotecas.  
![Passo 4 - Criação da pasta python](../exercicios/comandos_outros.png)

### Passo 5: Instalar as bibliotecas
Baixe as bibliotecas e suas dependências na pasta **python**.  
![Passo 5 - Instalação das bibliotecas](../exercicios/baixar_bibliotecas.png)

### Passo 6: Compactar o diretório python
Compacte todos os arquivos da pasta **python** em um arquivo ZIP.  
![Passo 6 - Compactação do diretório python](../exercicios/compactar_dir.png)

### Passo 7: Copiar o ZIP para a máquina local
Abra outro terminal, descubra o ID do container e copie o arquivo ZIP para sua máquina local.  
![Passo 7 - Cópia do ZIP para a máquina local](../exercicios/id_cont.png)

### Passo 8: Fazer upload para o S3
Faça o upload do arquivo ZIP para um bucket S3.  
![Passo 8 - Upload do ZIP para o S3](../exercicios/buck.png)

### Passo 9: Criar a camada no AWS Lambda
No painel do AWS Lambda, crie uma nova camada, dê o nome **PandasLayer** e use a URL do S3 para fazer o upload.  
![Passo 9 - Criação da camada no Lambda](../exercicios/pandas_layer.png)

---

## Etapa 4: Utilizar a Layer
1. Escolha **Custom Layers** (Camadas personalizadas).

2. Localize a camada e versão criadas.
![camada](../exercicios/criar_lamb.png)

3. Execute novamente o código utilizando o teste configurado.  

![Etapa 4 - Utilização da Layer](../exercicios/resultado_lamb.png)

---

## Exemplo de URL no S3
```plaintext
https://s3.us-east-1.amazonaws.com/testecompass.com/minha-camada-pandas.zip

