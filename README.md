# POC Remote Authentication

## Objetivo
Criar uma poc que represente  um cenario onde possamos autenticar o usuario remotamente

Imagine que temos dois sistema e que o sistema externo contém a base de dados dos usuarios, e o  sistema novo nao possui a base de dados de usuario.

Como o django pode resolver este cenario?

    1 - Criar um sistema sem a autenticação nativa do django
    2 - Permite que o sistema externo possa ser autenticado com usuario e que gere um token
    3 - O sistema externo deverá permitir que o token seja validado


## Criterios do Sistema Novo
    1- Criação do DockerFile
    2- Criação do Compose com dois bancos, local e o externo
    3- Autenticação via HTTP_AUTHORIZATION
        3.1 - para que isso seja possivel será necessário criar um middleware que permita que as request seja interceptadas e autenticadas.
        3.2 - criar um backend services authentication
    4 - Configurando o acesso ao banco de dados:
        - routers.py
        - settings adicionar o dict DATABASE_ROUTERS
        - em settings.py adicionar o dict DATABASES do banco de dados remoto
    5 - Criaçao das apps: remote_users, product


### git pull from repo
    cmd: git clone https://github.com/rubensgoncalvesext/poc_django_auth.git 

### Inicializando o serviço via docker
    cmd: docker compose -f compose.yml build

### Inicializando o serviço via docker
    cmd: docker compose -f compose.yml up

### executando o migrate
    cmd: docker compose -f compose.yml migrate

### restores da base de dados
    cmd: cp file_from_backup.sql poc_external_db:/backup.sql 
    cmd: docker exec poc_external_db pg_restore -U root -d proj_db /backup.sql





