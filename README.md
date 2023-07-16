# I AM Auditor
[![NPM](https://img.shields.io/npm/l/react)](https://github.com/1hmacarte/IAM.Auditor/blob/master/LICENSE) 

# Sobre o projeto

https://iamauditor-e4lzjl7w6a-rj.a.run.app

A ferramenta I AM Auditor é uma aplicação Serveless implantada no Cloud Run da GCP oferece uma solução eficaz para simplificar a análise de logs IAM. Com os benefícios de acesso fácil, flexibilidade, filtragem personalizada e integração com o ecossistema da GCP, você pode melhorar a segurança, a conformidade e a tomada de decisões informadas em relação ao gerenciamento de acesso. Ao utilizar essa ferramenta , você pode obter insights valiosos para o gerenciamento de evidências no IAM.

# Objetivo 
Acesso e Visibilidade: A ferramenta I AM Auditor fornece uma interface amigável para acessar logs específicos do IAM. Isso oferece visibilidade completa sobre as concessões e revogações de roles, permitindo rastrear quem fez as alterações, quais roles foram modificadas e quando essas ações ocorreram.

## Layout Consulta
![Consultar logs](https://github.com/1hmacarte/assets/blob/drwa/consultalogs.jpeg)

## Layout Resultados
![Resultados](https://github.com/1hmacarte/assets/blob/drwa/results.jpeg)


## Desenho de Arquitetura
![Modelo Conceitual](https://github.com/acenelio/assets/raw/main/sds1/modelo-conceitual.png)

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

## Back end
Pré-requisitos: Java 11

```bash
# clonar repositório
git clone https://github.com/devsuperior/sds1-wmazoni

# entrar na pasta do projeto back end
cd backend

# executar o projeto
./mvnw spring-boot:run
```

## Front end web
Pré-requisitos: npm / yarn

```bash
# clonar repositório
git clone https://github.com/devsuperior/sds1-wmazoni

# entrar na pasta do projeto front end web
cd front-web

# instalar dependências
yarn install

# executar o projeto
yarn start
```

# Autor

Wellington Mazoni de Andrade

https://www.linkedin.com/in/wmazoni

