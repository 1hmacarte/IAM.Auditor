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

## 1 - Prepare o ambiente python no terminal GCP de acordo com as bibliotecas que serão usadas :

Flask==2.0.1
google-cloud-logging==3.0.0
google-auth==2.0.2



## Habilite as APIS 

IAM
logs 
cloudbuild
GCR
GCS



## 2- crie um diretório para os arquivos e deploy no CLI do projeto que irá utilizar o app como por exemplo :

home/logsiam/iamauditor


## 3 - Prepare o arquivo do código python no diretório

main.py:

https://github.com/1hmacarte/IAM.Auditor/blob/master/main.py
	

## 4 - Crie um folder para os arquivos html no mesmo diretório de onde ficará o código python, isso faz com que o flask renderize os templates html que serão criados.

Preparae o arquivo da página inicial da aplicação como por exemplo:

index.html:

<!DOCTYPE html>
<html>
<head>
    <title>I AM Auditor</title>
    <style>
        body {
            text-align: center;
            background-color: #191d28;
            color: #fff;
            font-family: Arial, sans-serif;
        }

        h1 {
            font-size: 24px;
            padding: 20px;
            background-color: #306998;
            color: #fff;
        }

        p {
            font-size: 18px;
        }

        nav {
            margin-top: 50px;
        }

        ul {
            list-style-type: none;
            padding: 0;
            margin: 0;
        }

        li {
            display: inline-block;
            margin: 10px;
        }

        a {
            display: inline-block;
            padding: 10px 20px;
            background-color: #4d4dff;
            color: #fff;
            text-decoration: none;
            border-radius: 5px;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
            transition: background-color 0.3s ease-in-out;
        }

        a:hover {
            background-color: #1a1aff;
        }
        
        .cybersecurity-theme {
            background-image: linear-gradient(to right bottom, #2b2e4a, #0e101c);
            color: #fff;
        }
        
        .cybersecurity-button {
            background-color: #ff5f5f;
            color: #fff;
        }
        
        .cybersecurity-button:hover {
            background-color: #ff3b3b;
        }

        .lottie-container {
            display: flex;
            justify-content: center;
            align-items: center;
            margin-top: 20px;
        }
    </style>
</head>
<body>
    <h1 class="cybersecurity-theme">I AM Auditor</h1>
    
    <p class="cybersecurity-theme">Exibição de logs.</p>
    
    <nav>
        <ul>
            <li><a href="/logs" class="cybersecurity-button">Ver Logs</a></li>
        </ul>
    </nav>

    <div class="lottie-container">
        <div id="lottie-animation"></div>
    </div>

    <script src="https://cdnjs.cloudflare.com/ajax/libs/bodymovin/5.7.10/lottie.min.js"></script>
    <script>
        // Configurações do Lottie
        var animationData = {
            container: document.getElementById('lottie-animation'),
            renderer: 'svg',
            loop: true,
            autoplay: true,
            path: '/home/contatohiagomacarte/logs/lottieanimação.json' // Caminho para o arquivo JSON Lottie
        };

        // Carrega a animação com as configurações
        var anim = bodymovin.loadAnimation(animationData);
    </script>
</body>
</html>


5 - Crie a interface de resultados:

<!DOCTYPE html>
<html>
<head>
    <title>I AM Auditor</title>
    <style>
        body {
            text-align: center;
            background-color: #1a1a1a;
            color: #fff;
            font-family: Arial, sans-serif;
        }

        h1 {
            font-size: 24px;
            padding: 20px;
            background-color: #306998;
            color: #fff;
        }

        .card {
            border: 1px solid #4d4dff;
            border-radius: 5px;
            padding: 10px;
            margin-bottom: 10px;
            background-color: #191d28;
            color: #fff;
        }

        pre {
            font-family: Consolas, Monaco, 'Courier New', Courier, monospace;
            font-size: 14px;
            white-space: pre-wrap;
            word-wrap: break-word;
        }
    </style>
</head>
<body>
    <h1>I AM Auditor</h1>
    <div>
        {% for log in logs %}
        <div class="card">
            <pre>{{ log }}</pre>
        </div>
        {% endfor %}
    </div>
</body>
</html>

_________________________________________________________________________________________

6 - Crie o arquivo de requerimentos no mesmo diretório raiz onde está o código python.

requirements.txt:

Flask==2.0.1
google-cloud-logging==3.0.0
google-auth==2.0.2

_________________________________________________________________________________________
7 - Crie o arquivo Docker nomeando como Dockerfile.

Dockerfile: 

FROM python:3.9-slim-buster

WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "main.py"]


_________________________________________________________________________________________
Seu diretório deve estar nessa estrutura 

- main.py
- Dockerfile
- requirements.txt
- templates/
  - index.html
  - logs.html

_________________________________________________________________________________________

8 - Navegue até o diretório da aplicação pelo terminal 

execute os comandos 

##Realize o build da imagem docker

docker build -t iamauditor .

##Defina uma tag para imagem
docker tag iamauditor gcr.io/petpotter/iamauditor

##Realize o push da imagem para a biblioteta do Google container registry 

docker push gcr.io/petpotter/iamauditor

_________________________________________________________________________________________
8 - Prepare a VPC de acordo as regras do seu ambiente, nesse exemplo utilizaremos a default

_________________________________________________________________________________________

9 - Prepare a Service account para a aplicação.

Ela precisa da permissão logging.logEntries.list concedida por IAM no projeto que será realizado a execução da auditoria

***
obs: foi realizado a concessão do papel Editor para o desenvolvimento e análise através do security insights para identificar as permissões excesivas.

Exemplo : 

iamauditor@petpotter.iam.gserviceaccount.com

criado uma role customizada para a permissão logging.logEntries.list

Grant access 

_________________________________________________________________________________________
10 - Navegue até o Cloud Run onde para criar um novo serviço

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

