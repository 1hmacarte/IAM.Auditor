# I AM Auditor
[![NPM](https://img.shields.io/npm/l/react)](https://github.com/1hmacarte/IAM.Auditor/blob/master/LICENSE) 

# Sobre o projeto

A ferramenta I AM Auditor é uma aplicação Serveless implantada no Cloud Run da GCP oferece uma solução eficaz para simplificar a análise de logs IAM. Com os benefícios de acesso fácil, flexibilidade, filtragem personalizada e integração com o ecossistema da GCP, você pode melhorar a segurança, a conformidade e a tomada de decisões informadas em relação ao gerenciamento de acesso. Ao utilizar essa ferramenta , você pode obter insights valiosos para o gerenciamento de evidências no IAM.

# Objetivo 
Acesso e Visibilidade: A ferramenta I AM Auditor fornece uma interface amigável para acessar logs específicos do IAM. Isso oferece visibilidade completa sobre as concessões e revogações de roles, permitindo rastrear quem fez as alterações, quais roles foram modificadas e quando essas ações ocorreram.

## Layout Consulta
![Consultar logs](https://github.com/1hmacarte/assets/blob/drwa/consultalogs.jpeg)

## Layout Resultados
![Resultados](https://github.com/1hmacarte/assets/blob/drwa/results.jpeg)


## Desenho de Arquitetura
![](https://github.com/1hmacarte/assets/blob/drwa/Desenho%20tecnico.PNG)

# Tecnologias utilizadas
## Aplicação
- Python
- Flask
- HTML
- Docker

## GCP
- IAM API
- Logs
- Cloud Build
- Google Container Registry
- Cloud Run


## Dependências


# Como executar o projeto

### 1 - Prepare o ambiente python no terminal GCP de acordo com as bibliotecas que serão usadas :

Flask==2.0.1
google-cloud-logging==3.0.0
google-auth==2.0.2



### Habilite as APIS 

IAM
logs 
cloudbuild
GCR
GCS



### 2- crie um diretório para os arquivos e deploy no CLI do projeto que irá utilizar o app como por exemplo :

home/logsiam/iamauditor


### 3 - Prepare o arquivo do código python no diretório

main.py:

https://github.com/1hmacarte/IAM.Auditor/blob/master/main.py
	

### 4 - Crie um folder para os arquivos html no mesmo diretório de onde ficará o código python, isso faz com que o flask renderize os templates html que serão criados.

Preparae o arquivo da página inicial da aplicação como por exemplo:

index.html:

https://github.com/1hmacarte/IAM.Auditor/blob/master/templates/index.html

### 5 - Crie a interface de resultados:

https://github.com/1hmacarte/IAM.Auditor/blob/master/templates/logs.html

### 6 - Crie o arquivo de requerimentos no mesmo diretório raiz onde está o código python.

requirements.txt:

https://github.com/1hmacarte/IAM.Auditor/blob/master/requirements.txt

### 7 - Crie o arquivo Docker nomeando como Dockerfile.

Dockerfile: 

https://github.com/1hmacarte/IAM.Auditor/blob/master/Dockerfile


## Seu diretório deve estar nessa estrutura 

- main.py
- Dockerfile
- requirements.txt
- templates/
  - index.html
  - logs.html



### 8 - Navegue até o diretório da aplicação pelo terminal 


### Realize o build da imagem docker

docker build -t iamauditor .
![Build](https://github.com/1hmacarte/assets/blob/drwa/Docker%20build%20image.jpeg)

### Defina uma tag para imagem
docker tag iamauditor gcr.io/petpotter/iamauditor

##Realize o push da imagem para a biblioteta do Google container registry 

docker push gcr.io/petpotter/iamauditor

![push](https://github.com/1hmacarte/assets/blob/drwa/docker%20push%20image%20to%20gcr.jpeg)


### 9 - Prepare a VPC de acordo as regras do seu ambiente, nesse exemplo utilizaremos a default


### 10 - Prepare a Service account para a aplicação.

Ela precisa da permissão logging.logEntries.list concedida por IAM no projeto que será realizado a execução da auditoria

***
obs: foi realizado a concessão do papel Editor na fase de primeiro desenvolvimento e análise através do security insights para identificar as permissões excesivas.

Exemplo : 

iamauditor@petpotter.iam.gserviceaccount.com

criado uma role customizada para a permissão logging.logEntries.list

Grant access 

![push](https://github.com/1hmacarte/assets/blob/drwa/create%20service%20account.jpeg)


### 11 - Navegue até o Cloud Run onde para criar um novo serviço

Defina as preferências como:

-Container image URL :

gcr.io/petpotter/iamauditor@sha256:d315e7aa687d0d158b0d5d921579cd4763b6f3ad35460352f.........

-Service name :

iamauditor

-Region :

como por exemplo 

south america

-Autoscaling : 


-Ingress control(Restricts network access to your Cloud Run service.)


***
Internal
Allow traffic from VPCs and certain Google Cloud services in your project, Shared VPC, regional internal Application Load Balancers, and traffic allowed by VPC service controls.(Acesso restrito configurado em VPC service controls )

All
Allow direct access to your service from the internet (Acesso direto por url)
***

Neste exemplo utilizaremos a opção por URL

- Authentication(Cloud Run services have stable and secure HTTPS endpoints by default. The permission to invoke the service over HTTPS is managed via Cloud IAM.)

***

Allow unauthenticated invocations
Check this if you are creating a public API or website. (Site publico)

Require authentication
Manage authorized users with Cloud IAM. (restrição por Cloud IAM)

***
Neste exemplo utilizaremos a opção Allow unauthenticated invocations
Check this if you are creating a public API or website. (Site publico)

***
-Não será definido VPC neste caso pois não estou realizando o deploy dentro de uma org 
***

-Na aba security defina a Service account criada para a aplicação 

Service account :  iamauditor@petpotter.iam.gserviceaccount.com

-Encryption

Google-managed encryption key
No configuration required

Customer-managed encryption key (CMEK)
Manage via Google Cloud Key Management Service

Neste exemplo utilizaremos a opção de cripitografia gerenciada pelo Google (Google-managed encryption key
No configuration required)

Clique em Create
_________________________________________________________________________________________

Acesse a aplicação através do link disponibilizado e execute a query.

Será possível obter os logs 


```bash

```


```bash

```

# Autor

Hiago Souza 

https://www.linkedin.com/in/hiago-souza-b27941187/

