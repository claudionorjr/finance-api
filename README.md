<h4 align="center"> 
	🚧  Finance Api 🚀 Em construção...  🚧
</h4>

# Finance API

O objetivo é trabalhar a interação de micro-serviços, armazenando, processando e disponibilizando os dados. É considerado trabalhar com as melhores práticas de TI.

O repositório esta dividido em três micro-serviços. Estes interagem entre si, através do uso de API. Cada serviço lida com dados pessoais financeiros.

## Descrições dos Projetos
### Projeto Base A:
Os dados disponibilizado neste projeto, lida com informações pessoais, como:

* Nome Completo
* CPF
* RG
* Data de Nascimento
* As principais Rendas

Como são dados críticos, é de extrema importanção que a aplicação tenha a preocupação com essas informações trabalhando com a segurança e a integridade. Seguindo esta linha, foi utilizado a crytptografia dos dados, esta feita na aplicação, possibilitando a troca do banco de dados posteriormente. A forma de autenticação é com AUTHBasic, sabendo que não é a melhor forma de proteção. A solução seria gerar tokens a cada requisição, com tempo de expiração. A parde de cadastro dos dados é feita por este endpoint, a partir do momento da requisição de cadastro, é dividido as informações, entre a Base B, jogando os dados nescessários para o calculo financeiro pessoal.

## Projeto Base B:

Da mesma maneira que o projeto Base A, o projeto Base B, também lida com dados críticos. Foi seguido a mesma linha de raciocínio na parte de segurança e integridade dos dados. Este dados são:

* Idade
* Lista de Bens
* Endereço
* Fontes de Renda
* Dívidas

Este serviço seria para integrações de empresas que queiram utilizar destes dados, realizando a análise financeira de seus clientes.

Os dados Pessoais, fazem requisições para a Base A, a fim de obter estas informações. Este vinculo entre os dados, é feito pelo id da pessoa na base A, com isso, este projeto disponibiliza os dados, com o intuido de utilizar o aprendizado de maquina(Machine Learn). Estes dados são disponibilizado de forma que, não seja possível identificar de qual é a pessoa. Todas as requisições exigem a autenticação conforme o projeto Base A.

A cada consulta, é feita uma requisição para o projeto Base C, que informa qual empresa fez a consulta nos dados fornecidos.

## Projeto Base C

Esta Base serve como relatório de transacões em um certo cpf. Recebe as consultas de um cpf da Base b e a registra. Também é disponibilizado a integrações entre terceiros, recebendo a transação do cpf. Estas transações também são as transações em um certo estabelacimento.  

Tipos de informações:

* Última consulta do CPF. 
* Movimentação ﬁnanceira nesse CPF. 
* Dados relacionados a última compra com cartao de crédito vinculado ao CPF.

### 🛠 Tecnologias

As seguintes ferramentas foram usadas na construção do projeto:

- [Python](https://www.python.org/)
- [Flask](https://flask.palletsprojects.com/en/1.1.x/)
- [Java](https://www.java.com/pt_BR/)
- [Sprin Cloud](https://spring.io/)
- [Postgres](https://www.postgresql.org/)
- [Docker](https://www.docker.com/) Não implementado
- [Amazon Lightsail](https://aws.amazon.com/pt/lightsail/)  Não implementado

### Autor
---

<a href="https://lucas-martins.com">
 <img style="border-radius: 50%;" src="https://avatars3.githubusercontent.com/u/21229387?s=460&u=e254bf0490ba4bac61137f52c8974eb58da33dee&v=4" width="100px;" alt=""/>
 <br />
 <sub><b>Lucas Martins</b></sub></a> <a href="https://lucas-martins.com">🚀</a>


[![Linkedin Badge](https://img.shields.io/badge/-Lucas-blue?style=flat-square&logo=Linkedin&logoColor=white&link=https://www.linkedin.com/in/lucas-mcast/)](https://www.linkedin.com/in/lucas-mcast) 
[![Gmail Badge](https://img.shields.io/badge/-lucas.martins.c03@gmail.com-c14438?style=flat-square&logo=Gmail&logoColor=white&link=mailto:lucas.martins.c03@gmail.com)](mailto:lucas.martins.c03@gmail.com)
