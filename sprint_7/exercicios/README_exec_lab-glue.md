# Exercício: Configuração e Execução do AWS Glue e Lake Formation

Este repositório contém as etapas e evidências relacionadas ao exercício de configuração de permissões, criação de roles, jobs e crawlers no AWS Glue e Lake Formation. As imagens de suporte estão localizadas na pasta `exercicios\evidencias_exercicios\` e são referenciadas ao longo do documento.



## Etapas do Exercício

### 1. Criando a IAM Role para os jobs do AWS Glue
A criação da IAM Role é o primeiro passo, como mostrado abaixo:

![Criar Função](../exercicios/evidencias_exercicios/criar_funcao.png)



### 2. Adicionando Permissões
Na etapa **Add permissions**, foi selecionada a permissão **AmazonS3FullAccess**:

![Add Permission](../exercicios/evidencias_exercicios/add_permission.png)



### 3. Finalizando a Criação da Role
Informe o nome da role como `AWSGlueServiceRole-Lab4` e clique em **Create Role**:

![Create Role](../exercicios/evidencias_exercicios/create_role.png)



### 4. Perfil Criado
Visualize o perfil criado conforme a imagem abaixo:

![Perfil Criado](../exercicios/evidencias_exercicios/perffil_criado.png)



### 5. Configurando o AWS Glue
Para configurar o AWS Glue, siga os passos abaixo:

1. Indique as roles que terão acesso ao serviço AWS Glue, selecionando a role `AWSGlueServiceRole-Lab4` em **Choose roles**:

![Config Glue](../exercicios/evidencias_exercicios/config_glue.png)

2. No próximo passo, forneça acesso total ao S3 para leitura e escrita:

![Total Access](../exercicios/evidencias_exercicios/total_acess.png)

3. Marque a opção **Update the standard AWS Glue service role and set it as the default (recommended)** e finalize o processo clicando em **Next** e depois **Apply changes**:

![Update Glue](../exercicios/evidencias_exercicios/update_glue.png)



### 6. Configurando o AWS Lake Formation
Acesse o AWS Lake Formation e, no menu **Databases**, clique em **Create Database**:

![Create Database](../exercicios/evidencias_exercicios/creat_batabase.png)

#### Database Criado
Veja o resultado da criação do database:

![Database Criado](../exercicios/evidencias_exercicios/database_criado.png)



### 7. Criando Novo Job no AWS Glue
1. Na página inicial, busque por **Visual ETL** em **ETL jobs** e clique em **Script editor**:

![Script Editor](../exercicios/evidencias_exercicios/script-editor.png)

2. Crie o script conforme necessário:

![Create Script](../exercicios/evidencias_exercicios/create_script.png)

#### Exemplo de Script
Veja um exemplo de script criado:

![Script Exemplo](../exercicios/evidencias_exercicios/sript-exemplo.png)

#### Parar Execuções Ativas
Para evitar conflitos, interrompa os jobs em execução:

![Execução Parada](../exercicios/evidencias_exercicios/exec_parada.png)

#### Resultado
Construa o job nos moldes descritos e veja o resultado:

![Frequência de Nomes](../exercicios/evidencias_exercicios/frequencia_nomes.png)

#### Logs de Execução
Verifique os logs no CloudWatch:

![Logs de Execução](../exercicios/evidencias_exercicios/logs_exec.png)



### 8. Criando Crawler
1. Na tela inicial, selecione o **FrequenciaRegistroNomesCrawler** e clique em **Run**:

![Crawler](../exercicios/evidencias_exercicios/craweler.png)



### 9. Usando o Athena
Abra o Athena com o comando SQL gerado e certifique-se de que esteja configurado conforme a imagem abaixo:

![SQL Athena](../exercicios/evidencias_exercicios/sql-athena.png)

#### Tabela Gerada
Veja a tabela resultante:

![Tabela Gerada](../exercicios/evidencias_exercicios/tabela_gerada.png)

